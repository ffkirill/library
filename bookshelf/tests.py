import typing
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from rest_framework.test import APITestCase

from book.models import Book
from .models import BookshelfItem

Items = typing.List[BookshelfItem]
Books = typing.List[Book]


class BookshelfPositionTestCase(APITestCase):

    def prepare(self):
        response = self.client.post(
            '/api/author/',
            {'first_name': 'Name',
             'middle_name': 'Middle',
             'last_name': 'Last'},
             format='json')
        self.assertEqual(response.status_code, 201)
        self.author_url = response.data['url']

        response = self.client.post(
            '/api/book/',
            {'title': 'title',
             'place_of_publication': 'place',
             'publisher': 'pub',
             'type_of_book': 'type',
             'year': '2001-01-01',
             'isbn': 1234567891230,
             'content': File(SimpleUploadedFile('up.txt', b'123')),
             'authors': [self.author_url],
             })

        self.assertEqual(response.status_code, 201)
        self.book_url = response.data['url']

        response = self.client.post(
            '/api/bookshelf/',
            {
                'title': 'Bookshelf'
            },
            format='json'
        )

        self.assertEqual(response.status_code, 201)
        self.bookshelf_url = response.data['url']

    def test_insert_item_btw_a_and_b(self) -> None:
        self.prepare()

        # Insert Item A
        response = self.client.post(
            '/api/bookshelfitem/',
            {
                'bookshelf': self.bookshelf_url,
                'book': self.book_url,
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['position'], '1')

        # Insert Item B
        response = self.client.post(
            '/api/bookshelfitem/',
            {
                'bookshelf': self.bookshelf_url,
                'book': self.book_url,
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['position'], '2')

        # Insert Item C between A and B
        response = self.client.post(
            '/api/bookshelfitem/',
            {
                'bookshelf': self.bookshelf_url,
                'book': self.book_url,
                'position': '1/2'
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['position'], '1/2')

    def test_insert_item_btw_0_and_a(self) -> None:
        self.prepare()

        # Insert Item A
        response = self.client.post(
            '/api/bookshelfitem/',
            {
                'bookshelf': self.bookshelf_url,
                'book': self.book_url,
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['position'], '1')

        # Insert Item B
        response = self.client.post(
            '/api/bookshelfitem/',
            {
                'bookshelf': self.bookshelf_url,
                'book': self.book_url,
                'position': '1/2'
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['position'], '1/2')

    def test_change_position_a_c_b(self) -> None:
        self.prepare()

        # Insert Item A
        response = self.client.post(
            '/api/bookshelfitem/',
            {
                'bookshelf': self.bookshelf_url,
                'book': self.book_url,
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['position'], '1')

        # Insert Item B
        response = self.client.post(
            '/api/bookshelfitem/',
            {
                'bookshelf': self.bookshelf_url,
                'book': self.book_url,
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['position'], '2')

        # Insert Item C
        response = self.client.post(
            '/api/bookshelfitem/',
            {
                'bookshelf': self.bookshelf_url,
                'book': self.book_url,
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['position'], '3')

        # Change position of C to be between A and B
        payload = response.data
        payload['position'] = '3/2'
        response = self.client.put(
            payload['url'],
            payload,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['position'], '3/2')

        # Check sequence A C B
        response = self.client.get('/api/bookshelfitem/')
        self.assertEqual(tuple(item['position'] for item in response.data),
                         ('1', '3/2', '2'))

        # Test filters
        response = self.client.get('/api/bookshelfitem/?bookshelf=1')
        self.assertEqual(tuple(item['position'] for item in response.data),
                         ('1', '3/2', '2'))

        response = self.client.get('/api/bookshelfitem/?bookshelf=22')
        self.assertEqual(len(response.data), 0)
