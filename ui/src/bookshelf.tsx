import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { EventCb, BasicItem, Urls } from './utils';


interface BookshelfSelectorProps {
  items: BasicItem[];
  current?: number;
  onActivateItem: EventCb;
}

//Bookshelf selector
export function BookshelfSelector({items, current, onActivateItem}: BookshelfSelectorProps) {
  const bookshelfLi = (item: BasicItem) => {
    const cls = `bookshelves__item ${item.pk === current? "bookshelves__item-active" : ""}`;
    const action = () => onActivateItem(item.pk);
    return <li class={cls} key={item.pk}>
      <button onClick={action}>{item.title}</button>
    </li>
  };

  const listItems = items.map(bookshelfLi);

  return [
    <h2>Bookshelves</h2>,
    <ul class="bookshelves">{ listItems }</ul>
  ];
}
