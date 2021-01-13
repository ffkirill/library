(function (factory) {
    if (typeof module === "object" && typeof module.exports === "object") {
        var v = factory(require, exports);
        if (v !== undefined) module.exports = v;
    }
    else if (typeof define === "function" && define.amd) {
        define(["require", "exports", "react", "react-dom"], factory);
    }
})(function (require, exports) {
    "use strict";
    exports.__esModule = true;
    var React = require("react");
    var ReactDOM = require("react-dom");
    ReactDOM.render(React.createElement("p", null, "Hello, world!"), document.getElementById('root'));
    console.log("hello");
});
