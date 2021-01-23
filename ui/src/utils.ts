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

// Fraction
export class Fraction {
  num: number;
  denom: number;

  constructor(n: number, d: number) {
    this.num = n;
    this.denom = d;
  }

  middle(other: Fraction) {
    return new Fraction(this.num * other.denom + other.num * this.denom, 2 * this.denom * other.denom);
  }

  middleZero() {
    return new Fraction(this.num, 2 * this.denom);
  }

  middleInf() {
    return new Fraction(Math.ceil(this.num / this.denom), 1);
  }

  const fromStr() {
  }

}