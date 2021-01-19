import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { BasicItem, EventCb } from './utils'
import { BookshelfItem } from './library_container';

export interface BookContainerProps {
  items: BookshelfItem[];
  onMoveUp?: EventCb;
  onMoveDown?: EventCb;
}

export function BookList({items, onMoveUp, onMoveDown}: BookContainerProps) {
  const listItems = items.map((item) => <li class="books__item"> {item.book.title} </li>);

  return [
    <h2>Books:</h2>,
    <ul class="books">
      { listItems }
    </ul>
  ];
}
