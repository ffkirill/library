import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { LibraryContainer } from './library_container';

const Header = () => [
  <h1>Library</h1>,
  <details>A demo Django framework web application</details>
];

ReactDOM.render([
  Header(),
  <LibraryContainer />],
  document.getElementById('root') as HTMLElement
);
