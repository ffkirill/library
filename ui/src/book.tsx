import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { BasicItem, EventCb } from './utils'
import { BookshelfItem } from './library_container';

export interface BookContainerProps {
  items: BookshelfItem[];
  onMoveUp?: EventCb;
  onMoveDown?: EventCb;
  version: number;
}

export function BookList({items, onMoveUp, onMoveDown}: BookContainerProps) {
  const listItems = items.map((item) => <li class="book">
    <span class="book__title">{ item.book_entity.title }</span>
    <button class="book__button" onClick={ () => onMoveUp(item.pk)  }>   Up  </button>
    <button class="book__button" onClick={ () => onMoveDown(item.pk) }> Down </button>
  </li>);

  return [
    <h2>Books:</h2>,
    <ul class="books">
      { listItems }
    </ul>
  ];
}
