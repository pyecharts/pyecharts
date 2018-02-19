define(["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var version = '1.3.6';
    function load_ipython_extension() {
        console.log("jupyter-echarts " + version + " (echarts 3.6.2) has been loaded");
    }
    exports.load_ipython_extension = load_ipython_extension;
});
