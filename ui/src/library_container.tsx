// Container. Contains non UI React Application logic.
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { BasicItem, Urls, Fraction } from './utils';
import { BookshelfSelector } from './bookshelf';
import { BookList } from './book';

export interface BookshelfItem extends BasicItem {
  book_entity: BasicItem;
}

interface LibraryState {
  currentBookshelf?: number,
  bookshelves: BasicItem[],
  books: BookshelfItem[]
}

export class LibraryContainer extends React.Component<{}, LibraryState> {
  state: LibraryState = {
    bookshelves: [],
    books: []
  };

  activateBookshelf = async (pk: number) => {
    const books = await this.fetchBooks(pk);
    (this as React.Component).setState({
      currentBookshelf: pk,
      books: books
    });
  }

  async moveItem(index: number, up: boolean) {
    if (index == 0 && up) return;
    that = this.state.books[index].book_entity;
    if (index == this.state.books.length - 1) {
      const position = Fraction.fromStr(that.position).middleInf();
    } else {
      const position = Fraction.fromStr(that.position).middle(
        up? this.state.books[index-1].book_entity.position :
          this.state.books[index].book_entity.position
      );

    }
    that = this.state.books[index];
  }

  async fetchBookshelves() {
    const response = await fetch(Urls.bookshelves());
    const items = await response.json();
    (this as React.Component).setState({bookshelves: items});
  }

  async fetchBooks(bookshelfId: number) {
    const response = await fetch(Urls.books(bookshelfId));
    return await response.json();
  }

  async componentDidMount() {
    await this.fetchBookshelves();
  }

  render() {
    const selector = <BookshelfSelector items={this.state.bookshelves}
      current={this.state.currentBookshelf}
      onActivateItem={this.activateBookshelf} />;
    const bookList = <BookList items={this.state.books} />;
    return [
      selector,
      bookList
    ]
  }
}
