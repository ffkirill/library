from rest_framework import viewsets

from .models import Bookshelf, BookshelfItem
from .serializers import BookshelfSerializer, BookshelfItemSerializer


class BookshelfViewSet(viewsets.ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer


class BookshelfItemViewSet(viewsets.ModelViewSet):
    queryset = BookshelfItem.objects.all()
    serializer_class = BookshelfItemSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given bookshelf,
        by filtering against a `bookshelf` query parameter in the URL.
        """
        bookshelf_id = self.request.query_params.get('bookshelf', None)
        qs = super().get_queryset()
        if bookshelf_id is not None:
            qs = qs.filter(bookshelf=bookshelf_id)
        return qs
