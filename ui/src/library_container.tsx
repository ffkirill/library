// Container. Contains non UI React Application logic.

import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { BasicItem, Urls} from './utils';
import { BookshelfSelector } from './bookshelf';
import { BookList } from './book';

export interface BookshelfItem extends BasicItem {
  book: BasicItem;
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
