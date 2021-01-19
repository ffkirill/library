export namespace Urls {
 export const bookshelves = () => `/api/bookshelf/`;
 export const books = (pk: Number) => `/api/bookshelfitem/?bookshelf=${pk}`;
}

// Event Processing
export type EventCb = (itemId: number) => void;

// DTO Abstractions
export interface BasicItem {
  pk: number,
  title: string,
  url: string
}
