from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('pk',
                  'url',
                  'first_name',
                  'middle_name',
                  'last_name')

        read_only_fields = ('pk',)


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('pk',
                  'url',
                  'title',
                  'place_of_publication',
                  'publisher',
                  'type_of_book',
                  'year',
                  'isbn',
                  'content',
                  'authors')

        read_only_fields = ('pk',)
