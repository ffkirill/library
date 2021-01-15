from rest_framework import viewsets
from rest_framework import filters

from .models import Bookshelf, BookshelfItem
from .serializers import BookshelfSerializer, BookshelfItemSerializer


class BookshelfRelatedSearchFilter(filters.SearchFilter):
    lookup_prefixes = {'=':  'exact'}
    search_param = 'bookshelf'


class BookshelfViewSet(viewsets.ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer


class BookshelfItemViewSet(viewsets.ModelViewSet):
    queryset = BookshelfItem.objects.all()
    serializer_class = BookshelfItemSerializer
    filter_backends = (BookshelfRelatedSearchFilter, )
    search_fields = ('=bookshelf_id', )
    search_description = 'Bookshelf id'
