(function (factory) {
    if (typeof module === "object" && typeof module.exports === "object") {
        var v = factory(require, exports);
        if (v !== undefined) module.exports = v;
    }
    else if (typeof define === "function" && define.amd) {
        define(["require", "exports", "react", "react-dom", "./library_container"], factory);
    }
})(function (require, exports) {
    "use strict";
    exports.__esModule = true;
    var React = require("react");
    var ReactDOM = require("react-dom");
    var library_container_1 = require("./library_container");
    var Header = function () { return [
        React.createElement("h1", null, "Library"),
        React.createElement("details", null, "A demo Django framework web application")
    ]; };
    ReactDOM.render([
        Header(),
        React.createElement(library_container_1.LibraryContainer, null)
    ], document.getElementById('root'));
});
