from typing import Optional
from fractions import Fraction

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import F
from django.db.transaction import atomic

from ool import VersionField, VersionedMixin
from sequences import Sequence

positions_seq = Sequence('bookshelf_items_order')


class Bookshelf(VersionedMixin, models.Model):
    """Represents Bookshelf
    """
    version = VersionField()
    title = models.CharField(
        max_length=256,
        verbose_name=_("Bookshelf name"))

    def __str__(self):
        return self.title


class BookshelfItemManager(models.Manager):
    def get_queryset(self):
        """Apply fractional order,
        In production use db specific speedups such as functional indices
        """
        return (super()
                .get_queryset()
                .annotate(_position=F('pos_numerator') / F('pos_denominator'),
                          bookshelf_version=F('bookshelf__version'))
                .order_by('_position'))


class BookshelfItem(VersionedMixin, models.Model):
    """Represents book in the bookshelf

    Uses fractional position for ordering, populate it from the sequence

    [See](https://wiki.postgresql.org/wiki/User-specified_ordering_with_fractions)
    The implementation is POC and not optimized or db-specific
    """
    id = models.AutoField(unique=False, primary_key=True)

    bookshelf = models.ForeignKey(to=Bookshelf, verbose_name=_("Bookshelf"),
                                  on_delete=models.CASCADE)

    book = models.ForeignKey(to='book.Book',
                             on_delete=models.CASCADE)

    pos_numerator = models.IntegerField(null=False,
                                        verbose_name=_("Position(numerator)"))

    pos_denominator = models.IntegerField(null=False,
                                          verbose_name=_(
                                              "Position(denominator)"))
    version = VersionField()

    objects = BookshelfItemManager()

    class Meta:
        unique_together = ('pos_numerator', 'pos_denominator')

    def __str__(self):
        return f'Bookshelf item {self.id}, at {self.position}'

    @atomic
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Fill position from the sequence"""
        if self.position is None:
            self.position = Fraction(positions_seq.get_next_value(), 1)
        return super().save(force_insert=False, force_update=False, using=None,
                            update_fields=None)

    @property
    def position(self) -> Optional[Fraction]:
        if self.pos_denominator is None or self.pos_numerator is None:
            return None
        else:
            return Fraction(self.pos_numerator, self.pos_denominator)

    @position.setter
    def position(self, value: Fraction):
        self.pos_numerator = value.numerator
        self.pos_denominator = value.denominator
