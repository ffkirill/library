from fractions import Fraction
from typing import Optional

from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.exceptions import ValidationError

from book.serializers import BookSerializer
from .models import Bookshelf, BookshelfItem


class VersionFieldMixin:
    """Forbid user to fill in version field when creating entity"""
    def create(self: serializers.ModelSerializer, validated_data):
        if frozenset(self.Meta.version_fields) & validated_data.keys():
            raise ValidationError(
                'Version fields should be unfilled when creating entity')
        return super().create(validated_data)


class FractionField(serializers.Field):
    """Performs literal <-> Fraction() conversion
    """
    def to_representation(self, value: Fraction):
        return str(value)

    def to_internal_value(self, data):
        return Fraction(data)


class BookshelfSerializer(VersionFieldMixin,
                          serializers.HyperlinkedModelSerializer):
    """Performs Bookshelf entities (de)serialization"""
    class Meta:
        model = Bookshelf
        fields = ('url', 'pk', 'title', 'version')
        version_fields = ('version', )
        read_only_fields = ('pk', )


class BookshelfItemSerializer(VersionFieldMixin,
                              serializers.HyperlinkedModelSerializer):
    """Performs Bookshelf items (de)serialization"""
    position = FractionField(required=False)
    version = IntegerField(required=False)
    bookshelf_version = IntegerField(required=False)
    book = BookSerializer(read_only=True)

    def create(self, validated_data):
        """DTO position to raw models's position"""
        position: Optional[Fraction] = validated_data.pop('position', None)
        if position:
            validated_data['pos_numerator'] = position.numerator
            validated_data['pos_denominator'] = position.denominator
        instance = super().create(validated_data)
        instance.bookshelf.save()  # Bump bookshelf version
        setattr(instance, 'bookshelf_version', instance.bookshelf.version)
        return instance

    @atomic
    def update(self, instance, validated_data):
        """Touch bookshelf's optimistic lock
        to insure that clients data is up to date"""
        instance.bookshelf.version = validated_data['bookshelf_version']
        instance.bookshelf.save()  # Increase version
        return super(BookshelfItemSerializer, self).update(instance,
                                                           validated_data)

    class Meta:
        model = BookshelfItem
        version_fields = ('version', 'bookshelf_version')
        fields = ('pk',
                  'url',
                  'bookshelf',
                  'book',
                  'position',
                  'version',
                  'bookshelf_version')

        read_only_fields = ('pk',)
