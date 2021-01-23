from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Author(models.Model):
    """
    Author
    """
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return " ".join(el for el in (self.first_name,
                                      self.middle_name,
                                      self.last_name) if el)


class Book(models.Model):
    """
    Publication
    Represents title entity of publication
    Fields are taken from GOST 7.0.4-2006
    """
    title = models.CharField(verbose_name=_("Title, e.g. 'Grammatica Latina'"),
                             max_length=256)

    place_of_publication = models.CharField(verbose_name=
        _("Place of publication, e.g. Moscow"),
        max_length=256)

    publisher = models.CharField(
        verbose_name=_("Publisher, e.g. 'MSU Press'"),
        max_length=256)

    type_of_book = models.CharField(
        verbose_name=_("Type of book, e.g. 'Textbook'"),
        max_length=256)

    year = models.DateField(verbose_name=_("Year of publication"))
    isbn = models.PositiveIntegerField(verbose_name=_("ISBN"), null=True)
    content = models.FileField(upload_to=settings.UPLOADS_PATH)
    authors = models.ManyToManyField(to=Author, related_name='books')

    def __str__(self):
        return self.title
