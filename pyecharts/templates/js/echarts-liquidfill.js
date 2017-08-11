(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory(require("echarts"));
	else if(typeof define === 'function' && define.amd)
		define(["echarts"], factory);
	else if(typeof exports === 'object')
		exports["echarts-liquidfill"] = factory(require("echarts"));
	else
		root["echarts-liquidfill"] = factory(root["echarts"]);
})(this, function(__WEBPACK_EXTERNAL_MODULE_2__) {
return /******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	module.exports = __webpack_require__(1);


/***/ },
/* 1 */
/***/ function(module, exports, __webpack_require__) {

	var echarts = __webpack_require__(2);

	__webpack_require__(3);
	__webpack_require__(6);


	echarts.registerVisual(
	    echarts.util.curry(
	        __webpack_require__(64), 'liquidFill'
	    )
	);


/***/ },
/* 2 */
/***/ function(module, exports) {

	module.exports = __WEBPACK_EXTERNAL_MODULE_2__;

/***/ },
/* 3 */
/***/ function(module, exports, __webpack_require__) {

	var completeDimensions = __webpack_require__(4);
	var echarts = __webpack_require__(2);

	echarts.extendSeriesModel({

	    type: 'series.liquidFill',

	    visualColorAccessPath: 'textStyle.normal.color',

	    optionUpdated: function () {
	        var option = this.option;
	        option.gridSize = Math.max(Math.floor(option.gridSize), 4);
	    },

	    getInitialData: function (option, ecModel) {
	        var dimensions = completeDimensions(['value'], option.data);
	        var list = new echarts.List(dimensions, this);
	        list.initData(option.data);
	        return list;
	    },

	    defaultOption: {
	        color: ['#294D99', '#156ACF', '#1598ED', '#45BDFF'],
	        center: ['50%', '50%'],
	        radius: '50%',
	        amplitude: '8%',
	        waveLength: '80%',
	        phase: 'auto',
	        period: 'auto',
	        direction: 'right',
	        shape: 'circle',

	        waveAnimation: true,
	        animationEasing: 'linear',
	        animationEasingUpdate: 'linear',
	        animationDuration: 2000,
	        animationDurationUpdate: 1000,

	        outline: {
	            show: true,
	            borderDistance: 8,
	            itemStyle: {
	                color: 'none',
	                borderColor: '#294D99',
	                borderWidth: 8,
	                shadowBlur: 20,
	                shadowColor: 'rgba(0, 0, 0, 0.25)'
	            }
	        },

	        backgroundStyle: {
	            color: '#E3F7FF'
	        },

	        itemStyle: {
	            normal: {
	                opacity: 0.95,
	                shadowBlur: 50,
	                shadowColor: 'rgba(0, 0, 0, 0.4)'
	            },
	            emphasis: {
	                opacity: 0.8
	            }
	        },

	        label: {
	            normal: {
	                show: true,
	                textStyle: {
	                    color: '#294D99',
	                    insideColor: '#fff',
	                    fontSize: 50,
	                    fontWeight: 'bold',

	                    align: 'center',
	                    baseline: 'middle'
	                },
	                position: 'inside'
	            }
	        }
	    }
	});


/***/ },
/* 4 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * Complete dimensions by data (guess dimension).
	 */


	    var zrUtil = __webpack_require__(5);

	    /**
	     * Complete the dimensions array guessed from the data structure.
	     * @param  {Array.<string>} dimensions      Necessary dimensions, like ['x', 'y']
	     * @param  {Array} data                     Data list. [[1, 2, 3], [2, 3, 4]]
	     * @param  {Array.<string>} [defaultNames]    Default names to fill not necessary dimensions, like ['value']
	     * @param  {string} [extraPrefix]             Prefix of name when filling the left dimensions.
	     * @return {Array.<string>}
	     */
	    function completeDimensions(dimensions, data, defaultNames, extraPrefix) {
	        if (!data) {
	            return dimensions;
	        }

	        var value0 = retrieveValue(data[0]);
	        var dimSize = zrUtil.isArray(value0) && value0.length || 1;

	        defaultNames = defaultNames || [];
	        extraPrefix = extraPrefix || 'extra';
	        for (var i = 0; i < dimSize; i++) {
	            if (!dimensions[i]) {
	                var name = defaultNames[i] || (extraPrefix + (i - defaultNames.length));
	                dimensions[i] = guessOrdinal(data, i)
	                    ? {type: 'ordinal', name: name}
	                    : name;
	            }
	        }

	        return dimensions;
	    }

	    // The rule should not be complex, otherwise user might not
	    // be able to known where the data is wrong.
	    var guessOrdinal = completeDimensions.guessOrdinal = function (data, dimIndex) {
	        for (var i = 0, len = data.length; i < len; i++) {
	            var value = retrieveValue(data[i]);

	            if (!zrUtil.isArray(value)) {
	                return false;
	            }

	            var value = value[dimIndex];
	            if (value != null && isFinite(value)) {
	                return false;
	            }
	            else if (zrUtil.isString(value) && value !== '-') {
	                return true;
	            }
	        }
	        return false;
	    };

	    function retrieveValue(o) {
	        return zrUtil.isArray(o) ? o : zrUtil.isObject(o) ? o.value: o;
	    }

	    module.exports = completeDimensions;



/***/ },
/* 5 */
/***/ function(module, exports) {

	/**
	 * @module zrender/core/util
	 */


	    // 閻劋绨径鍕倞merge閺冭埖妫ゅ▔鏇憾閸樺挷ate缁涘顕挒锛勬畱闂傤噣顣�
	    var BUILTIN_OBJECT = {
	        '[object Function]': 1,
	        '[object RegExp]': 1,
	        '[object Date]': 1,
	        '[object Error]': 1,
	        '[object CanvasGradient]': 1,
	        '[object CanvasPattern]': 1,
	        // For node-canvas
	        '[object Image]': 1,
	        '[object Canvas]': 1
	    };

	    var TYPED_ARRAY = {
	        '[object Int8Array]': 1,
	        '[object Uint8Array]': 1,
	        '[object Uint8ClampedArray]': 1,
	        '[object Int16Array]': 1,
	        '[object Uint16Array]': 1,
	        '[object Int32Array]': 1,
	        '[object Uint32Array]': 1,
	        '[object Float32Array]': 1,
	        '[object Float64Array]': 1
	    };

	    var objToString = Object.prototype.toString;

	    var arrayProto = Array.prototype;
	    var nativeForEach = arrayProto.forEach;
	    var nativeFilter = arrayProto.filter;
	    var nativeSlice = arrayProto.slice;
	    var nativeMap = arrayProto.map;
	    var nativeReduce = arrayProto.reduce;

	    /**
	     * Those data types can be cloned:
	     *     Plain object, Array, TypedArray, number, string, null, undefined.
	     * Those data types will be assgined using the orginal data:
	     *     BUILTIN_OBJECT
	     * Instance of user defined class will be cloned to a plain object, without
	     * properties in prototype.
	     * Other data types is not supported (not sure what will happen).
	     *
	     * Caution: do not support clone Date, for performance consideration.
	     * (There might be a large number of date in `series.data`).
	     * So date should not be modified in and out of echarts.
	     *
	     * @param {*} source
	     * @return {*} new
	     */
	    function clone(source) {
	        if (source == null || typeof source != 'object') {
	            return source;
	        }

	        var result = source;
	        var typeStr = objToString.call(source);

	        if (typeStr === '[object Array]') {
	            result = [];
	            for (var i = 0, len = source.length; i < len; i++) {
	                result[i] = clone(source[i]);
	            }
	        }
	        else if (TYPED_ARRAY[typeStr]) {
	            result = source.constructor.from(source);
	        }
	        else if (!BUILTIN_OBJECT[typeStr] && !isDom(source)) {
	            result = {};
	            for (var key in source) {
	                if (source.hasOwnProperty(key)) {
	                    result[key] = clone(source[key]);
	                }
	            }
	        }

	        return result;
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {*} target
	     * @param {*} source
	     * @param {boolean} [overwrite=false]
	     */
	    function merge(target, source, overwrite) {
	        // We should escapse that source is string
	        // and enter for ... in ...
	        if (!isObject(source) || !isObject(target)) {
	            return overwrite ? clone(source) : target;
	        }

	        for (var key in source) {
	            if (source.hasOwnProperty(key)) {
	                var targetProp = target[key];
	                var sourceProp = source[key];

	                if (isObject(sourceProp)
	                    && isObject(targetProp)
	                    && !isArray(sourceProp)
	                    && !isArray(targetProp)
	                    && !isDom(sourceProp)
	                    && !isDom(targetProp)
	                    && !isBuildInObject(sourceProp)
	                    && !isBuildInObject(targetProp)
	                ) {
	                    // 婵″倹鐏夐棁鈧憰渚€鈧帒缍婄憰鍡欐磰閿涘苯姘ㄩ柅鎺戠秺鐠嬪啰鏁erge
	                    merge(targetProp, sourceProp, overwrite);
	                }
	                else if (overwrite || !(key in target)) {
	                    // 閸氾箑鍨崣顏勵槱閻炲攷verwrite娑撶皪rue閿涘本鍨ㄩ懓鍛躬閻╊喗鐖ｇ€电钖勬稉顓熺梾閺堝顒濈仦鐐粹偓褏娈戦幆鍛枌
	                    // NOTE閿涘苯婀� target[key] 娑撳秴鐡ㄩ崷銊ф畱閺冭泛鈧瑤绡冮弰顖滄纯閹恒儴顩惄锟�
	                    target[key] = clone(source[key], true);
	                }
	            }
	        }

	        return target;
	    }

	    /**
	     * @param {Array} targetAndSources The first item is target, and the rests are source.
	     * @param {boolean} [overwrite=false]
	     * @return {*} target
	     */
	    function mergeAll(targetAndSources, overwrite) {
	        var result = targetAndSources[0];
	        for (var i = 1, len = targetAndSources.length; i < len; i++) {
	            result = merge(result, targetAndSources[i], overwrite);
	        }
	        return result;
	    }

	    /**
	     * @param {*} target
	     * @param {*} source
	     * @memberOf module:zrender/core/util
	     */
	    function extend(target, source) {
	        for (var key in source) {
	            if (source.hasOwnProperty(key)) {
	                target[key] = source[key];
	            }
	        }
	        return target;
	    }

	    /**
	     * @param {*} target
	     * @param {*} source
	     * @param {boolen} [overlay=false]
	     * @memberOf module:zrender/core/util
	     */
	    function defaults(target, source, overlay) {
	        for (var key in source) {
	            if (source.hasOwnProperty(key)
	                && (overlay ? source[key] != null : target[key] == null)
	            ) {
	                target[key] = source[key];
	            }
	        }
	        return target;
	    }

	    function createCanvas() {
	        return document.createElement('canvas');
	    }
	    // FIXME
	    var _ctx;
	    function getContext() {
	        if (!_ctx) {
	            // Use util.createCanvas instead of createCanvas
	            // because createCanvas may be overwritten in different environment
	            _ctx = util.createCanvas().getContext('2d');
	        }
	        return _ctx;
	    }

	    /**
	     * 閺屻儴顕楅弫鎵矋娑擃厼鍘撶槐鐘垫畱index
	     * @memberOf module:zrender/core/util
	     */
	    function indexOf(array, value) {
	        if (array) {
	            if (array.indexOf) {
	                return array.indexOf(value);
	            }
	            for (var i = 0, len = array.length; i < len; i++) {
	                if (array[i] === value) {
	                    return i;
	                }
	            }
	        }
	        return -1;
	    }

	    /**
	     * 閺嬪嫰鈧姷琚紒褎澹欓崗宕囬兇
	     *
	     * @memberOf module:zrender/core/util
	     * @param {Function} clazz 濠ф劗琚�
	     * @param {Function} baseClazz 閸╄櫣琚�
	     */
	    function inherits(clazz, baseClazz) {
	        var clazzPrototype = clazz.prototype;
	        function F() {}
	        F.prototype = baseClazz.prototype;
	        clazz.prototype = new F();

	        for (var prop in clazzPrototype) {
	            clazz.prototype[prop] = clazzPrototype[prop];
	        }
	        clazz.prototype.constructor = clazz;
	        clazz.superClass = baseClazz;
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {Object|Function} target
	     * @param {Object|Function} sorce
	     * @param {boolean} overlay
	     */
	    function mixin(target, source, overlay) {
	        target = 'prototype' in target ? target.prototype : target;
	        source = 'prototype' in source ? source.prototype : source;

	        defaults(target, source, overlay);
	    }

	    /**
	     * @param {Array|TypedArray} data
	     */
	    function isArrayLike(data) {
	        if (! data) {
	            return;
	        }
	        if (typeof data == 'string') {
	            return false;
	        }
	        return typeof data.length == 'number';
	    }

	    /**
	     * 閺佹壆绮嶉幋鏍ь嚠鐠烇繝浜堕崢锟�
	     * @memberOf module:zrender/core/util
	     * @param {Object|Array} obj
	     * @param {Function} cb
	     * @param {*} [context]
	     */
	    function each(obj, cb, context) {
	        if (!(obj && cb)) {
	            return;
	        }
	        if (obj.forEach && obj.forEach === nativeForEach) {
	            obj.forEach(cb, context);
	        }
	        else if (obj.length === +obj.length) {
	            for (var i = 0, len = obj.length; i < len; i++) {
	                cb.call(context, obj[i], i, obj);
	            }
	        }
	        else {
	            for (var key in obj) {
	                if (obj.hasOwnProperty(key)) {
	                    cb.call(context, obj[key], key, obj);
	                }
	            }
	        }
	    }

	    /**
	     * 閺佹壆绮嶉弰鐘茬殸
	     * @memberOf module:zrender/core/util
	     * @param {Array} obj
	     * @param {Function} cb
	     * @param {*} [context]
	     * @return {Array}
	     */
	    function map(obj, cb, context) {
	        if (!(obj && cb)) {
	            return;
	        }
	        if (obj.map && obj.map === nativeMap) {
	            return obj.map(cb, context);
	        }
	        else {
	            var result = [];
	            for (var i = 0, len = obj.length; i < len; i++) {
	                result.push(cb.call(context, obj[i], i, obj));
	            }
	            return result;
	        }
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {Array} obj
	     * @param {Function} cb
	     * @param {Object} [memo]
	     * @param {*} [context]
	     * @return {Array}
	     */
	    function reduce(obj, cb, memo, context) {
	        if (!(obj && cb)) {
	            return;
	        }
	        if (obj.reduce && obj.reduce === nativeReduce) {
	            return obj.reduce(cb, memo, context);
	        }
	        else {
	            for (var i = 0, len = obj.length; i < len; i++) {
	                memo = cb.call(context, memo, obj[i], i, obj);
	            }
	            return memo;
	        }
	    }

	    /**
	     * 閺佹壆绮嶆潻鍥ㄦ姢
	     * @memberOf module:zrender/core/util
	     * @param {Array} obj
	     * @param {Function} cb
	     * @param {*} [context]
	     * @return {Array}
	     */
	    function filter(obj, cb, context) {
	        if (!(obj && cb)) {
	            return;
	        }
	        if (obj.filter && obj.filter === nativeFilter) {
	            return obj.filter(cb, context);
	        }
	        else {
	            var result = [];
	            for (var i = 0, len = obj.length; i < len; i++) {
	                if (cb.call(context, obj[i], i, obj)) {
	                    result.push(obj[i]);
	                }
	            }
	            return result;
	        }
	    }

	    /**
	     * 閺佹壆绮嶆い瑙勭叀閹碉拷
	     * @memberOf module:zrender/core/util
	     * @param {Array} obj
	     * @param {Function} cb
	     * @param {*} [context]
	     * @return {Array}
	     */
	    function find(obj, cb, context) {
	        if (!(obj && cb)) {
	            return;
	        }
	        for (var i = 0, len = obj.length; i < len; i++) {
	            if (cb.call(context, obj[i], i, obj)) {
	                return obj[i];
	            }
	        }
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {Function} func
	     * @param {*} context
	     * @return {Function}
	     */
	    function bind(func, context) {
	        var args = nativeSlice.call(arguments, 2);
	        return function () {
	            return func.apply(context, args.concat(nativeSlice.call(arguments)));
	        };
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {Function} func
	     * @return {Function}
	     */
	    function curry(func) {
	        var args = nativeSlice.call(arguments, 1);
	        return function () {
	            return func.apply(this, args.concat(nativeSlice.call(arguments)));
	        };
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {*} value
	     * @return {boolean}
	     */
	    function isArray(value) {
	        return objToString.call(value) === '[object Array]';
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {*} value
	     * @return {boolean}
	     */
	    function isFunction(value) {
	        return typeof value === 'function';
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {*} value
	     * @return {boolean}
	     */
	    function isString(value) {
	        return objToString.call(value) === '[object String]';
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {*} value
	     * @return {boolean}
	     */
	    function isObject(value) {
	        // Avoid a V8 JIT bug in Chrome 19-20.
	        // See https://code.google.com/p/v8/issues/detail?id=2291 for more details.
	        var type = typeof value;
	        return type === 'function' || (!!value && type == 'object');
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {*} value
	     * @return {boolean}
	     */
	    function isBuildInObject(value) {
	        return !!BUILTIN_OBJECT[objToString.call(value)];
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {*} value
	     * @return {boolean}
	     */
	    function isDom(value) {
	        return typeof value === 'object'
	            && typeof value.nodeType === 'number'
	            && typeof value.ownerDocument === 'object';
	    }

	    /**
	     * Whether is exactly NaN. Notice isNaN('a') returns true.
	     * @param {*} value
	     * @return {boolean}
	     */
	    function eqNaN(value) {
	        return value !== value;
	    }

	    /**
	     * If value1 is not null, then return value1, otherwise judget rest of values.
	     * @memberOf module:zrender/core/util
	     * @return {*} Final value
	     */
	    function retrieve(values) {
	        for (var i = 0, len = arguments.length; i < len; i++) {
	            if (arguments[i] != null) {
	                return arguments[i];
	            }
	        }
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {Array} arr
	     * @param {number} startIndex
	     * @param {number} endIndex
	     * @return {Array}
	     */
	    function slice() {
	        return Function.call.apply(nativeSlice, arguments);
	    }

	    /**
	     * @memberOf module:zrender/core/util
	     * @param {boolean} condition
	     * @param {string} message
	     */
	    function assert(condition, message) {
	        if (!condition) {
	            throw new Error(message);
	        }
	    }

	    var util = {
	        inherits: inherits,
	        mixin: mixin,
	        clone: clone,
	        merge: merge,
	        mergeAll: mergeAll,
	        extend: extend,
	        defaults: defaults,
	        getContext: getContext,
	        createCanvas: createCanvas,
	        indexOf: indexOf,
	        slice: slice,
	        find: find,
	        isArrayLike: isArrayLike,
	        each: each,
	        map: map,
	        reduce: reduce,
	        filter: filter,
	        bind: bind,
	        curry: curry,
	        isArray: isArray,
	        isString: isString,
	        isObject: isObject,
	        isFunction: isFunction,
	        isBuildInObject: isBuildInObject,
	        isDom: isDom,
	        eqNaN: eqNaN,
	        retrieve: retrieve,
	        assert: assert,
	        noop: function () {}
	    };
	    module.exports = util;



/***/ },
/* 6 */
/***/ function(module, exports, __webpack_require__) {

	var echarts = __webpack_require__(2);
	var numberUtil = echarts.number;
	var symbolUtil = __webpack_require__(7);
	var parsePercent = numberUtil.parsePercent;

	var LiquidLayout = __webpack_require__(63);

	function getShallow(model, path) {
	    return model && model.getShallow(path);
	}

	echarts.extendChartView({

	    type: 'liquidFill',

	    render: function (seriesModel, ecModel, api) {
	        var group = this.group;
	        group.removeAll();

	        var data = seriesModel.getData();

	        var itemModel = data.getItemModel(0);

	        var center = itemModel.get('center');
	        var radius = itemModel.get('radius');

	        var width = api.getWidth();
	        var height = api.getHeight();
	        var size = Math.min(width, height);
	        // itemStyle
	        var outlineDistance = 0;
	        var outlineBorderWidth = 0;
	        var showOutline = seriesModel.get('outline.show');

	        var waveClips = [];

	        if (showOutline) {
	            outlineDistance = seriesModel.get('outline.borderDistance');
	            outlineBorderWidth = parsePercent(seriesModel.get('outline.itemStyle.borderWidth'), size);
	        }

	        var cx = parsePercent(center[0], width);
	        var cy = parsePercent(center[1], height);
	        var outterRadius = parsePercent(radius, size) / 2;
	        var innerRadius = outterRadius - outlineBorderWidth / 2;
	        var paddingRadius = parsePercent(outlineDistance, size);

	        var wavePath = null;

	        if (showOutline) {
	            var outline = getOutline();
	            outline.style.lineWidth = outlineBorderWidth;
	            group.add(getOutline());
	        }

	        radius = innerRadius - paddingRadius;
	        var left = cx - radius;
	        var top = cy - radius;

	        group.add(getBackground());

	        // each data item for a wave
	        var oldData = this._data;
	        var waves = [];
	        data.diff(oldData)
	            .add(function (idx) {
	                var wave = getWave(idx, false);

	                var waterLevel = wave.shape.waterLevel;
	                wave.shape.waterLevel = radius;
	                echarts.graphic.initProps(wave, {
	                    shape: {
	                        waterLevel: waterLevel
	                    }
	                }, seriesModel);

	                wave.z2 = 2;
	                setWaveAnimation(idx, wave, null);

	                group.add(wave);
	                data.setItemGraphicEl(idx, wave);
	                waves.push(wave);
	            })
	            .update(function (newIdx, oldIdx) {
	                var waveElement = oldData.getItemGraphicEl(oldIdx);

	                // new wave is used to calculate position, but not added
	                var newWave = getWave(newIdx, false, waveElement);
	                // update old wave with parameters of new wave
	                echarts.graphic.updateProps(waveElement, {
	                    shape: newWave.shape,
	                    style: newWave.style
	                }, seriesModel);
	                waveElement.position = newWave.position;
	                waveElement.setClipPath(newWave.clipPath);

	                setWaveAnimation(newIdx, waveElement, waveElement);
	                group.add(waveElement);
	                data.setItemGraphicEl(newIdx, waveElement);
	                waves.push(waveElement);
	            })
	            .remove(function (idx) {
	                var wave = oldData.getItemGraphicEl(idx);
	                group.remove(wave);
	            })
	            .execute();

	        group.add(getText(waves));

	        this._data = data;

	        /**
	         * Get path for outline, background and clipping
	         */
	        function getPath(r, isForClipping) {
	            var symbol = seriesModel.get('shape');
	            if (symbol) {
	                // customed symbol path
	                if (symbol.indexOf('path://') === 0) {
	                    var path = echarts.graphic.makePath(symbol.slice(7), {});
	                    var bouding = path.getBoundingRect();
	                    var width = bouding.width;
	                    var height = bouding.height;
	                    if (width > height) {
	                        height = r * 2 / width * height;
	                        width = r * 2;
	                    }
	                    else {
	                        width = r * 2 / height * width;
	                        height = r * 2;
	                    }

	                    var left = isForClipping ? 0 : cx - width / 2;
	                    var top = isForClipping ? 0 : cy - height / 2;
	                    path = echarts.graphic.makePath(
	                        symbol.slice(7),
	                        {},
	                        new echarts.graphic.BoundingRect(left, top, width, height)
	                    );
	                    if (isForClipping) {
	                        path.position = [-width / 2, -height / 2];
	                    }
	                    return path;
	                }
	                else {
	                    var x = isForClipping ? -r : cx - r;
	                    var y = isForClipping ? -r : cy - r;
	                    if (symbol === 'pin') {
	                        y += r;
	                    }
	                    else if (symbol === 'arrow') {
	                        y -= r;
	                    }
	                    return symbolUtil.createSymbol(symbol, x, y, r * 2, r * 2);
	                }
	            }

	            return new echarts.graphic.Circle({
	                shape: {
	                    cx: isForClipping ? 0 : cx,
	                    cy: isForClipping ? 0 : cy,
	                    r: r
	                }
	            });
	        }
	        /**
	         * Create outline
	         */
	        function getOutline() {
	            var outlinePath = getPath(outterRadius);
	            outlinePath.style.fill = null;

	            outlinePath.setStyle(seriesModel.getModel('outline.itemStyle')
	                .getItemStyle());

	            return outlinePath;
	        }

	        /**
	         * Create background
	         */
	        function getBackground() {
	            // Seperate stroke and fill, so we can use stroke to cover the alias of clipping.
	            var strokePath = getPath(radius);
	            strokePath.setStyle(seriesModel.getModel('backgroundStyle')
	                .getItemStyle());
	            strokePath.style.fill = null;

	            // Stroke is front of wave
	            strokePath.z2 = 5;

	            var fillPath = getPath(radius);
	            fillPath.setStyle(seriesModel.getModel('backgroundStyle')
	                .getItemStyle());
	            fillPath.style.stroke = null;

	            var group = new echarts.graphic.Group();
	            group.add(strokePath);
	            group.add(fillPath);

	            return group;
	        }

	        /**
	         * wave shape
	         */
	        function getWave(idx, isInverse, oldWave) {
	            var itemModel = data.getItemModel(idx);
	            var itemStyleModel = itemModel.getModel('itemStyle');
	            var phase = itemModel.get('phase');
	            var amplitude = parsePercent(itemModel.get('amplitude'),
	                radius * 2);
	            var waveLength = parsePercent(itemModel.get('waveLength'),
	                radius * 2);

	            var value = data.get('value', idx);
	            var waterLevel = radius - value * radius * 2;
	            phase = oldWave ? oldWave.shape.phase
	                : (phase === 'auto' ? idx * Math.PI / 4 : phase);
	            var normalStyle = itemStyleModel.getModel('normal').getItemStyle();
	            normalStyle.fill = data.getItemVisual(idx, 'color');

	            var x = radius * 2;
	            var wave = new LiquidLayout({
	                shape: {
	                    waveLength: waveLength,
	                    radius: radius,
	                    cx: x,
	                    cy: 0,
	                    waterLevel: waterLevel,
	                    amplitude: amplitude,
	                    phase: phase,
	                    inverse: isInverse
	                },
	                style: normalStyle,
	                position: [cx, cy]
	            });
	            wave.shape._waterLevel = waterLevel;

	            var hoverStyle = itemStyleModel.getModel('emphasis').getItemStyle();
	            hoverStyle.lineWidth = 0;
	            echarts.graphic.setHoverStyle(wave, hoverStyle);

	            // clip out the part outside the circle
	            var clip = getPath(radius, true);
	            wave.setClipPath(clip);
	            waveClips.push(clip);

	            return wave;
	        }

	        function setWaveAnimation(idx, wave, oldWave) {
	            var itemModel = data.getItemModel(idx);

	            var maxSpeed = itemModel.get('period');
	            var direction = itemModel.get('direction');

	            var value = data.get('value', idx);
	            var value0 = data.get('value', 0);

	            var phase = itemModel.get('phase');
	            phase = oldWave ? oldWave.shape.phase
	                : (phase === 'auto' ? idx * Math.PI / 4 : phase);

	            var defaultSpeed = function (maxSpeed) {
	                var cnt = data.count();
	                return cnt === 0 ? maxSpeed : maxSpeed *
	                    (0.2 + (cnt - idx) / cnt * 0.8);
	            };
	            var speed = 0;
	            if (maxSpeed === 'auto') {
	                speed = defaultSpeed(5000);
	            }
	            else {
	                speed = typeof maxSpeed === 'function'
	                    ? maxSpeed(value, idx) : maxSpeed;
	            }

	            // phase for moving left/right
	            var phaseOffset = 0;
	            if (direction === 'right' || direction == null) {
	                phaseOffset = Math.PI;
	            }
	            else if (direction === 'left') {
	                phaseOffset = -Math.PI;
	            }
	            else if (direction === 'none') {
	                phaseOffset = 0;
	            }
	            else {
	                console.error('Illegal direction value for liquid fill.');
	            }

	            // wave animation of moving left/right
	            if (direction !== 'none' && itemModel.get('waveAnimation')) {
	                wave
	                    .animate('shape', true)
	                    .when(0, {
	                        phase: phase
	                    })
	                    .when(speed / 2, {
	                        phase: phaseOffset + phase
	                    })
	                    .when(speed, {
	                        phase: phaseOffset * 2 + phase
	                    })
	                    .during(function () {
	                        if (wavePath) {
	                            wavePath.dirty(true);
	                        }
	                        // for (var i = 0; i < waveClips.length; ++i) {
	                        //     if (waveClips[i]) {
	                        //         waveClips[i].dirty(true);
	                        //     }
	                        // }
	                    })
	                    .start();
	            }
	        }

	        /**
	         * text on wave
	         */
	        function getText(waves) {
	            var labelModel = itemModel.getModel('label.normal');
	            var textStyle = labelModel.getModel('textStyle');

	            function formatLabel() {
	                var formatted = seriesModel.getFormattedLabel(0, 'normal');
	                var defaultVal = (data.get('value', 0) * 100);
	                var defaultLabel = data.getName(0) || seriesModel.name;
	                if (!isNaN(defaultVal)) {
	                    defaultLabel = defaultVal.toFixed(0) + '%';
	                }
	                return formatted == null ? defaultLabel : formatted;
	            }

	            var textOption = {
	                z2: 10,
	                shape: {
	                    x: left,
	                    y: top,
	                    width: radius * 2,
	                    height: radius * 2
	                },
	                style: {
	                    fill: 'transparent',
	                    text: formatLabel(),
	                    textAlign: textStyle.get('align'),
	                    textVerticalAlign: textStyle.get('baseline')
	                },
	                silent: true
	            };

	            var outsideTextRect = new echarts.graphic.Rect(textOption);
	            var color = textStyle.get('color');
	            echarts.graphic.setText(outsideTextRect.style, labelModel, color);

	            var insideTextRect = new echarts.graphic.Rect(textOption);
	            var insColor = textStyle.get('insideColor');
	            echarts.graphic.setText(insideTextRect.style, labelModel, insColor);
	            insideTextRect.style.textFill = insColor;

	            var group = new echarts.graphic.Group();
	            group.add(outsideTextRect);
	            group.add(insideTextRect);

	            // clip out waves for insideText
	            var boundingCircle = getPath(radius, true);

	            wavePath = new echarts.graphic.CompoundPath({
	                shape: {
	                    paths: waves
	                },
	                position: [cx, cy]
	            });

	            wavePath.setClipPath(boundingCircle);
	            insideTextRect.setClipPath(wavePath);

	            return group;
	        }
	    }
	});


/***/ },
/* 7 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	// Symbol factory


	    var graphic = __webpack_require__(8);
	    var BoundingRect = __webpack_require__(28);

	    /**
	     * Triangle shape
	     * @inner
	     */
	    var Triangle = graphic.extendShape({
	        type: 'triangle',
	        shape: {
	            cx: 0,
	            cy: 0,
	            width: 0,
	            height: 0
	        },
	        buildPath: function (path, shape) {
	            var cx = shape.cx;
	            var cy = shape.cy;
	            var width = shape.width / 2;
	            var height = shape.height / 2;
	            path.moveTo(cx, cy - height);
	            path.lineTo(cx + width, cy + height);
	            path.lineTo(cx - width, cy + height);
	            path.closePath();
	        }
	    });
	    /**
	     * Diamond shape
	     * @inner
	     */
	    var Diamond = graphic.extendShape({
	        type: 'diamond',
	        shape: {
	            cx: 0,
	            cy: 0,
	            width: 0,
	            height: 0
	        },
	        buildPath: function (path, shape) {
	            var cx = shape.cx;
	            var cy = shape.cy;
	            var width = shape.width / 2;
	            var height = shape.height / 2;
	            path.moveTo(cx, cy - height);
	            path.lineTo(cx + width, cy);
	            path.lineTo(cx, cy + height);
	            path.lineTo(cx - width, cy);
	            path.closePath();
	        }
	    });

	    /**
	     * Pin shape
	     * @inner
	     */
	    var Pin = graphic.extendShape({
	        type: 'pin',
	        shape: {
	            // x, y on the cusp
	            x: 0,
	            y: 0,
	            width: 0,
	            height: 0
	        },

	        buildPath: function (path, shape) {
	            var x = shape.x;
	            var y = shape.y;
	            var w = shape.width / 5 * 3;
	            // Height must be larger than width
	            var h = Math.max(w, shape.height);
	            var r = w / 2;

	            // Dist on y with tangent point and circle center
	            var dy = r * r / (h - r);
	            var cy = y - h + r + dy;
	            var angle = Math.asin(dy / r);
	            // Dist on x with tangent point and circle center
	            var dx = Math.cos(angle) * r;

	            var tanX = Math.sin(angle);
	            var tanY = Math.cos(angle);

	            path.arc(
	                x, cy, r,
	                Math.PI - angle,
	                Math.PI * 2 + angle
	            );

	            var cpLen = r * 0.6;
	            var cpLen2 = r * 0.7;
	            path.bezierCurveTo(
	                x + dx - tanX * cpLen, cy + dy + tanY * cpLen,
	                x, y - cpLen2,
	                x, y
	            );
	            path.bezierCurveTo(
	                x, y - cpLen2,
	                x - dx + tanX * cpLen, cy + dy + tanY * cpLen,
	                x - dx, cy + dy
	            );
	            path.closePath();
	        }
	    });

	    /**
	     * Arrow shape
	     * @inner
	     */
	    var Arrow = graphic.extendShape({

	        type: 'arrow',

	        shape: {
	            x: 0,
	            y: 0,
	            width: 0,
	            height: 0
	        },

	        buildPath: function (ctx, shape) {
	            var height = shape.height;
	            var width = shape.width;
	            var x = shape.x;
	            var y = shape.y;
	            var dx = width / 3 * 2;
	            ctx.moveTo(x, y);
	            ctx.lineTo(x + dx, y + height);
	            ctx.lineTo(x, y + height / 4 * 3);
	            ctx.lineTo(x - dx, y + height);
	            ctx.lineTo(x, y);
	            ctx.closePath();
	        }
	    });

	    /**
	     * Map of path contructors
	     * @type {Object.<string, module:zrender/graphic/Path>}
	     */
	    var symbolCtors = {
	        line: graphic.Line,

	        rect: graphic.Rect,

	        roundRect: graphic.Rect,

	        square: graphic.Rect,

	        circle: graphic.Circle,

	        diamond: Diamond,

	        pin: Pin,

	        arrow: Arrow,

	        triangle: Triangle
	    };

	    var symbolShapeMakers = {

	        line: function (x, y, w, h, shape) {
	            // FIXME
	            shape.x1 = x;
	            shape.y1 = y + h / 2;
	            shape.x2 = x + w;
	            shape.y2 = y + h / 2;
	        },

	        rect: function (x, y, w, h, shape) {
	            shape.x = x;
	            shape.y = y;
	            shape.width = w;
	            shape.height = h;
	        },

	        roundRect: function (x, y, w, h, shape) {
	            shape.x = x;
	            shape.y = y;
	            shape.width = w;
	            shape.height = h;
	            shape.r = Math.min(w, h) / 4;
	        },

	        square: function (x, y, w, h, shape) {
	            var size = Math.min(w, h);
	            shape.x = x;
	            shape.y = y;
	            shape.width = size;
	            shape.height = size;
	        },

	        circle: function (x, y, w, h, shape) {
	            // Put circle in the center of square
	            shape.cx = x + w / 2;
	            shape.cy = y + h / 2;
	            shape.r = Math.min(w, h) / 2;
	        },

	        diamond: function (x, y, w, h, shape) {
	            shape.cx = x + w / 2;
	            shape.cy = y + h / 2;
	            shape.width = w;
	            shape.height = h;
	        },

	        pin: function (x, y, w, h, shape) {
	            shape.x = x + w / 2;
	            shape.y = y + h / 2;
	            shape.width = w;
	            shape.height = h;
	        },

	        arrow: function (x, y, w, h, shape) {
	            shape.x = x + w / 2;
	            shape.y = y + h / 2;
	            shape.width = w;
	            shape.height = h;
	        },

	        triangle: function (x, y, w, h, shape) {
	            shape.cx = x + w / 2;
	            shape.cy = y + h / 2;
	            shape.width = w;
	            shape.height = h;
	        }
	    };

	    var symbolBuildProxies = {};
	    for (var name in symbolCtors) {
	        if (symbolCtors.hasOwnProperty(name)) {
	            symbolBuildProxies[name] = new symbolCtors[name]();
	        }
	    }

	    var Symbol = graphic.extendShape({

	        type: 'symbol',

	        shape: {
	            symbolType: '',
	            x: 0,
	            y: 0,
	            width: 0,
	            height: 0
	        },

	        beforeBrush: function () {
	            var style = this.style;
	            var shape = this.shape;
	            // FIXME
	            if (shape.symbolType === 'pin' && style.textPosition === 'inside') {
	                style.textPosition = ['50%', '40%'];
	                style.textAlign = 'center';
	                style.textVerticalAlign = 'middle';
	            }
	        },

	        buildPath: function (ctx, shape, inBundle) {
	            var symbolType = shape.symbolType;
	            var proxySymbol = symbolBuildProxies[symbolType];
	            if (shape.symbolType !== 'none') {
	                if (!proxySymbol) {
	                    // Default rect
	                    symbolType = 'rect';
	                    proxySymbol = symbolBuildProxies[symbolType];
	                }
	                symbolShapeMakers[symbolType](
	                    shape.x, shape.y, shape.width, shape.height, proxySymbol.shape
	                );
	                proxySymbol.buildPath(ctx, proxySymbol.shape, inBundle);
	            }
	        }
	    });

	    // Provide setColor helper method to avoid determine if set the fill or stroke outside
	    var symbolPathSetColor = function (color) {
	        if (this.type !== 'image') {
	            var symbolStyle = this.style;
	            var symbolShape = this.shape;
	            if (symbolShape && symbolShape.symbolType === 'line') {
	                symbolStyle.stroke = color;
	            }
	            else if (this.__isEmptyBrush) {
	                symbolStyle.stroke = color;
	                symbolStyle.fill = '#fff';
	            }
	            else {
	                // FIXME 閸掋倖鏌囬崶鎯ц埌姒涙ǹ顓婚弰顖氾綖閸忓懓绻曢弰顖涘伎鏉堢櫢绱濇担璺ㄦ暏 onlyStroke ?
	                symbolStyle.fill && (symbolStyle.fill = color);
	                symbolStyle.stroke && (symbolStyle.stroke = color);
	            }
	            this.dirty(false);
	        }
	    };

	    var symbolUtil = {
	        /**
	         * Create a symbol element with given symbol configuration: shape, x, y, width, height, color
	         * @param {string} symbolType
	         * @param {number} x
	         * @param {number} y
	         * @param {number} w
	         * @param {number} h
	         * @param {string} color
	         */
	        createSymbol: function (symbolType, x, y, w, h, color) {
	            var isEmpty = symbolType.indexOf('empty') === 0;
	            if (isEmpty) {
	                symbolType = symbolType.substr(5, 1).toLowerCase() + symbolType.substr(6);
	            }
	            var symbolPath;

	            if (symbolType.indexOf('image://') === 0) {
	                symbolPath = new graphic.Image({
	                    style: {
	                        image: symbolType.slice(8),
	                        x: x,
	                        y: y,
	                        width: w,
	                        height: h
	                    }
	                });
	            }
	            else if (symbolType.indexOf('path://') === 0) {
	                symbolPath = graphic.makePath(symbolType.slice(7), {}, new BoundingRect(x, y, w, h));
	            }
	            else {
	                symbolPath = new Symbol({
	                    shape: {
	                        symbolType: symbolType,
	                        x: x,
	                        y: y,
	                        width: w,
	                        height: h
	                    }
	                });
	            }

	            symbolPath.__isEmptyBrush = isEmpty;

	            symbolPath.setColor = symbolPathSetColor;

	            symbolPath.setColor(color);

	            return symbolPath;
	        }
	    };

	    module.exports = symbolUtil;


/***/ },
/* 8 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';


	    var zrUtil = __webpack_require__(5);

	    var pathTool = __webpack_require__(9);
	    var round = Math.round;
	    var Path = __webpack_require__(10);
	    var colorTool = __webpack_require__(23);
	    var matrix = __webpack_require__(17);
	    var vector = __webpack_require__(18);

	    var graphic = {};

	    graphic.Group = __webpack_require__(41);

	    graphic.Image = __webpack_require__(42);

	    graphic.Text = __webpack_require__(44);

	    graphic.Circle = __webpack_require__(45);

	    graphic.Sector = __webpack_require__(46);

	    graphic.Ring = __webpack_require__(48);

	    graphic.Polygon = __webpack_require__(49);

	    graphic.Polyline = __webpack_require__(53);

	    graphic.Rect = __webpack_require__(54);

	    graphic.Line = __webpack_require__(56);

	    graphic.BezierCurve = __webpack_require__(57);

	    graphic.Arc = __webpack_require__(58);

	    graphic.CompoundPath = __webpack_require__(59);

	    graphic.LinearGradient = __webpack_require__(60);

	    graphic.RadialGradient = __webpack_require__(62);

	    graphic.BoundingRect = __webpack_require__(28);

	    /**
	     * Extend shape with parameters
	     */
	    graphic.extendShape = function (opts) {
	        return Path.extend(opts);
	    };

	    /**
	     * Extend path
	     */
	    graphic.extendPath = function (pathData, opts) {
	        return pathTool.extendFromString(pathData, opts);
	    };

	    /**
	     * Create a path element from path data string
	     * @param {string} pathData
	     * @param {Object} opts
	     * @param {module:zrender/core/BoundingRect} rect
	     * @param {string} [layout=cover] 'center' or 'cover'
	     */
	    graphic.makePath = function (pathData, opts, rect, layout) {
	        var path = pathTool.createFromString(pathData, opts);
	        var boundingRect = path.getBoundingRect();
	        if (rect) {
	            var aspect = boundingRect.width / boundingRect.height;

	            if (layout === 'center') {
	                // Set rect to center, keep width / height ratio.
	                var width = rect.height * aspect;
	                var height;
	                if (width <= rect.width) {
	                    height = rect.height;
	                }
	                else {
	                    width = rect.width;
	                    height = width / aspect;
	                }
	                var cx = rect.x + rect.width / 2;
	                var cy = rect.y + rect.height / 2;

	                rect.x = cx - width / 2;
	                rect.y = cy - height / 2;
	                rect.width = width;
	                rect.height = height;
	            }

	            graphic.resizePath(path, rect);
	        }
	        return path;
	    };

	    graphic.mergePath = pathTool.mergePath,

	    /**
	     * Resize a path to fit the rect
	     * @param {module:zrender/graphic/Path} path
	     * @param {Object} rect
	     */
	    graphic.resizePath = function (path, rect) {
	        if (!path.applyTransform) {
	            return;
	        }

	        var pathRect = path.getBoundingRect();

	        var m = pathRect.calculateTransform(rect);

	        path.applyTransform(m);
	    };

	    /**
	     * Sub pixel optimize line for canvas
	     *
	     * @param {Object} param
	     * @param {Object} [param.shape]
	     * @param {number} [param.shape.x1]
	     * @param {number} [param.shape.y1]
	     * @param {number} [param.shape.x2]
	     * @param {number} [param.shape.y2]
	     * @param {Object} [param.style]
	     * @param {number} [param.style.lineWidth]
	     * @return {Object} Modified param
	     */
	    graphic.subPixelOptimizeLine = function (param) {
	        var subPixelOptimize = graphic.subPixelOptimize;
	        var shape = param.shape;
	        var lineWidth = param.style.lineWidth;

	        if (round(shape.x1 * 2) === round(shape.x2 * 2)) {
	            shape.x1 = shape.x2 = subPixelOptimize(shape.x1, lineWidth, true);
	        }
	        if (round(shape.y1 * 2) === round(shape.y2 * 2)) {
	            shape.y1 = shape.y2 = subPixelOptimize(shape.y1, lineWidth, true);
	        }
	        return param;
	    };

	    /**
	     * Sub pixel optimize rect for canvas
	     *
	     * @param {Object} param
	     * @param {Object} [param.shape]
	     * @param {number} [param.shape.x]
	     * @param {number} [param.shape.y]
	     * @param {number} [param.shape.width]
	     * @param {number} [param.shape.height]
	     * @param {Object} [param.style]
	     * @param {number} [param.style.lineWidth]
	     * @return {Object} Modified param
	     */
	    graphic.subPixelOptimizeRect = function (param) {
	        var subPixelOptimize = graphic.subPixelOptimize;
	        var shape = param.shape;
	        var lineWidth = param.style.lineWidth;
	        var originX = shape.x;
	        var originY = shape.y;
	        var originWidth = shape.width;
	        var originHeight = shape.height;
	        shape.x = subPixelOptimize(shape.x, lineWidth, true);
	        shape.y = subPixelOptimize(shape.y, lineWidth, true);
	        shape.width = Math.max(
	            subPixelOptimize(originX + originWidth, lineWidth, false) - shape.x,
	            originWidth === 0 ? 0 : 1
	        );
	        shape.height = Math.max(
	            subPixelOptimize(originY + originHeight, lineWidth, false) - shape.y,
	            originHeight === 0 ? 0 : 1
	        );
	        return param;
	    };

	    /**
	     * Sub pixel optimize for canvas
	     *
	     * @param {number} position Coordinate, such as x, y
	     * @param {number} lineWidth Should be nonnegative integer.
	     * @param {boolean=} positiveOrNegative Default false (negative).
	     * @return {number} Optimized position.
	     */
	    graphic.subPixelOptimize = function (position, lineWidth, positiveOrNegative) {
	        // Assure that (position + lineWidth / 2) is near integer edge,
	        // otherwise line will be fuzzy in canvas.
	        var doubledPosition = round(position * 2);
	        return (doubledPosition + round(lineWidth)) % 2 === 0
	            ? doubledPosition / 2
	            : (doubledPosition + (positiveOrNegative ? 1 : -1)) / 2;
	    };

	    function hasFillOrStroke(fillOrStroke) {
	        return fillOrStroke != null && fillOrStroke != 'none';
	    }

	    function liftColor(color) {
	        return typeof color === 'string' ? colorTool.lift(color, -0.1) : color;
	    }

	    /**
	     * @private
	     */
	    function cacheElementStl(el) {
	        if (el.__hoverStlDirty) {
	            var stroke = el.style.stroke;
	            var fill = el.style.fill;

	            // Create hoverStyle on mouseover
	            var hoverStyle = el.__hoverStl;
	            hoverStyle.fill = hoverStyle.fill
	                || (hasFillOrStroke(fill) ? liftColor(fill) : null);
	            hoverStyle.stroke = hoverStyle.stroke
	                || (hasFillOrStroke(stroke) ? liftColor(stroke) : null);

	            var normalStyle = {};
	            for (var name in hoverStyle) {
	                if (hoverStyle.hasOwnProperty(name)) {
	                    normalStyle[name] = el.style[name];
	                }
	            }

	            el.__normalStl = normalStyle;

	            el.__hoverStlDirty = false;
	        }
	    }

	    /**
	     * @private
	     */
	    function doSingleEnterHover(el) {
	        if (el.__isHover) {
	            return;
	        }

	        cacheElementStl(el);

	        if (el.useHoverLayer) {
	            el.__zr && el.__zr.addHover(el, el.__hoverStl);
	        }
	        else {
	            el.setStyle(el.__hoverStl);
	            el.z2 += 1;
	        }

	        el.__isHover = true;
	    }

	    /**
	     * @inner
	     */
	    function doSingleLeaveHover(el) {
	        if (!el.__isHover) {
	            return;
	        }

	        var normalStl = el.__normalStl;
	        if (el.useHoverLayer) {
	            el.__zr && el.__zr.removeHover(el);
	        }
	        else {
	            normalStl && el.setStyle(normalStl);
	            el.z2 -= 1;
	        }

	        el.__isHover = false;
	    }

	    /**
	     * @inner
	     */
	    function doEnterHover(el) {
	        el.type === 'group'
	            ? el.traverse(function (child) {
	                if (child.type !== 'group') {
	                    doSingleEnterHover(child);
	                }
	            })
	            : doSingleEnterHover(el);
	    }

	    function doLeaveHover(el) {
	        el.type === 'group'
	            ? el.traverse(function (child) {
	                if (child.type !== 'group') {
	                    doSingleLeaveHover(child);
	                }
	            })
	            : doSingleLeaveHover(el);
	    }

	    /**
	     * @inner
	     */
	    function setElementHoverStl(el, hoverStl) {
	        // If element has sepcified hoverStyle, then use it instead of given hoverStyle
	        // Often used when item group has a label element and it's hoverStyle is different
	        el.__hoverStl = el.hoverStyle || hoverStl || {};
	        el.__hoverStlDirty = true;

	        if (el.__isHover) {
	            cacheElementStl(el);
	        }
	    }

	    /**
	     * @inner
	     */
	    function onElementMouseOver(e) {
	        if (this.__hoverSilentOnTouch && e.zrByTouch) {
	            return;
	        }

	        // Only if element is not in emphasis status
	        !this.__isEmphasis && doEnterHover(this);
	    }

	    /**
	     * @inner
	     */
	    function onElementMouseOut(e) {
	        if (this.__hoverSilentOnTouch && e.zrByTouch) {
	            return;
	        }

	        // Only if element is not in emphasis status
	        !this.__isEmphasis && doLeaveHover(this);
	    }

	    /**
	     * @inner
	     */
	    function enterEmphasis() {
	        this.__isEmphasis = true;
	        doEnterHover(this);
	    }

	    /**
	     * @inner
	     */
	    function leaveEmphasis() {
	        this.__isEmphasis = false;
	        doLeaveHover(this);
	    }

	    /**
	     * Set hover style of element
	     * @param {module:zrender/Element} el
	     * @param {Object} [hoverStyle]
	     * @param {Object} [opt]
	     * @param {boolean} [opt.hoverSilentOnTouch=false]
	     *        In touch device, mouseover event will be trigger on touchstart event
	     *        (see module:zrender/dom/HandlerProxy). By this mechanism, we can
	     *        conviniently use hoverStyle when tap on touch screen without additional
	     *        code for compatibility.
	     *        But if the chart/component has select feature, which usually also use
	     *        hoverStyle, there might be conflict between 'select-highlight' and
	     *        'hover-highlight' especially when roam is enabled (see geo for example).
	     *        In this case, hoverSilentOnTouch should be used to disable hover-highlight
	     *        on touch device.
	     */
	    graphic.setHoverStyle = function (el, hoverStyle, opt) {
	        el.__hoverSilentOnTouch = opt && opt.hoverSilentOnTouch;

	        el.type === 'group'
	            ? el.traverse(function (child) {
	                if (child.type !== 'group') {
	                    setElementHoverStl(child, hoverStyle);
	                }
	            })
	            : setElementHoverStl(el, hoverStyle);

	        // Duplicated function will be auto-ignored, see Eventful.js.
	        el.on('mouseover', onElementMouseOver)
	          .on('mouseout', onElementMouseOut);

	        // Emphasis, normal can be triggered manually
	        el.on('emphasis', enterEmphasis)
	          .on('normal', leaveEmphasis);
	    };

	    /**
	     * Set text option in the style
	     * @param {Object} textStyle
	     * @param {module:echarts/model/Model} labelModel
	     * @param {string} color
	     */
	    graphic.setText = function (textStyle, labelModel, color) {
	        var labelPosition = labelModel.getShallow('position') || 'inside';
	        var labelColor = labelPosition.indexOf('inside') >= 0 ? 'white' : color;
	        var textStyleModel = labelModel.getModel('textStyle');
	        zrUtil.extend(textStyle, {
	            textDistance: labelModel.getShallow('distance') || 5,
	            textFont: textStyleModel.getFont(),
	            textPosition: labelPosition,
	            textFill: textStyleModel.getTextColor() || labelColor
	        });
	    };

	    function animateOrSetProps(isUpdate, el, props, animatableModel, dataIndex, cb) {
	        if (typeof dataIndex === 'function') {
	            cb = dataIndex;
	            dataIndex = null;
	        }
	        var animationEnabled = animatableModel
	            && (
	                animatableModel.ifEnableAnimation
	                ? animatableModel.ifEnableAnimation()
	                // Directly use animation property
	                : animatableModel.getShallow('animation')
	            );

	        if (animationEnabled) {
	            var postfix = isUpdate ? 'Update' : '';
	            var duration = animatableModel
	                && animatableModel.getShallow('animationDuration' + postfix);
	            var animationEasing = animatableModel
	                && animatableModel.getShallow('animationEasing' + postfix);
	            var animationDelay = animatableModel
	                && animatableModel.getShallow('animationDelay' + postfix);
	            if (typeof animationDelay === 'function') {
	                animationDelay = animationDelay(dataIndex);
	            }
	            if (typeof duration === 'function') {
	                duration = duration(dataIndex);
	            }

	            duration > 0
	                ? el.animateTo(props, duration, animationDelay || 0, animationEasing, cb)
	                : (el.attr(props), cb && cb());
	        }
	        else {
	            el.attr(props);
	            cb && cb();
	        }
	    }
	    /**
	     * Update graphic element properties with or without animation according to the configuration in series
	     * @param {module:zrender/Element} el
	     * @param {Object} props
	     * @param {module:echarts/model/Model} [animatableModel]
	     * @param {number} [dataIndex]
	     * @param {Function} [cb]
	     * @example
	     *     graphic.updateProps(el, {
	     *         position: [100, 100]
	     *     }, seriesModel, dataIndex, function () { console.log('Animation done!'); });
	     *     // Or
	     *     graphic.updateProps(el, {
	     *         position: [100, 100]
	     *     }, seriesModel, function () { console.log('Animation done!'); });
	     */
	    graphic.updateProps = function (el, props, animatableModel, dataIndex, cb) {
	        animateOrSetProps(true, el, props, animatableModel, dataIndex, cb);
	    };

	    /**
	     * Init graphic element properties with or without animation according to the configuration in series
	     * @param {module:zrender/Element} el
	     * @param {Object} props
	     * @param {module:echarts/model/Model} [animatableModel]
	     * @param {number} [dataIndex]
	     * @param {Function} cb
	     */
	    graphic.initProps = function (el, props, animatableModel, dataIndex, cb) {
	        animateOrSetProps(false, el, props, animatableModel, dataIndex, cb);
	    };

	    /**
	     * Get transform matrix of target (param target),
	     * in coordinate of its ancestor (param ancestor)
	     *
	     * @param {module:zrender/mixin/Transformable} target
	     * @param {module:zrender/mixin/Transformable} [ancestor]
	     */
	    graphic.getTransform = function (target, ancestor) {
	        var mat = matrix.identity([]);

	        while (target && target !== ancestor) {
	            matrix.mul(mat, target.getLocalTransform(), mat);
	            target = target.parent;
	        }

	        return mat;
	    };

	    /**
	     * Apply transform to an vertex.
	     * @param {Array.<number>} vertex [x, y]
	     * @param {Array.<number>} transform Transform matrix: like [1, 0, 0, 1, 0, 0]
	     * @param {boolean=} invert Whether use invert matrix.
	     * @return {Array.<number>} [x, y]
	     */
	    graphic.applyTransform = function (vertex, transform, invert) {
	        if (invert) {
	            transform = matrix.invert([], transform);
	        }
	        return vector.applyTransform([], vertex, transform);
	    };

	    /**
	     * @param {string} direction 'left' 'right' 'top' 'bottom'
	     * @param {Array.<number>} transform Transform matrix: like [1, 0, 0, 1, 0, 0]
	     * @param {boolean=} invert Whether use invert matrix.
	     * @return {string} Transformed direction. 'left' 'right' 'top' 'bottom'
	     */
	    graphic.transformDirection = function (direction, transform, invert) {

	        // Pick a base, ensure that transform result will not be (0, 0).
	        var hBase = (transform[4] === 0 || transform[5] === 0 || transform[0] === 0)
	            ? 1 : Math.abs(2 * transform[4] / transform[0]);
	        var vBase = (transform[4] === 0 || transform[5] === 0 || transform[2] === 0)
	            ? 1 : Math.abs(2 * transform[4] / transform[2]);

	        var vertex = [
	            direction === 'left' ? -hBase : direction === 'right' ? hBase : 0,
	            direction === 'top' ? -vBase : direction === 'bottom' ? vBase : 0
	        ];

	        vertex = graphic.applyTransform(vertex, transform, invert);

	        return Math.abs(vertex[0]) > Math.abs(vertex[1])
	            ? (vertex[0] > 0 ? 'right' : 'left')
	            : (vertex[1] > 0 ? 'bottom' : 'top');
	    };

	    /**
	     * Apply group transition animation from g1 to g2
	     */
	    graphic.groupTransition = function (g1, g2, animatableModel, cb) {
	        if (!g1 || !g2) {
	            return;
	        }

	        function getElMap(g) {
	            var elMap = {};
	            g.traverse(function (el) {
	                if (!el.isGroup && el.anid) {
	                    elMap[el.anid] = el;
	                }
	            });
	            return elMap;
	        }
	        function getAnimatableProps(el) {
	            var obj = {
	                position: vector.clone(el.position),
	                rotation: el.rotation
	            };
	            if (el.shape) {
	                obj.shape = zrUtil.extend({}, el.shape);
	            }
	            return obj;
	        }
	        var elMap1 = getElMap(g1);

	        g2.traverse(function (el) {
	            if (!el.isGroup && el.anid) {
	                var oldEl = elMap1[el.anid];
	                if (oldEl) {
	                    var newProp = getAnimatableProps(el);
	                    el.attr(getAnimatableProps(oldEl));
	                    graphic.updateProps(el, newProp, animatableModel, el.dataIndex);
	                }
	                // else {
	                //     if (el.previousProps) {
	                //         graphic.updateProps
	                //     }
	                // }
	            }
	        });
	    };

	    module.exports = graphic;



/***/ },
/* 9 */
/***/ function(module, exports, __webpack_require__) {

	

	    var Path = __webpack_require__(10);
	    var PathProxy = __webpack_require__(29);
	    var transformPath = __webpack_require__(40);
	    var matrix = __webpack_require__(17);

	    // command chars
	    var cc = [
	        'm', 'M', 'l', 'L', 'v', 'V', 'h', 'H', 'z', 'Z',
	        'c', 'C', 'q', 'Q', 't', 'T', 's', 'S', 'a', 'A'
	    ];

	    var mathSqrt = Math.sqrt;
	    var mathSin = Math.sin;
	    var mathCos = Math.cos;
	    var PI = Math.PI;

	    var vMag = function(v) {
	        return Math.sqrt(v[0] * v[0] + v[1] * v[1]);
	    };
	    var vRatio = function(u, v) {
	        return (u[0] * v[0] + u[1] * v[1]) / (vMag(u) * vMag(v));
	    };
	    var vAngle = function(u, v) {
	        return (u[0] * v[1] < u[1] * v[0] ? -1 : 1)
	                * Math.acos(vRatio(u, v));
	    };

	    function processArc(x1, y1, x2, y2, fa, fs, rx, ry, psiDeg, cmd, path) {
	        var psi = psiDeg * (PI / 180.0);
	        var xp = mathCos(psi) * (x1 - x2) / 2.0
	                 + mathSin(psi) * (y1 - y2) / 2.0;
	        var yp = -1 * mathSin(psi) * (x1 - x2) / 2.0
	                 + mathCos(psi) * (y1 - y2) / 2.0;

	        var lambda = (xp * xp) / (rx * rx) + (yp * yp) / (ry * ry);

	        if (lambda > 1) {
	            rx *= mathSqrt(lambda);
	            ry *= mathSqrt(lambda);
	        }

	        var f = (fa === fs ? -1 : 1)
	            * mathSqrt((((rx * rx) * (ry * ry))
	                    - ((rx * rx) * (yp * yp))
	                    - ((ry * ry) * (xp * xp))) / ((rx * rx) * (yp * yp)
	                    + (ry * ry) * (xp * xp))
	                ) || 0;

	        var cxp = f * rx * yp / ry;
	        var cyp = f * -ry * xp / rx;

	        var cx = (x1 + x2) / 2.0
	                 + mathCos(psi) * cxp
	                 - mathSin(psi) * cyp;
	        var cy = (y1 + y2) / 2.0
	                + mathSin(psi) * cxp
	                + mathCos(psi) * cyp;

	        var theta = vAngle([ 1, 0 ], [ (xp - cxp) / rx, (yp - cyp) / ry ]);
	        var u = [ (xp - cxp) / rx, (yp - cyp) / ry ];
	        var v = [ (-1 * xp - cxp) / rx, (-1 * yp - cyp) / ry ];
	        var dTheta = vAngle(u, v);

	        if (vRatio(u, v) <= -1) {
	            dTheta = PI;
	        }
	        if (vRatio(u, v) >= 1) {
	            dTheta = 0;
	        }
	        if (fs === 0 && dTheta > 0) {
	            dTheta = dTheta - 2 * PI;
	        }
	        if (fs === 1 && dTheta < 0) {
	            dTheta = dTheta + 2 * PI;
	        }

	        path.addData(cmd, cx, cy, rx, ry, theta, dTheta, psi, fs);
	    }

	    function createPathProxyFromString(data) {
	        if (!data) {
	            return [];
	        }

	        // command string
	        var cs = data.replace(/-/g, ' -')
	            .replace(/  /g, ' ')
	            .replace(/ /g, ',')
	            .replace(/,,/g, ',');

	        var n;
	        // create pipes so that we can split the data
	        for (n = 0; n < cc.length; n++) {
	            cs = cs.replace(new RegExp(cc[n], 'g'), '|' + cc[n]);
	        }

	        // create array
	        var arr = cs.split('|');
	        // init context point
	        var cpx = 0;
	        var cpy = 0;

	        var path = new PathProxy();
	        var CMD = PathProxy.CMD;

	        var prevCmd;
	        for (n = 1; n < arr.length; n++) {
	            var str = arr[n];
	            var c = str.charAt(0);
	            var off = 0;
	            var p = str.slice(1).replace(/e,-/g, 'e-').split(',');
	            var cmd;

	            if (p.length > 0 && p[0] === '') {
	                p.shift();
	            }

	            for (var i = 0; i < p.length; i++) {
	                p[i] = parseFloat(p[i]);
	            }
	            while (off < p.length && !isNaN(p[off])) {
	                if (isNaN(p[0])) {
	                    break;
	                }
	                var ctlPtx;
	                var ctlPty;

	                var rx;
	                var ry;
	                var psi;
	                var fa;
	                var fs;

	                var x1 = cpx;
	                var y1 = cpy;

	                // convert l, H, h, V, and v to L
	                switch (c) {
	                    case 'l':
	                        cpx += p[off++];
	                        cpy += p[off++];
	                        cmd = CMD.L;
	                        path.addData(cmd, cpx, cpy);
	                        break;
	                    case 'L':
	                        cpx = p[off++];
	                        cpy = p[off++];
	                        cmd = CMD.L;
	                        path.addData(cmd, cpx, cpy);
	                        break;
	                    case 'm':
	                        cpx += p[off++];
	                        cpy += p[off++];
	                        cmd = CMD.M;
	                        path.addData(cmd, cpx, cpy);
	                        c = 'l';
	                        break;
	                    case 'M':
	                        cpx = p[off++];
	                        cpy = p[off++];
	                        cmd = CMD.M;
	                        path.addData(cmd, cpx, cpy);
	                        c = 'L';
	                        break;
	                    case 'h':
	                        cpx += p[off++];
	                        cmd = CMD.L;
	                        path.addData(cmd, cpx, cpy);
	                        break;
	                    case 'H':
	                        cpx = p[off++];
	                        cmd = CMD.L;
	                        path.addData(cmd, cpx, cpy);
	                        break;
	                    case 'v':
	                        cpy += p[off++];
	                        cmd = CMD.L;
	                        path.addData(cmd, cpx, cpy);
	                        break;
	                    case 'V':
	                        cpy = p[off++];
	                        cmd = CMD.L;
	                        path.addData(cmd, cpx, cpy);
	                        break;
	                    case 'C':
	                        cmd = CMD.C;
	                        path.addData(
	                            cmd, p[off++], p[off++], p[off++], p[off++], p[off++], p[off++]
	                        );
	                        cpx = p[off - 2];
	                        cpy = p[off - 1];
	                        break;
	                    case 'c':
	                        cmd = CMD.C;
	                        path.addData(
	                            cmd,
	                            p[off++] + cpx, p[off++] + cpy,
	                            p[off++] + cpx, p[off++] + cpy,
	                            p[off++] + cpx, p[off++] + cpy
	                        );
	                        cpx += p[off - 2];
	                        cpy += p[off - 1];
	                        break;
	                    case 'S':
	                        ctlPtx = cpx;
	                        ctlPty = cpy;
	                        var len = path.len();
	                        var pathData = path.data;
	                        if (prevCmd === CMD.C) {
	                            ctlPtx += cpx - pathData[len - 4];
	                            ctlPty += cpy - pathData[len - 3];
	                        }
	                        cmd = CMD.C;
	                        x1 = p[off++];
	                        y1 = p[off++];
	                        cpx = p[off++];
	                        cpy = p[off++];
	                        path.addData(cmd, ctlPtx, ctlPty, x1, y1, cpx, cpy);
	                        break;
	                    case 's':
	                        ctlPtx = cpx;
	                        ctlPty = cpy;
	                        var len = path.len();
	                        var pathData = path.data;
	                        if (prevCmd === CMD.C) {
	                            ctlPtx += cpx - pathData[len - 4];
	                            ctlPty += cpy - pathData[len - 3];
	                        }
	                        cmd = CMD.C;
	                        x1 = cpx + p[off++];
	                        y1 = cpy + p[off++];
	                        cpx += p[off++];
	                        cpy += p[off++];
	                        path.addData(cmd, ctlPtx, ctlPty, x1, y1, cpx, cpy);
	                        break;
	                    case 'Q':
	                        x1 = p[off++];
	                        y1 = p[off++];
	                        cpx = p[off++];
	                        cpy = p[off++];
	                        cmd = CMD.Q;
	                        path.addData(cmd, x1, y1, cpx, cpy);
	                        break;
	                    case 'q':
	                        x1 = p[off++] + cpx;
	                        y1 = p[off++] + cpy;
	                        cpx += p[off++];
	                        cpy += p[off++];
	                        cmd = CMD.Q;
	                        path.addData(cmd, x1, y1, cpx, cpy);
	                        break;
	                    case 'T':
	                        ctlPtx = cpx;
	                        ctlPty = cpy;
	                        var len = path.len();
	                        var pathData = path.data;
	                        if (prevCmd === CMD.Q) {
	                            ctlPtx += cpx - pathData[len - 4];
	                            ctlPty += cpy - pathData[len - 3];
	                        }
	                        cpx = p[off++];
	                        cpy = p[off++];
	                        cmd = CMD.Q;
	                        path.addData(cmd, ctlPtx, ctlPty, cpx, cpy);
	                        break;
	                    case 't':
	                        ctlPtx = cpx;
	                        ctlPty = cpy;
	                        var len = path.len();
	                        var pathData = path.data;
	                        if (prevCmd === CMD.Q) {
	                            ctlPtx += cpx - pathData[len - 4];
	                            ctlPty += cpy - pathData[len - 3];
	                        }
	                        cpx += p[off++];
	                        cpy += p[off++];
	                        cmd = CMD.Q;
	                        path.addData(cmd, ctlPtx, ctlPty, cpx, cpy);
	                        break;
	                    case 'A':
	                        rx = p[off++];
	                        ry = p[off++];
	                        psi = p[off++];
	                        fa = p[off++];
	                        fs = p[off++];

	                        x1 = cpx, y1 = cpy;
	                        cpx = p[off++];
	                        cpy = p[off++];
	                        cmd = CMD.A;
	                        processArc(
	                            x1, y1, cpx, cpy, fa, fs, rx, ry, psi, cmd, path
	                        );
	                        break;
	                    case 'a':
	                        rx = p[off++];
	                        ry = p[off++];
	                        psi = p[off++];
	                        fa = p[off++];
	                        fs = p[off++];

	                        x1 = cpx, y1 = cpy;
	                        cpx += p[off++];
	                        cpy += p[off++];
	                        cmd = CMD.A;
	                        processArc(
	                            x1, y1, cpx, cpy, fa, fs, rx, ry, psi, cmd, path
	                        );
	                        break;
	                }
	            }

	            if (c === 'z' || c === 'Z') {
	                cmd = CMD.Z;
	                path.addData(cmd);
	            }

	            prevCmd = cmd;
	        }

	        path.toStatic();

	        return path;
	    }

	    // TODO Optimize double memory cost problem
	    function createPathOptions(str, opts) {
	        var pathProxy = createPathProxyFromString(str);
	        var transform;
	        opts = opts || {};
	        opts.buildPath = function (path) {
	            path.setData(pathProxy.data);
	            transform && transformPath(path, transform);
	            // Svg and vml renderer don't have context
	            var ctx = path.getContext();
	            if (ctx) {
	                path.rebuildPath(ctx);
	            }
	        };

	        opts.applyTransform = function (m) {
	            if (!transform) {
	                transform = matrix.create();
	            }
	            matrix.mul(transform, m, transform);
	            this.dirty(true);
	        };

	        return opts;
	    }

	    module.exports = {
	        /**
	         * Create a Path object from path string data
	         * http://www.w3.org/TR/SVG/paths.html#PathData
	         * @param  {Object} opts Other options
	         */
	        createFromString: function (str, opts) {
	            return new Path(createPathOptions(str, opts));
	        },

	        /**
	         * Create a Path class from path string data
	         * @param  {string} str
	         * @param  {Object} opts Other options
	         */
	        extendFromString: function (str, opts) {
	            return Path.extend(createPathOptions(str, opts));
	        },

	        /**
	         * Merge multiple paths
	         */
	        // TODO Apply transform
	        // TODO stroke dash
	        // TODO Optimize double memory cost problem
	        mergePath: function (pathEls, opts) {
	            var pathList = [];
	            var len = pathEls.length;
	            for (var i = 0; i < len; i++) {
	                var pathEl = pathEls[i];
	                if (pathEl.__dirty) {
	                    pathEl.buildPath(pathEl.path, pathEl.shape, true);
	                }
	                pathList.push(pathEl.path);
	            }

	            var pathBundle = new Path(opts);
	            pathBundle.buildPath = function (path) {
	                path.appendPath(pathList);
	                // Svg and vml renderer don't have context
	                var ctx = path.getContext();
	                if (ctx) {
	                    path.rebuildPath(ctx);
	                }
	            };

	            return pathBundle;
	        }
	    };


/***/ },
/* 10 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * Path element
	 * @module zrender/graphic/Path
	 */



	    var Displayable = __webpack_require__(11);
	    var zrUtil = __webpack_require__(5);
	    var PathProxy = __webpack_require__(29);
	    var pathContain = __webpack_require__(32);

	    var Pattern = __webpack_require__(39);
	    var getCanvasPattern = Pattern.prototype.getCanvasPattern;

	    var abs = Math.abs;

	    /**
	     * @alias module:zrender/graphic/Path
	     * @extends module:zrender/graphic/Displayable
	     * @constructor
	     * @param {Object} opts
	     */
	    function Path(opts) {
	        Displayable.call(this, opts);

	        /**
	         * @type {module:zrender/core/PathProxy}
	         * @readOnly
	         */
	        this.path = new PathProxy();
	    }

	    Path.prototype = {

	        constructor: Path,

	        type: 'path',

	        __dirtyPath: true,

	        strokeContainThreshold: 5,

	        brush: function (ctx, prevEl) {
	            var style = this.style;
	            var path = this.path;
	            var hasStroke = style.hasStroke();
	            var hasFill = style.hasFill();
	            var fill = style.fill;
	            var stroke = style.stroke;
	            var hasFillGradient = hasFill && !!(fill.colorStops);
	            var hasStrokeGradient = hasStroke && !!(stroke.colorStops);
	            var hasFillPattern = hasFill && !!(fill.image);
	            var hasStrokePattern = hasStroke && !!(stroke.image);

	            style.bind(ctx, this, prevEl);
	            this.setTransform(ctx);

	            if (this.__dirty) {
	                var rect = this.getBoundingRect();
	                // Update gradient because bounding rect may changed
	                if (hasFillGradient) {
	                    this._fillGradient = style.getGradient(ctx, fill, rect);
	                }
	                if (hasStrokeGradient) {
	                    this._strokeGradient = style.getGradient(ctx, stroke, rect);
	                }
	            }
	            // Use the gradient or pattern
	            if (hasFillGradient) {
	                // PENDING If may have affect the state
	                ctx.fillStyle = this._fillGradient;
	            }
	            else if (hasFillPattern) {
	                ctx.fillStyle = getCanvasPattern.call(fill, ctx);
	            }
	            if (hasStrokeGradient) {
	                ctx.strokeStyle = this._strokeGradient;
	            }
	            else if (hasStrokePattern) {
	                ctx.strokeStyle = getCanvasPattern.call(stroke, ctx);
	            }

	            var lineDash = style.lineDash;
	            var lineDashOffset = style.lineDashOffset;

	            var ctxLineDash = !!ctx.setLineDash;

	            // Update path sx, sy
	            var scale = this.getGlobalScale();
	            path.setScale(scale[0], scale[1]);

	            // Proxy context
	            // Rebuild path in following 2 cases
	            // 1. Path is dirty
	            // 2. Path needs javascript implemented lineDash stroking.
	            //    In this case, lineDash information will not be saved in PathProxy
	            if (this.__dirtyPath || (
	                lineDash && !ctxLineDash && hasStroke
	            )) {
	                path = this.path.beginPath(ctx);

	                // Setting line dash before build path
	                if (lineDash && !ctxLineDash) {
	                    path.setLineDash(lineDash);
	                    path.setLineDashOffset(lineDashOffset);
	                }

	                this.buildPath(path, this.shape, false);

	                // Clear path dirty flag
	                this.__dirtyPath = false;
	            }
	            else {
	                // Replay path building
	                ctx.beginPath();
	                this.path.rebuildPath(ctx);
	            }

	            hasFill && path.fill(ctx);

	            if (lineDash && ctxLineDash) {
	                ctx.setLineDash(lineDash);
	                ctx.lineDashOffset = lineDashOffset;
	            }

	            hasStroke && path.stroke(ctx);

	            if (lineDash && ctxLineDash) {
	                // PENDING
	                // Remove lineDash
	                ctx.setLineDash([]);
	            }


	            this.restoreTransform(ctx);

	            // Draw rect text
	            if (style.text != null) {
	                // var rect = this.getBoundingRect();
	                this.drawRectText(ctx, this.getBoundingRect());
	            }
	        },

	        // When bundling path, some shape may decide if use moveTo to begin a new subpath or closePath
	        // Like in circle
	        buildPath: function (ctx, shapeCfg, inBundle) {},

	        getBoundingRect: function () {
	            var rect = this._rect;
	            var style = this.style;
	            var needsUpdateRect = !rect;
	            if (needsUpdateRect) {
	                var path = this.path;
	                if (this.__dirtyPath) {
	                    path.beginPath();
	                    this.buildPath(path, this.shape, false);
	                }
	                rect = path.getBoundingRect();
	            }
	            this._rect = rect;

	            if (style.hasStroke()) {
	                // Needs update rect with stroke lineWidth when
	                // 1. Element changes scale or lineWidth
	                // 2. Shape is changed
	                var rectWithStroke = this._rectWithStroke || (this._rectWithStroke = rect.clone());
	                if (this.__dirty || needsUpdateRect) {
	                    rectWithStroke.copy(rect);
	                    // FIXME Must after updateTransform
	                    var w = style.lineWidth;
	                    // PENDING, Min line width is needed when line is horizontal or vertical
	                    var lineScale = style.strokeNoScale ? this.getLineScale() : 1;

	                    // Only add extra hover lineWidth when there are no fill
	                    if (!style.hasFill()) {
	                        w = Math.max(w, this.strokeContainThreshold || 4);
	                    }
	                    // Consider line width
	                    // Line scale can't be 0;
	                    if (lineScale > 1e-10) {
	                        rectWithStroke.width += w / lineScale;
	                        rectWithStroke.height += w / lineScale;
	                        rectWithStroke.x -= w / lineScale / 2;
	                        rectWithStroke.y -= w / lineScale / 2;
	                    }
	                }

	                // Return rect with stroke
	                return rectWithStroke;
	            }

	            return rect;
	        },

	        contain: function (x, y) {
	            var localPos = this.transformCoordToLocal(x, y);
	            var rect = this.getBoundingRect();
	            var style = this.style;
	            x = localPos[0];
	            y = localPos[1];

	            if (rect.contain(x, y)) {
	                var pathData = this.path.data;
	                if (style.hasStroke()) {
	                    var lineWidth = style.lineWidth;
	                    var lineScale = style.strokeNoScale ? this.getLineScale() : 1;
	                    // Line scale can't be 0;
	                    if (lineScale > 1e-10) {
	                        // Only add extra hover lineWidth when there are no fill
	                        if (!style.hasFill()) {
	                            lineWidth = Math.max(lineWidth, this.strokeContainThreshold);
	                        }
	                        if (pathContain.containStroke(
	                            pathData, lineWidth / lineScale, x, y
	                        )) {
	                            return true;
	                        }
	                    }
	                }
	                if (style.hasFill()) {
	                    return pathContain.contain(pathData, x, y);
	                }
	            }
	            return false;
	        },

	        /**
	         * @param  {boolean} dirtyPath
	         */
	        dirty: function (dirtyPath) {
	            if (dirtyPath == null) {
	                dirtyPath = true;
	            }
	            // Only mark dirty, not mark clean
	            if (dirtyPath) {
	                this.__dirtyPath = dirtyPath;
	                this._rect = null;
	            }

	            this.__dirty = true;

	            this.__zr && this.__zr.refresh();

	            // Used as a clipping path
	            if (this.__clipTarget) {
	                this.__clipTarget.dirty();
	            }
	        },

	        /**
	         * Alias for animate('shape')
	         * @param {boolean} loop
	         */
	        animateShape: function (loop) {
	            return this.animate('shape', loop);
	        },

	        // Overwrite attrKV
	        attrKV: function (key, value) {
	            // FIXME
	            if (key === 'shape') {
	                this.setShape(value);
	                this.__dirtyPath = true;
	                this._rect = null;
	            }
	            else {
	                Displayable.prototype.attrKV.call(this, key, value);
	            }
	        },

	        /**
	         * @param {Object|string} key
	         * @param {*} value
	         */
	        setShape: function (key, value) {
	            var shape = this.shape;
	            // Path from string may not have shape
	            if (shape) {
	                if (zrUtil.isObject(key)) {
	                    for (var name in key) {
	                        if (key.hasOwnProperty(name)) {
	                            shape[name] = key[name];
	                        }
	                    }
	                }
	                else {
	                    shape[key] = value;
	                }
	                this.dirty(true);
	            }
	            return this;
	        },

	        getLineScale: function () {
	            var m = this.transform;
	            // Get the line scale.
	            // Determinant of `m` means how much the area is enlarged by the
	            // transformation. So its square root can be used as a scale factor
	            // for width.
	            return m && abs(m[0] - 1) > 1e-10 && abs(m[3] - 1) > 1e-10
	                ? Math.sqrt(abs(m[0] * m[3] - m[2] * m[1]))
	                : 1;
	        }
	    };

	    /**
	     * 閹碘晛鐫嶆稉鈧稉锟� Path element, 濮ｆ柨顩ч弰鐔疯埌閿涘苯娓剧粵澶堚偓锟�
	     * Extend a path element
	     * @param {Object} props
	     * @param {string} props.type Path type
	     * @param {Function} props.init Initialize
	     * @param {Function} props.buildPath Overwrite buildPath method
	     * @param {Object} [props.style] Extended default style config
	     * @param {Object} [props.shape] Extended default shape config
	     */
	    Path.extend = function (defaults) {
	        var Sub = function (opts) {
	            Path.call(this, opts);

	            if (defaults.style) {
	                // Extend default style
	                this.style.extendFrom(defaults.style, false);
	            }

	            // Extend default shape
	            var defaultShape = defaults.shape;
	            if (defaultShape) {
	                this.shape = this.shape || {};
	                var thisShape = this.shape;
	                for (var name in defaultShape) {
	                    if (
	                        ! thisShape.hasOwnProperty(name)
	                        && defaultShape.hasOwnProperty(name)
	                    ) {
	                        thisShape[name] = defaultShape[name];
	                    }
	                }
	            }

	            defaults.init && defaults.init.call(this, opts);
	        };

	        zrUtil.inherits(Sub, Path);

	        // FIXME 娑撳秷鍏� extend position, rotation 缁涘绱╅悽銊ヮ嚠鐠烇拷
	        for (var name in defaults) {
	            // Extending prototype values and methods
	            if (name !== 'style' && name !== 'shape') {
	                Sub.prototype[name] = defaults[name];
	            }
	        }

	        return Sub;
	    };

	    zrUtil.inherits(Path, Displayable);

	    module.exports = Path;


/***/ },
/* 11 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * 閸欘垳绮崚鍓佹畱閸ユ儳鑸伴崺铏硅
	 * Base class of all displayable graphic objects
	 * @module zrender/graphic/Displayable
	 */



	    var zrUtil = __webpack_require__(5);

	    var Style = __webpack_require__(12);

	    var Element = __webpack_require__(13);
	    var RectText = __webpack_require__(26);
	    // var Stateful = require('./mixin/Stateful');

	    /**
	     * @alias module:zrender/graphic/Displayable
	     * @extends module:zrender/Element
	     * @extends module:zrender/graphic/mixin/RectText
	     */
	    function Displayable(opts) {

	        opts = opts || {};

	        Element.call(this, opts);

	        // Extend properties
	        for (var name in opts) {
	            if (
	                opts.hasOwnProperty(name) &&
	                name !== 'style'
	            ) {
	                this[name] = opts[name];
	            }
	        }

	        /**
	         * @type {module:zrender/graphic/Style}
	         */
	        this.style = new Style(opts.style);

	        this._rect = null;
	        // Shapes for cascade clipping.
	        this.__clipPaths = [];

	        // FIXME Stateful must be mixined after style is setted
	        // Stateful.call(this, opts);
	    }

	    Displayable.prototype = {

	        constructor: Displayable,

	        type: 'displayable',

	        /**
	         * Displayable 閺勵垰鎯佹稉楦垮壈閿涘ainter 娑擃厺绱伴弽瑙勫祦鐠囥儲鐖ｇ拋鏉垮灲閺傤厽妲搁崥锕傛付鐟曚焦妲搁崥锕傛付鐟曚線鍣搁弬鎵帛閸掞拷
	         * Dirty flag. From which painter will determine if this displayable object needs brush
	         * @name module:zrender/graphic/Displayable#__dirty
	         * @type {boolean}
	         */
	        __dirty: true,

	        /**
	         * 閸ユ儳鑸伴弰顖氭儊閸欘垵顫嗛敍灞艰礋true閺冩湹绗夌紒妯哄煑閸ユ儳鑸伴敍灞肩稻閺勵垯绮涢懗鍊熜曢崣鎴︾炊閺嶅洣绨ㄦ禒锟�
	         * If ignore drawing of the displayable object. Mouse event will still be triggered
	         * @name module:/zrender/graphic/Displayable#invisible
	         * @type {boolean}
	         * @default false
	         */
	        invisible: false,

	        /**
	         * @name module:/zrender/graphic/Displayable#z
	         * @type {number}
	         * @default 0
	         */
	        z: 0,

	        /**
	         * @name module:/zrender/graphic/Displayable#z
	         * @type {number}
	         * @default 0
	         */
	        z2: 0,

	        /**
	         * z鐏炰康evel閿涘苯鍠呯€规氨绮悽璇叉躬閸濐亜鐪癱anvas娑擄拷
	         * @name module:/zrender/graphic/Displayable#zlevel
	         * @type {number}
	         * @default 0
	         */
	        zlevel: 0,

	        /**
	         * 閺勵垰鎯侀崣顖涘珛閹凤拷
	         * @name module:/zrender/graphic/Displayable#draggable
	         * @type {boolean}
	         * @default false
	         */
	        draggable: false,

	        /**
	         * 閺勵垰鎯佸锝呮躬閹锋牗瀚�
	         * @name module:/zrender/graphic/Displayable#draggable
	         * @type {boolean}
	         * @default false
	         */
	        dragging: false,

	        /**
	         * 閺勵垰鎯侀惄绋跨安姒х姵鐖ｆ禍瀣╂
	         * @name module:/zrender/graphic/Displayable#silent
	         * @type {boolean}
	         * @default false
	         */
	        silent: false,

	        /**
	         * If enable culling
	         * @type {boolean}
	         * @default false
	         */
	        culling: false,

	        /**
	         * Mouse cursor when hovered
	         * @name module:/zrender/graphic/Displayable#cursor
	         * @type {string}
	         */
	        cursor: 'pointer',

	        /**
	         * If hover area is bounding rect
	         * @name module:/zrender/graphic/Displayable#rectHover
	         * @type {string}
	         */
	        rectHover: false,

	        /**
	         * Render the element progressively when the value >= 0,
	         * usefull for large data.
	         * @type {number}
	         */
	        progressive: -1,

	        beforeBrush: function (ctx) {},

	        afterBrush: function (ctx) {},

	        /**
	         * 閸ユ儳鑸扮紒妯哄煑閺傝纭�
	         * @param {Canvas2DRenderingContext} ctx
	         */
	        // Interface
	        brush: function (ctx, prevEl) {},

	        /**
	         * 閼惧嘲褰囬張鈧亸蹇撳瘶閸ュ娲�
	         * @return {module:zrender/core/BoundingRect}
	         */
	        // Interface
	        getBoundingRect: function () {},

	        /**
	         * 閸掋倖鏌囬崸鎰垼 x, y 閺勵垰鎯侀崷銊ユ禈瑜邦澀绗�
	         * If displayable element contain coord x, y
	         * @param  {number} x
	         * @param  {number} y
	         * @return {boolean}
	         */
	        contain: function (x, y) {
	            return this.rectContain(x, y);
	        },

	        /**
	         * @param  {Function} cb
	         * @param  {}   context
	         */
	        traverse: function (cb, context) {
	            cb.call(context, this);
	        },

	        /**
	         * 閸掋倖鏌囬崸鎰垼 x, y 閺勵垰鎯侀崷銊ユ禈瑜般垻娈戦崠鍛纯閻╂帊绗�
	         * If bounding rect of element contain coord x, y
	         * @param  {number} x
	         * @param  {number} y
	         * @return {boolean}
	         */
	        rectContain: function (x, y) {
	            var coord = this.transformCoordToLocal(x, y);
	            var rect = this.getBoundingRect();
	            return rect.contain(coord[0], coord[1]);
	        },

	        /**
	         * 閺嶅洩顔囬崶鎯ц埌閸忓啰绀屾稉楦垮壈閿涘苯鑻熸稉鏂挎躬娑撳绔寸敮褔鍣哥紒锟�
	         * Mark displayable element dirty and refresh next frame
	         */
	        dirty: function () {
	            this.__dirty = true;

	            this._rect = null;

	            this.__zr && this.__zr.refresh();
	        },

	        /**
	         * 閸ユ儳鑸伴弰顖氭儊娴兼俺袝閸欐垳绨ㄦ禒锟�
	         * If displayable object binded any event
	         * @return {boolean}
	         */
	        // TODO, 闁俺绻� bind 缂佹垵鐣鹃惃鍕皑娴狅拷
	        // isSilent: function () {
	        //     return !(
	        //         this.hoverable || this.draggable
	        //         || this.onmousemove || this.onmouseover || this.onmouseout
	        //         || this.onmousedown || this.onmouseup || this.onclick
	        //         || this.ondragenter || this.ondragover || this.ondragleave
	        //         || this.ondrop
	        //     );
	        // },
	        /**
	         * Alias for animate('style')
	         * @param {boolean} loop
	         */
	        animateStyle: function (loop) {
	            return this.animate('style', loop);
	        },

	        attrKV: function (key, value) {
	            if (key !== 'style') {
	                Element.prototype.attrKV.call(this, key, value);
	            }
	            else {
	                this.style.set(value);
	            }
	        },

	        /**
	         * @param {Object|string} key
	         * @param {*} value
	         */
	        setStyle: function (key, value) {
	            this.style.set(key, value);
	            this.dirty(false);
	            return this;
	        },

	        /**
	         * Use given style object
	         * @param  {Object} obj
	         */
	        useStyle: function (obj) {
	            this.style = new Style(obj);
	            this.dirty(false);
	            return this;
	        }
	    };

	    zrUtil.inherits(Displayable, Element);

	    zrUtil.mixin(Displayable, RectText);
	    // zrUtil.mixin(Displayable, Stateful);

	    module.exports = Displayable;


/***/ },
/* 12 */
/***/ function(module, exports) {

	/**
	 * @module zrender/graphic/Style
	 */


	    var STYLE_COMMON_PROPS = [
	        ['shadowBlur', 0], ['shadowOffsetX', 0], ['shadowOffsetY', 0], ['shadowColor', '#000'],
	        ['lineCap', 'butt'], ['lineJoin', 'miter'], ['miterLimit', 10]
	    ];

	    // var SHADOW_PROPS = STYLE_COMMON_PROPS.slice(0, 4);
	    // var LINE_PROPS = STYLE_COMMON_PROPS.slice(4);

	    var Style = function (opts) {
	        this.extendFrom(opts);
	    };

	    function createLinearGradient(ctx, obj, rect) {
	        // var size =
	        var x = obj.x;
	        var x2 = obj.x2;
	        var y = obj.y;
	        var y2 = obj.y2;

	        if (!obj.global) {
	            x = x * rect.width + rect.x;
	            x2 = x2 * rect.width + rect.x;
	            y = y * rect.height + rect.y;
	            y2 = y2 * rect.height + rect.y;
	        }

	        var canvasGradient = ctx.createLinearGradient(x, y, x2, y2);

	        return canvasGradient;
	    }

	    function createRadialGradient(ctx, obj, rect) {
	        var width = rect.width;
	        var height = rect.height;
	        var min = Math.min(width, height);

	        var x = obj.x;
	        var y = obj.y;
	        var r = obj.r;
	        if (!obj.global) {
	            x = x * width + rect.x;
	            y = y * height + rect.y;
	            r = r * min;
	        }

	        var canvasGradient = ctx.createRadialGradient(x, y, 0, x, y, r);

	        return canvasGradient;
	    }


	    Style.prototype = {

	        constructor: Style,

	        /**
	         * @type {string}
	         */
	        fill: '#000000',

	        /**
	         * @type {string}
	         */
	        stroke: null,

	        /**
	         * @type {number}
	         */
	        opacity: 1,

	        /**
	         * @type {Array.<number>}
	         */
	        lineDash: null,

	        /**
	         * @type {number}
	         */
	        lineDashOffset: 0,

	        /**
	         * @type {number}
	         */
	        shadowBlur: 0,

	        /**
	         * @type {number}
	         */
	        shadowOffsetX: 0,

	        /**
	         * @type {number}
	         */
	        shadowOffsetY: 0,

	        /**
	         * @type {number}
	         */
	        lineWidth: 1,

	        /**
	         * If stroke ignore scale
	         * @type {Boolean}
	         */
	        strokeNoScale: false,

	        // Bounding rect text configuration
	        // Not affected by element transform
	        /**
	         * @type {string}
	         */
	        text: null,

	        /**
	         * @type {string}
	         */
	        textFill: '#000',

	        /**
	         * @type {string}
	         */
	        textStroke: null,

	        /**
	         * 'inside', 'left', 'right', 'top', 'bottom'
	         * [x, y]
	         * @type {string|Array.<number>}
	         * @default 'inside'
	         */
	        textPosition: 'inside',

	        /**
	         * [x, y]
	         * @type {Array.<number>}
	         */
	        textOffset: null,

	        /**
	         * @type {string}
	         */
	        textBaseline: null,

	        /**
	         * @type {string}
	         */
	        textAlign: null,

	        /**
	         * @type {string}
	         */
	        textVerticalAlign: null,

	        /**
	         * Only useful in Path and Image element
	         * @type {number}
	         */
	        textDistance: 5,

	        /**
	         * Only useful in Path and Image element
	         * @type {number}
	         */
	        textShadowBlur: 0,

	        /**
	         * Only useful in Path and Image element
	         * @type {number}
	         */
	        textShadowOffsetX: 0,

	        /**
	         * Only useful in Path and Image element
	         * @type {number}
	         */
	        textShadowOffsetY: 0,

	        /**
	         * If transform text
	         * Only useful in Path and Image element
	         * @type {boolean}
	         */
	        textTransform: false,

	        /**
	         * Text rotate around position of Path or Image
	         * Only useful in Path and Image element and textTransform is false.
	         */
	        textRotation: 0,

	        /**
	         * @type {string}
	         * https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/globalCompositeOperation
	         */
	        blend: null,

	        /**
	         * @param {CanvasRenderingContext2D} ctx
	         */
	        bind: function (ctx, el, prevEl) {
	            var style = this;
	            var prevStyle = prevEl && prevEl.style;
	            var firstDraw = !prevStyle;

	            for (var i = 0; i < STYLE_COMMON_PROPS.length; i++) {
	                var prop = STYLE_COMMON_PROPS[i];
	                var styleName = prop[0];

	                if (firstDraw || style[styleName] !== prevStyle[styleName]) {
	                    // FIXME Invalid property value will cause style leak from previous element.
	                    ctx[styleName] = style[styleName] || prop[1];
	                }
	            }

	            if ((firstDraw || style.fill !== prevStyle.fill)) {
	                ctx.fillStyle = style.fill;
	            }
	            if ((firstDraw || style.stroke !== prevStyle.stroke)) {
	                ctx.strokeStyle = style.stroke;
	            }
	            if ((firstDraw || style.opacity !== prevStyle.opacity)) {
	                ctx.globalAlpha = style.opacity == null ? 1 : style.opacity;
	            }

	            if ((firstDraw || style.blend !== prevStyle.blend)) {
	                ctx.globalCompositeOperation = style.blend || 'source-over';
	            }
	            if (this.hasStroke()) {
	                var lineWidth = style.lineWidth;
	                ctx.lineWidth = lineWidth / (
	                    (this.strokeNoScale && el && el.getLineScale) ? el.getLineScale() : 1
	                );
	            }
	        },

	        hasFill: function () {
	            var fill = this.fill;
	            return fill != null && fill !== 'none';
	        },

	        hasStroke: function () {
	            var stroke = this.stroke;
	            return stroke != null && stroke !== 'none' && this.lineWidth > 0;
	        },

	        /**
	         * Extend from other style
	         * @param {zrender/graphic/Style} otherStyle
	         * @param {boolean} overwrite
	         */
	        extendFrom: function (otherStyle, overwrite) {
	            if (otherStyle) {
	                var target = this;
	                for (var name in otherStyle) {
	                    if (otherStyle.hasOwnProperty(name)
	                        && (overwrite || ! target.hasOwnProperty(name))
	                    ) {
	                        target[name] = otherStyle[name];
	                    }
	                }
	            }
	        },

	        /**
	         * Batch setting style with a given object
	         * @param {Object|string} obj
	         * @param {*} [obj]
	         */
	        set: function (obj, value) {
	            if (typeof obj === 'string') {
	                this[obj] = value;
	            }
	            else {
	                this.extendFrom(obj, true);
	            }
	        },

	        /**
	         * Clone
	         * @return {zrender/graphic/Style} [description]
	         */
	        clone: function () {
	            var newStyle = new this.constructor();
	            newStyle.extendFrom(this, true);
	            return newStyle;
	        },

	        getGradient: function (ctx, obj, rect) {
	            var method = obj.type === 'radial' ? createRadialGradient : createLinearGradient;
	            var canvasGradient = method(ctx, obj, rect);
	            var colorStops = obj.colorStops;
	            for (var i = 0; i < colorStops.length; i++) {
	                canvasGradient.addColorStop(
	                    colorStops[i].offset, colorStops[i].color
	                );
	            }
	            return canvasGradient;
	        }
	    };

	    var styleProto = Style.prototype;
	    for (var i = 0; i < STYLE_COMMON_PROPS.length; i++) {
	        var prop = STYLE_COMMON_PROPS[i];
	        if (!(prop[0] in styleProto)) {
	            styleProto[prop[0]] = prop[1];
	        }
	    }

	    // Provide for others
	    Style.getGradient = styleProto.getGradient;

	    module.exports = Style;


/***/ },
/* 13 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	/**
	 * @module zrender/Element
	 */


	    var guid = __webpack_require__(14);
	    var Eventful = __webpack_require__(15);
	    var Transformable = __webpack_require__(16);
	    var Animatable = __webpack_require__(19);
	    var zrUtil = __webpack_require__(5);

	    /**
	     * @alias module:zrender/Element
	     * @constructor
	     * @extends {module:zrender/mixin/Animatable}
	     * @extends {module:zrender/mixin/Transformable}
	     * @extends {module:zrender/mixin/Eventful}
	     */
	    var Element = function (opts) {

	        Transformable.call(this, opts);
	        Eventful.call(this, opts);
	        Animatable.call(this, opts);

	        /**
	         * 閻㈣绔烽崗鍐ID
	         * @type {string}
	         */
	        this.id = opts.id || guid();
	    };

	    Element.prototype = {

	        /**
	         * 閸忓啰绀岀猾璇茬€�
	         * Element type
	         * @type {string}
	         */
	        type: 'element',

	        /**
	         * 閸忓啰绀岄崥宥呯摟
	         * Element name
	         * @type {string}
	         */
	        name: '',

	        /**
	         * ZRender 鐎圭偘绶ョ€电钖勯敍灞肩窗閸︼拷 element 濞ｈ濮為崚锟� zrender 鐎圭偘绶ユ稉顓炴倵閼奉亜濮╃挧瀣偓锟�
	         * ZRender instance will be assigned when element is associated with zrender
	         * @name module:/zrender/Element#__zr
	         * @type {module:zrender/ZRender}
	         */
	        __zr: null,

	        /**
	         * 閸ユ儳鑸伴弰顖氭儊韫囩晫鏆愰敍灞艰礋true閺冭泛鎷烽悾銉ユ禈瑜般垻娈戠紒妯哄煑娴犮儱寮锋禍瀣╂鐟欙箑褰�
	         * If ignore drawing and events of the element object
	         * @name module:/zrender/Element#ignore
	         * @type {boolean}
	         * @default false
	         */
	        ignore: false,

	        /**
	         * 閻劋绨憗浣稿閻ㄥ嫯鐭惧锟�(shape)閿涘本澧嶉張锟� Group 閸愬懐娈戠捄顖氱窞閸︺劎绮崚鑸垫闁垝绱扮悮顐ョ箹娑擃亣鐭惧鍕梿閸擄拷
	         * 鐠囥儴鐭惧鍕窗缂佈勫鐞氼偉顥嗛崙蹇擃嚠鐠烇紕娈戦崣妯诲床
	         * @type {module:zrender/graphic/Path}
	         * @see http://www.w3.org/TR/2dcontext/#clipping-region
	         * @readOnly
	         */
	        clipPath: null,

	        /**
	         * Drift element
	         * @param  {number} dx dx on the global space
	         * @param  {number} dy dy on the global space
	         */
	        drift: function (dx, dy) {
	            switch (this.draggable) {
	                case 'horizontal':
	                    dy = 0;
	                    break;
	                case 'vertical':
	                    dx = 0;
	                    break;
	            }

	            var m = this.transform;
	            if (!m) {
	                m = this.transform = [1, 0, 0, 1, 0, 0];
	            }
	            m[4] += dx;
	            m[5] += dy;

	            this.decomposeTransform();
	            this.dirty(false);
	        },

	        /**
	         * Hook before update
	         */
	        beforeUpdate: function () {},
	        /**
	         * Hook after update
	         */
	        afterUpdate: function () {},
	        /**
	         * Update each frame
	         */
	        update: function () {
	            this.updateTransform();
	        },

	        /**
	         * @param  {Function} cb
	         * @param  {}   context
	         */
	        traverse: function (cb, context) {},

	        /**
	         * @protected
	         */
	        attrKV: function (key, value) {
	            if (key === 'position' || key === 'scale' || key === 'origin') {
	                // Copy the array
	                if (value) {
	                    var target = this[key];
	                    if (!target) {
	                        target = this[key] = [];
	                    }
	                    target[0] = value[0];
	                    target[1] = value[1];
	                }
	            }
	            else {
	                this[key] = value;
	            }
	        },

	        /**
	         * Hide the element
	         */
	        hide: function () {
	            this.ignore = true;
	            this.__zr && this.__zr.refresh();
	        },

	        /**
	         * Show the element
	         */
	        show: function () {
	            this.ignore = false;
	            this.__zr && this.__zr.refresh();
	        },

	        /**
	         * @param {string|Object} key
	         * @param {*} value
	         */
	        attr: function (key, value) {
	            if (typeof key === 'string') {
	                this.attrKV(key, value);
	            }
	            else if (zrUtil.isObject(key)) {
	                for (var name in key) {
	                    if (key.hasOwnProperty(name)) {
	                        this.attrKV(name, key[name]);
	                    }
	                }
	            }

	            this.dirty(false);

	            return this;
	        },

	        /**
	         * @param {module:zrender/graphic/Path} clipPath
	         */
	        setClipPath: function (clipPath) {
	            var zr = this.__zr;
	            if (zr) {
	                clipPath.addSelfToZr(zr);
	            }

	            // Remove previous clip path
	            if (this.clipPath && this.clipPath !== clipPath) {
	                this.removeClipPath();
	            }

	            this.clipPath = clipPath;
	            clipPath.__zr = zr;
	            clipPath.__clipTarget = this;

	            this.dirty(false);
	        },

	        /**
	         */
	        removeClipPath: function () {
	            var clipPath = this.clipPath;
	            if (clipPath) {
	                if (clipPath.__zr) {
	                    clipPath.removeSelfFromZr(clipPath.__zr);
	                }

	                clipPath.__zr = null;
	                clipPath.__clipTarget = null;
	                this.clipPath = null;

	                this.dirty(false);
	            }
	        },

	        /**
	         * Add self from zrender instance.
	         * Not recursively because it will be invoked when element added to storage.
	         * @param {module:zrender/ZRender} zr
	         */
	        addSelfToZr: function (zr) {
	            this.__zr = zr;
	            // 濞ｈ濮為崝銊ф暰
	            var animators = this.animators;
	            if (animators) {
	                for (var i = 0; i < animators.length; i++) {
	                    zr.animation.addAnimator(animators[i]);
	                }
	            }

	            if (this.clipPath) {
	                this.clipPath.addSelfToZr(zr);
	            }
	        },

	        /**
	         * Remove self from zrender instance.
	         * Not recursively because it will be invoked when element added to storage.
	         * @param {module:zrender/ZRender} zr
	         */
	        removeSelfFromZr: function (zr) {
	            this.__zr = null;
	            // 缁夊娅庨崝銊ф暰
	            var animators = this.animators;
	            if (animators) {
	                for (var i = 0; i < animators.length; i++) {
	                    zr.animation.removeAnimator(animators[i]);
	                }
	            }

	            if (this.clipPath) {
	                this.clipPath.removeSelfFromZr(zr);
	            }
	        }
	    };

	    zrUtil.mixin(Element, Animatable);
	    zrUtil.mixin(Element, Transformable);
	    zrUtil.mixin(Element, Eventful);

	    module.exports = Element;


/***/ },
/* 14 */
/***/ function(module, exports) {

	/**
	 * zrender: 閻㈢喐鍨氶崬顖欑id
	 *
	 * @author errorrik (errorrik@gmail.com)
	 */


	    var idStart = 0x0907;

	    module.exports = function () {
	        return idStart++;
	    };



/***/ },
/* 15 */
/***/ function(module, exports) {

	/**
	 * 娴滃娆㈤幍鈺佺潔
	 * @module zrender/mixin/Eventful
	 * @author Kener (@Kener-閺嬫鍢�, kener.linfeng@gmail.com)
	 *         pissang (https://www.github.com/pissang)
	 */


	    var arrySlice = Array.prototype.slice;

	    /**
	     * 娴滃娆㈤崚鍡楀絺閸ｏ拷
	     * @alias module:zrender/mixin/Eventful
	     * @constructor
	     */
	    var Eventful = function () {
	        this._$handlers = {};
	    };

	    Eventful.prototype = {

	        constructor: Eventful,

	        /**
	         * 閸楁洘顐肩憴锕€褰傜紒鎴濈暰閿涘rigger閸氬酣鏀㈠В锟�
	         *
	         * @param {string} event 娴滃娆㈤崥锟�
	         * @param {Function} handler 閸濆秴绨查崙鑺ユ殶
	         * @param {Object} context
	         */
	        one: function (event, handler, context) {
	            var _h = this._$handlers;

	            if (!handler || !event) {
	                return this;
	            }

	            if (!_h[event]) {
	                _h[event] = [];
	            }

	            for (var i = 0; i < _h[event].length; i++) {
	                if (_h[event][i].h === handler) {
	                    return this;
	                }
	            }

	            _h[event].push({
	                h: handler,
	                one: true,
	                ctx: context || this
	            });

	            return this;
	        },

	        /**
	         * 缂佹垵鐣炬禍瀣╂
	         * @param {string} event 娴滃娆㈤崥锟�
	         * @param {Function} handler 娴滃娆㈡径鍕倞閸戣姤鏆�
	         * @param {Object} [context]
	         */
	        on: function (event, handler, context) {
	            var _h = this._$handlers;

	            if (!handler || !event) {
	                return this;
	            }

	            if (!_h[event]) {
	                _h[event] = [];
	            }

	            for (var i = 0; i < _h[event].length; i++) {
	                if (_h[event][i].h === handler) {
	                    return this;
	                }
	            }

	            _h[event].push({
	                h: handler,
	                one: false,
	                ctx: context || this
	            });

	            return this;
	        },

	        /**
	         * 閺勵垰鎯佺紒鎴濈暰娴滃棔绨ㄦ禒锟�
	         * @param  {string}  event
	         * @return {boolean}
	         */
	        isSilent: function (event) {
	            var _h = this._$handlers;
	            return _h[event] && _h[event].length;
	        },

	        /**
	         * 鐟欙絿绮︽禍瀣╂
	         * @param {string} event 娴滃娆㈤崥锟�
	         * @param {Function} [handler] 娴滃娆㈡径鍕倞閸戣姤鏆�
	         */
	        off: function (event, handler) {
	            var _h = this._$handlers;

	            if (!event) {
	                this._$handlers = {};
	                return this;
	            }

	            if (handler) {
	                if (_h[event]) {
	                    var newList = [];
	                    for (var i = 0, l = _h[event].length; i < l; i++) {
	                        if (_h[event][i]['h'] != handler) {
	                            newList.push(_h[event][i]);
	                        }
	                    }
	                    _h[event] = newList;
	                }

	                if (_h[event] && _h[event].length === 0) {
	                    delete _h[event];
	                }
	            }
	            else {
	                delete _h[event];
	            }

	            return this;
	        },

	        /**
	         * 娴滃娆㈤崚鍡楀絺
	         *
	         * @param {string} type 娴滃娆㈢猾璇茬€�
	         */
	        trigger: function (type) {
	            if (this._$handlers[type]) {
	                var args = arguments;
	                var argLen = args.length;

	                if (argLen > 3) {
	                    args = arrySlice.call(args, 1);
	                }

	                var _h = this._$handlers[type];
	                var len = _h.length;
	                for (var i = 0; i < len;) {
	                    // Optimize advise from backbone
	                    switch (argLen) {
	                        case 1:
	                            _h[i]['h'].call(_h[i]['ctx']);
	                            break;
	                        case 2:
	                            _h[i]['h'].call(_h[i]['ctx'], args[1]);
	                            break;
	                        case 3:
	                            _h[i]['h'].call(_h[i]['ctx'], args[1], args[2]);
	                            break;
	                        default:
	                            // have more than 2 given arguments
	                            _h[i]['h'].apply(_h[i]['ctx'], args);
	                            break;
	                    }

	                    if (_h[i]['one']) {
	                        _h.splice(i, 1);
	                        len--;
	                    }
	                    else {
	                        i++;
	                    }
	                }
	            }

	            return this;
	        },

	        /**
	         * 鐢附婀乧ontext閻ㄥ嫪绨ㄦ禒璺哄瀻閸欙拷, 閺堚偓閸氬簼绔存稉顏勫棘閺佺増妲告禍瀣╂閸ョ偠鐨熼惃鍒ntext
	         * @param {string} type 娴滃娆㈢猾璇茬€�
	         */
	        triggerWithContext: function (type) {
	            if (this._$handlers[type]) {
	                var args = arguments;
	                var argLen = args.length;

	                if (argLen > 4) {
	                    args = arrySlice.call(args, 1, args.length - 1);
	                }
	                var ctx = args[args.length - 1];

	                var _h = this._$handlers[type];
	                var len = _h.length;
	                for (var i = 0; i < len;) {
	                    // Optimize advise from backbone
	                    switch (argLen) {
	                        case 1:
	                            _h[i]['h'].call(ctx);
	                            break;
	                        case 2:
	                            _h[i]['h'].call(ctx, args[1]);
	                            break;
	                        case 3:
	                            _h[i]['h'].call(ctx, args[1], args[2]);
	                            break;
	                        default:
	                            // have more than 2 given arguments
	                            _h[i]['h'].apply(ctx, args);
	                            break;
	                    }

	                    if (_h[i]['one']) {
	                        _h.splice(i, 1);
	                        len--;
	                    }
	                    else {
	                        i++;
	                    }
	                }
	            }

	            return this;
	        }
	    };

	    // 鐎电钖勯崣顖欎簰闁俺绻� onxxxx 缂佹垵鐣炬禍瀣╂
	    /**
	     * @event module:zrender/mixin/Eventful#onclick
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#onmouseover
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#onmouseout
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#onmousemove
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#onmousewheel
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#onmousedown
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#onmouseup
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#ondrag
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#ondragstart
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#ondragend
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#ondragenter
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#ondragleave
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#ondragover
	     * @type {Function}
	     * @default null
	     */
	    /**
	     * @event module:zrender/mixin/Eventful#ondrop
	     * @type {Function}
	     * @default null
	     */

	    module.exports = Eventful;



/***/ },
/* 16 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	/**
	 * 閹绘劒绶甸崣妯诲床閹碘晛鐫�
	 * @module zrender/mixin/Transformable
	 * @author pissang (https://www.github.com/pissang)
	 */


	    var matrix = __webpack_require__(17);
	    var vector = __webpack_require__(18);
	    var mIdentity = matrix.identity;

	    var EPSILON = 5e-5;

	    function isNotAroundZero(val) {
	        return val > EPSILON || val < -EPSILON;
	    }

	    /**
	     * @alias module:zrender/mixin/Transformable
	     * @constructor
	     */
	    var Transformable = function (opts) {
	        opts = opts || {};
	        // If there are no given position, rotation, scale
	        if (!opts.position) {
	            /**
	             * 楠炲磭些
	             * @type {Array.<number>}
	             * @default [0, 0]
	             */
	            this.position = [0, 0];
	        }
	        if (opts.rotation == null) {
	            /**
	             * 閺冨娴�
	             * @type {Array.<number>}
	             * @default 0
	             */
	            this.rotation = 0;
	        }
	        if (!opts.scale) {
	            /**
	             * 缂傗晜鏂�
	             * @type {Array.<number>}
	             * @default [1, 1]
	             */
	            this.scale = [1, 1];
	        }
	        /**
	         * 閺冨娴嗛崪宀€缂夐弨鍓ф畱閸樼喓鍋�
	         * @type {Array.<number>}
	         * @default null
	         */
	        this.origin = this.origin || null;
	    };

	    var transformableProto = Transformable.prototype;
	    transformableProto.transform = null;

	    /**
	     * 閸掋倖鏌囬弰顖氭儊闂団偓鐟曚焦婀侀崸鎰垼閸欐ɑ宕�
	     * 婵″倹鐏夐張澶婃綏閺嶅洤褰夐幑锟�, 閸掓瑤绮爌osition, rotation, scale娴犮儱寮烽悥鎯板Ν閻愬湱娈憈ransform鐠侊紕鐣婚崙楦垮殰闊偆娈憈ransform閻晠妯€
	     */
	    transformableProto.needLocalTransform = function () {
	        return isNotAroundZero(this.rotation)
	            || isNotAroundZero(this.position[0])
	            || isNotAroundZero(this.position[1])
	            || isNotAroundZero(this.scale[0] - 1)
	            || isNotAroundZero(this.scale[1] - 1);
	    };

	    transformableProto.updateTransform = function () {
	        var parent = this.parent;
	        var parentHasTransform = parent && parent.transform;
	        var needLocalTransform = this.needLocalTransform();

	        var m = this.transform;
	        if (!(needLocalTransform || parentHasTransform)) {
	            m && mIdentity(m);
	            return;
	        }

	        m = m || matrix.create();

	        if (needLocalTransform) {
	            this.getLocalTransform(m);
	        }
	        else {
	            mIdentity(m);
	        }

	        // 鎼存梻鏁ら悥鎯板Ν閻愮懓褰夐幑锟�
	        if (parentHasTransform) {
	            if (needLocalTransform) {
	                matrix.mul(m, parent.transform, m);
	            }
	            else {
	                matrix.copy(m, parent.transform);
	            }
	        }
	        // 娣囨繂鐡ㄦ潻娆庨嚋閸欐ɑ宕查惌鈺呮█
	        this.transform = m;

	        this.invTransform = this.invTransform || matrix.create();
	        matrix.invert(this.invTransform, m);
	    };

	    transformableProto.getLocalTransform = function (m) {
	        m = m || [];
	        mIdentity(m);

	        var origin = this.origin;

	        var scale = this.scale;
	        var rotation = this.rotation;
	        var position = this.position;
	        if (origin) {
	            // Translate to origin
	            m[4] -= origin[0];
	            m[5] -= origin[1];
	        }
	        matrix.scale(m, m, scale);
	        if (rotation) {
	            matrix.rotate(m, m, rotation);
	        }
	        if (origin) {
	            // Translate back from origin
	            m[4] += origin[0];
	            m[5] += origin[1];
	        }

	        m[4] += position[0];
	        m[5] += position[1];

	        return m;
	    };
	    /**
	     * 鐏忓棜鍤滃杈╂畱transform鎼存梻鏁ら崚鐧眔ntext娑擄拷
	     * @param {Context2D} ctx
	     */
	    transformableProto.setTransform = function (ctx) {
	        var m = this.transform;
	        var dpr = ctx.dpr || 1;
	        if (m) {
	            ctx.setTransform(dpr * m[0], dpr * m[1], dpr * m[2], dpr * m[3], dpr * m[4], dpr * m[5]);
	        }
	        else {
	            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
	        }
	    };

	    transformableProto.restoreTransform = function (ctx) {
	        var m = this.transform;
	        var dpr = ctx.dpr || 1;
	        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
	    }

	    var tmpTransform = [];

	    /**
	     * 閸掑棜袙`transform`閻晠妯€閸掔櫗position`, `rotation`, `scale`
	     */
	    transformableProto.decomposeTransform = function () {
	        if (!this.transform) {
	            return;
	        }
	        var parent = this.parent;
	        var m = this.transform;
	        if (parent && parent.transform) {
	            // Get local transform and decompose them to position, scale, rotation
	            matrix.mul(tmpTransform, parent.invTransform, m);
	            m = tmpTransform;
	        }
	        var sx = m[0] * m[0] + m[1] * m[1];
	        var sy = m[2] * m[2] + m[3] * m[3];
	        var position = this.position;
	        var scale = this.scale;
	        if (isNotAroundZero(sx - 1)) {
	            sx = Math.sqrt(sx);
	        }
	        if (isNotAroundZero(sy - 1)) {
	            sy = Math.sqrt(sy);
	        }
	        if (m[0] < 0) {
	            sx = -sx;
	        }
	        if (m[3] < 0) {
	            sy = -sy;
	        }
	        position[0] = m[4];
	        position[1] = m[5];
	        scale[0] = sx;
	        scale[1] = sy;
	        this.rotation = Math.atan2(-m[1] / sy, m[0] / sx);
	    };

	    /**
	     * Get global scale
	     * @return {Array.<number>}
	     */
	    transformableProto.getGlobalScale = function () {
	        var m = this.transform;
	        if (!m) {
	            return [1, 1];
	        }
	        var sx = Math.sqrt(m[0] * m[0] + m[1] * m[1]);
	        var sy = Math.sqrt(m[2] * m[2] + m[3] * m[3]);
	        if (m[0] < 0) {
	            sx = -sx;
	        }
	        if (m[3] < 0) {
	            sy = -sy;
	        }
	        return [sx, sy];
	    };
	    /**
	     * 閸欐ɑ宕查崸鎰垼娴ｅ秶鐤嗛崚锟� shape 閻ㄥ嫬鐪柈銊ユ綏閺嶅洨鈹栭梻锟�
	     * @method
	     * @param {number} x
	     * @param {number} y
	     * @return {Array.<number>}
	     */
	    transformableProto.transformCoordToLocal = function (x, y) {
	        var v2 = [x, y];
	        var invTransform = this.invTransform;
	        if (invTransform) {
	            vector.applyTransform(v2, v2, invTransform);
	        }
	        return v2;
	    };

	    /**
	     * 閸欐ɑ宕茬仦鈧柈銊ユ綏閺嶅洣缍呯純顔煎煂閸忋劌鐪崸鎰垼缁屾椽妫�
	     * @method
	     * @param {number} x
	     * @param {number} y
	     * @return {Array.<number>}
	     */
	    transformableProto.transformCoordToGlobal = function (x, y) {
	        var v2 = [x, y];
	        var transform = this.transform;
	        if (transform) {
	            vector.applyTransform(v2, v2, transform);
	        }
	        return v2;
	    };

	    module.exports = Transformable;



/***/ },
/* 17 */
/***/ function(module, exports) {

	
	    var ArrayCtor = typeof Float32Array === 'undefined'
	        ? Array
	        : Float32Array;
	    /**
	     * 3x2閻晠妯€閹垮秳缍旂猾锟�
	     * @exports zrender/tool/matrix
	     */
	    var matrix = {
	        /**
	         * 閸掓稑缂撴稉鈧稉顏勫礋娴ｅ秶鐓╅梼锟�
	         * @return {Float32Array|Array.<number>}
	         */
	        create : function() {
	            var out = new ArrayCtor(6);
	            matrix.identity(out);

	            return out;
	        },
	        /**
	         * 鐠佸墽鐤嗛惌鈺呮█娑撳搫宕熸担宥囩叐闂冿拷
	         * @param {Float32Array|Array.<number>} out
	         */
	        identity : function(out) {
	            out[0] = 1;
	            out[1] = 0;
	            out[2] = 0;
	            out[3] = 1;
	            out[4] = 0;
	            out[5] = 0;
	            return out;
	        },
	        /**
	         * 婢跺秴鍩楅惌鈺呮█
	         * @param {Float32Array|Array.<number>} out
	         * @param {Float32Array|Array.<number>} m
	         */
	        copy: function(out, m) {
	            out[0] = m[0];
	            out[1] = m[1];
	            out[2] = m[2];
	            out[3] = m[3];
	            out[4] = m[4];
	            out[5] = m[5];
	            return out;
	        },
	        /**
	         * 閻晠妯€閻╅晲绠�
	         * @param {Float32Array|Array.<number>} out
	         * @param {Float32Array|Array.<number>} m1
	         * @param {Float32Array|Array.<number>} m2
	         */
	        mul : function (out, m1, m2) {
	            // Consider matrix.mul(m, m2, m);
	            // where out is the same as m2.
	            // So use temp variable to escape error.
	            var out0 = m1[0] * m2[0] + m1[2] * m2[1];
	            var out1 = m1[1] * m2[0] + m1[3] * m2[1];
	            var out2 = m1[0] * m2[2] + m1[2] * m2[3];
	            var out3 = m1[1] * m2[2] + m1[3] * m2[3];
	            var out4 = m1[0] * m2[4] + m1[2] * m2[5] + m1[4];
	            var out5 = m1[1] * m2[4] + m1[3] * m2[5] + m1[5];
	            out[0] = out0;
	            out[1] = out1;
	            out[2] = out2;
	            out[3] = out3;
	            out[4] = out4;
	            out[5] = out5;
	            return out;
	        },
	        /**
	         * 楠炲磭些閸欐ɑ宕�
	         * @param {Float32Array|Array.<number>} out
	         * @param {Float32Array|Array.<number>} a
	         * @param {Float32Array|Array.<number>} v
	         */
	        translate : function(out, a, v) {
	            out[0] = a[0];
	            out[1] = a[1];
	            out[2] = a[2];
	            out[3] = a[3];
	            out[4] = a[4] + v[0];
	            out[5] = a[5] + v[1];
	            return out;
	        },
	        /**
	         * 閺冨娴嗛崣妯诲床
	         * @param {Float32Array|Array.<number>} out
	         * @param {Float32Array|Array.<number>} a
	         * @param {number} rad
	         */
	        rotate : function(out, a, rad) {
	            var aa = a[0];
	            var ac = a[2];
	            var atx = a[4];
	            var ab = a[1];
	            var ad = a[3];
	            var aty = a[5];
	            var st = Math.sin(rad);
	            var ct = Math.cos(rad);

	            out[0] = aa * ct + ab * st;
	            out[1] = -aa * st + ab * ct;
	            out[2] = ac * ct + ad * st;
	            out[3] = -ac * st + ct * ad;
	            out[4] = ct * atx + st * aty;
	            out[5] = ct * aty - st * atx;
	            return out;
	        },
	        /**
	         * 缂傗晜鏂侀崣妯诲床
	         * @param {Float32Array|Array.<number>} out
	         * @param {Float32Array|Array.<number>} a
	         * @param {Float32Array|Array.<number>} v
	         */
	        scale : function(out, a, v) {
	            var vx = v[0];
	            var vy = v[1];
	            out[0] = a[0] * vx;
	            out[1] = a[1] * vy;
	            out[2] = a[2] * vx;
	            out[3] = a[3] * vy;
	            out[4] = a[4] * vx;
	            out[5] = a[5] * vy;
	            return out;
	        },
	        /**
	         * 濮瑰倿鈧棛鐓╅梼锟�
	         * @param {Float32Array|Array.<number>} out
	         * @param {Float32Array|Array.<number>} a
	         */
	        invert : function(out, a) {

	            var aa = a[0];
	            var ac = a[2];
	            var atx = a[4];
	            var ab = a[1];
	            var ad = a[3];
	            var aty = a[5];

	            var det = aa * ad - ab * ac;
	            if (!det) {
	                return null;
	            }
	            det = 1.0 / det;

	            out[0] = ad * det;
	            out[1] = -ab * det;
	            out[2] = -ac * det;
	            out[3] = aa * det;
	            out[4] = (ac * aty - ad * atx) * det;
	            out[5] = (ab * atx - aa * aty) * det;
	            return out;
	        }
	    };

	    module.exports = matrix;



/***/ },
/* 18 */
/***/ function(module, exports) {

	
	    var ArrayCtor = typeof Float32Array === 'undefined'
	        ? Array
	        : Float32Array;

	    /**
	     * @typedef {Float32Array|Array.<number>} Vector2
	     */
	    /**
	     * 娴滃瞼娣崥鎴﹀櫤缁拷
	     * @exports zrender/tool/vector
	     */
	    var vector = {
	        /**
	         * 閸掓稑缂撴稉鈧稉顏勬倻闁诧拷
	         * @param {number} [x=0]
	         * @param {number} [y=0]
	         * @return {Vector2}
	         */
	        create: function (x, y) {
	            var out = new ArrayCtor(2);
	            if (x == null) {
	                x = 0;
	            }
	            if (y == null) {
	                y = 0;
	            }
	            out[0] = x;
	            out[1] = y;
	            return out;
	        },

	        /**
	         * 婢跺秴鍩楅崥鎴﹀櫤閺佺増宓�
	         * @param {Vector2} out
	         * @param {Vector2} v
	         * @return {Vector2}
	         */
	        copy: function (out, v) {
	            out[0] = v[0];
	            out[1] = v[1];
	            return out;
	        },

	        /**
	         * 閸忓娈曟稉鈧稉顏勬倻闁诧拷
	         * @param {Vector2} v
	         * @return {Vector2}
	         */
	        clone: function (v) {
	            var out = new ArrayCtor(2);
	            out[0] = v[0];
	            out[1] = v[1];
	            return out;
	        },

	        /**
	         * 鐠佸墽鐤嗛崥鎴﹀櫤閻ㄥ嫪琚辨稉顏堛€�
	         * @param {Vector2} out
	         * @param {number} a
	         * @param {number} b
	         * @return {Vector2} 缂佹挻鐏�
	         */
	        set: function (out, a, b) {
	            out[0] = a;
	            out[1] = b;
	            return out;
	        },

	        /**
	         * 閸氭垿鍣洪惄绋垮
	         * @param {Vector2} out
	         * @param {Vector2} v1
	         * @param {Vector2} v2
	         */
	        add: function (out, v1, v2) {
	            out[0] = v1[0] + v2[0];
	            out[1] = v1[1] + v2[1];
	            return out;
	        },

	        /**
	         * 閸氭垿鍣虹紓鈺傛杹閸氬海娴夐崝锟�
	         * @param {Vector2} out
	         * @param {Vector2} v1
	         * @param {Vector2} v2
	         * @param {number} a
	         */
	        scaleAndAdd: function (out, v1, v2, a) {
	            out[0] = v1[0] + v2[0] * a;
	            out[1] = v1[1] + v2[1] * a;
	            return out;
	        },

	        /**
	         * 閸氭垿鍣洪惄绋垮櫤
	         * @param {Vector2} out
	         * @param {Vector2} v1
	         * @param {Vector2} v2
	         */
	        sub: function (out, v1, v2) {
	            out[0] = v1[0] - v2[0];
	            out[1] = v1[1] - v2[1];
	            return out;
	        },

	        /**
	         * 閸氭垿鍣洪梹鍨
	         * @param {Vector2} v
	         * @return {number}
	         */
	        len: function (v) {
	            return Math.sqrt(this.lenSquare(v));
	        },

	        /**
	         * 閸氭垿鍣洪梹鍨楠炶櫕鏌�
	         * @param {Vector2} v
	         * @return {number}
	         */
	        lenSquare: function (v) {
	            return v[0] * v[0] + v[1] * v[1];
	        },

	        /**
	         * 閸氭垿鍣烘稊妯荤《
	         * @param {Vector2} out
	         * @param {Vector2} v1
	         * @param {Vector2} v2
	         */
	        mul: function (out, v1, v2) {
	            out[0] = v1[0] * v2[0];
	            out[1] = v1[1] * v2[1];
	            return out;
	        },

	        /**
	         * 閸氭垿鍣洪梽銈嗙《
	         * @param {Vector2} out
	         * @param {Vector2} v1
	         * @param {Vector2} v2
	         */
	        div: function (out, v1, v2) {
	            out[0] = v1[0] / v2[0];
	            out[1] = v1[1] / v2[1];
	            return out;
	        },

	        /**
	         * 閸氭垿鍣洪悙閫涚
	         * @param {Vector2} v1
	         * @param {Vector2} v2
	         * @return {number}
	         */
	        dot: function (v1, v2) {
	            return v1[0] * v2[0] + v1[1] * v2[1];
	        },

	        /**
	         * 閸氭垿鍣虹紓鈺傛杹
	         * @param {Vector2} out
	         * @param {Vector2} v
	         * @param {number} s
	         */
	        scale: function (out, v, s) {
	            out[0] = v[0] * s;
	            out[1] = v[1] * s;
	            return out;
	        },

	        /**
	         * 閸氭垿鍣鸿ぐ鎺嶇閸栵拷
	         * @param {Vector2} out
	         * @param {Vector2} v
	         */
	        normalize: function (out, v) {
	            var d = vector.len(v);
	            if (d === 0) {
	                out[0] = 0;
	                out[1] = 0;
	            }
	            else {
	                out[0] = v[0] / d;
	                out[1] = v[1] / d;
	            }
	            return out;
	        },

	        /**
	         * 鐠侊紕鐣婚崥鎴﹀櫤闂傜绐涚粋锟�
	         * @param {Vector2} v1
	         * @param {Vector2} v2
	         * @return {number}
	         */
	        distance: function (v1, v2) {
	            return Math.sqrt(
	                (v1[0] - v2[0]) * (v1[0] - v2[0])
	                + (v1[1] - v2[1]) * (v1[1] - v2[1])
	            );
	        },

	        /**
	         * 閸氭垿鍣虹捄婵堫瀲楠炶櫕鏌�
	         * @param {Vector2} v1
	         * @param {Vector2} v2
	         * @return {number}
	         */
	        distanceSquare: function (v1, v2) {
	            return (v1[0] - v2[0]) * (v1[0] - v2[0])
	                + (v1[1] - v2[1]) * (v1[1] - v2[1]);
	        },

	        /**
	         * 濮瑰倽绀嬮崥鎴﹀櫤
	         * @param {Vector2} out
	         * @param {Vector2} v
	         */
	        negate: function (out, v) {
	            out[0] = -v[0];
	            out[1] = -v[1];
	            return out;
	        },

	        /**
	         * 閹绘帒鈧棿琚辨稉顏嗗仯
	         * @param {Vector2} out
	         * @param {Vector2} v1
	         * @param {Vector2} v2
	         * @param {number} t
	         */
	        lerp: function (out, v1, v2, t) {
	            out[0] = v1[0] + t * (v2[0] - v1[0]);
	            out[1] = v1[1] + t * (v2[1] - v1[1]);
	            return out;
	        },

	        /**
	         * 閻晠妯€瀹革缚绠婚崥鎴﹀櫤
	         * @param {Vector2} out
	         * @param {Vector2} v
	         * @param {Vector2} m
	         */
	        applyTransform: function (out, v, m) {
	            var x = v[0];
	            var y = v[1];
	            out[0] = m[0] * x + m[2] * y + m[4];
	            out[1] = m[1] * x + m[3] * y + m[5];
	            return out;
	        },
	        /**
	         * 濮瑰倷琚辨稉顏勬倻闁插繑娓剁亸蹇撯偓锟�
	         * @param  {Vector2} out
	         * @param  {Vector2} v1
	         * @param  {Vector2} v2
	         */
	        min: function (out, v1, v2) {
	            out[0] = Math.min(v1[0], v2[0]);
	            out[1] = Math.min(v1[1], v2[1]);
	            return out;
	        },
	        /**
	         * 濮瑰倷琚辨稉顏勬倻闁插繑娓舵径褍鈧拷
	         * @param  {Vector2} out
	         * @param  {Vector2} v1
	         * @param  {Vector2} v2
	         */
	        max: function (out, v1, v2) {
	            out[0] = Math.max(v1[0], v2[0]);
	            out[1] = Math.max(v1[1], v2[1]);
	            return out;
	        }
	    };

	    vector.length = vector.len;
	    vector.lengthSquare = vector.lenSquare;
	    vector.dist = vector.distance;
	    vector.distSquare = vector.distanceSquare;

	    module.exports = vector;



/***/ },
/* 19 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	/**
	 * @module zrender/mixin/Animatable
	 */


	    var Animator = __webpack_require__(20);
	    var util = __webpack_require__(5);
	    var isString = util.isString;
	    var isFunction = util.isFunction;
	    var isObject = util.isObject;
	    var log = __webpack_require__(24);

	    /**
	     * @alias modue:zrender/mixin/Animatable
	     * @constructor
	     */
	    var Animatable = function () {

	        /**
	         * @type {Array.<module:zrender/animation/Animator>}
	         * @readOnly
	         */
	        this.animators = [];
	    };

	    Animatable.prototype = {

	        constructor: Animatable,

	        /**
	         * 閸斻劎鏁�
	         *
	         * @param {string} path 闂団偓鐟曚焦鍧婇崝鐘插З閻㈣崵娈戠仦鐐粹偓褑骞忛崣鏍熅瀵板嫸绱濋崣顖欎簰闁俺绻僡.b.c閺夈儴骞忛崣鏍ㄧ箒鐏炲倻娈戠仦鐐粹偓锟�
	         * @param {boolean} [loop] 閸斻劎鏁鹃弰顖氭儊瀵邦亞骞�
	         * @return {module:zrender/animation/Animator}
	         * @example:
	         *     el.animate('style', false)
	         *         .when(1000, {x: 10} )
	         *         .done(function(){ // Animation done })
	         *         .start()
	         */
	        animate: function (path, loop) {
	            var target;
	            var animatingShape = false;
	            var el = this;
	            var zr = this.__zr;
	            if (path) {
	                var pathSplitted = path.split('.');
	                var prop = el;
	                // If animating shape
	                animatingShape = pathSplitted[0] === 'shape';
	                for (var i = 0, l = pathSplitted.length; i < l; i++) {
	                    if (!prop) {
	                        continue;
	                    }
	                    prop = prop[pathSplitted[i]];
	                }
	                if (prop) {
	                    target = prop;
	                }
	            }
	            else {
	                target = el;
	            }

	            if (!target) {
	                log(
	                    'Property "'
	                    + path
	                    + '" is not existed in element '
	                    + el.id
	                );
	                return;
	            }

	            var animators = el.animators;

	            var animator = new Animator(target, loop);

	            animator.during(function (target) {
	                el.dirty(animatingShape);
	            })
	            .done(function () {
	                // FIXME Animator will not be removed if use `Animator#stop` to stop animation
	                animators.splice(util.indexOf(animators, animator), 1);
	            });

	            animators.push(animator);

	            // If animate after added to the zrender
	            if (zr) {
	                zr.animation.addAnimator(animator);
	            }

	            return animator;
	        },

	        /**
	         * 閸嬫粍顒涢崝銊ф暰
	         * @param {boolean} forwardToLast If move to last frame before stop
	         */
	        stopAnimation: function (forwardToLast) {
	            var animators = this.animators;
	            var len = animators.length;
	            for (var i = 0; i < len; i++) {
	                animators[i].stop(forwardToLast);
	            }
	            animators.length = 0;

	            return this;
	        },

	        /**
	         * @param {Object} target
	         * @param {number} [time=500] Time in ms
	         * @param {string} [easing='linear']
	         * @param {number} [delay=0]
	         * @param {Function} [callback]
	         *
	         * @example
	         *  // Animate position
	         *  el.animateTo({
	         *      position: [10, 10]
	         *  }, function () { // done })
	         *
	         *  // Animate shape, style and position in 100ms, delayed 100ms, with cubicOut easing
	         *  el.animateTo({
	         *      shape: {
	         *          width: 500
	         *      },
	         *      style: {
	         *          fill: 'red'
	         *      }
	         *      position: [10, 10]
	         *  }, 100, 100, 'cubicOut', function () { // done })
	         */
	         // TODO Return animation key
	        animateTo: function (target, time, delay, easing, callback) {
	            // animateTo(target, time, easing, callback);
	            if (isString(delay)) {
	                callback = easing;
	                easing = delay;
	                delay = 0;
	            }
	            // animateTo(target, time, delay, callback);
	            else if (isFunction(easing)) {
	                callback = easing;
	                easing = 'linear';
	                delay = 0;
	            }
	            // animateTo(target, time, callback);
	            else if (isFunction(delay)) {
	                callback = delay;
	                delay = 0;
	            }
	            // animateTo(target, callback)
	            else if (isFunction(time)) {
	                callback = time;
	                time = 500;
	            }
	            // animateTo(target)
	            else if (!time) {
	                time = 500;
	            }
	            // Stop all previous animations
	            this.stopAnimation();
	            this._animateToShallow('', this, target, time, delay, easing, callback);

	            // Animators may be removed immediately after start
	            // if there is nothing to animate
	            var animators = this.animators.slice();
	            var count = animators.length;
	            function done() {
	                count--;
	                if (!count) {
	                    callback && callback();
	                }
	            }

	            // No animators. This should be checked before animators[i].start(),
	            // because 'done' may be executed immediately if no need to animate.
	            if (!count) {
	                callback && callback();
	            }
	            // Start after all animators created
	            // Incase any animator is done immediately when all animation properties are not changed
	            for (var i = 0; i < animators.length; i++) {
	                animators[i]
	                    .done(done)
	                    .start(easing);
	            }
	        },

	        /**
	         * @private
	         * @param {string} path=''
	         * @param {Object} source=this
	         * @param {Object} target
	         * @param {number} [time=500]
	         * @param {number} [delay=0]
	         *
	         * @example
	         *  // Animate position
	         *  el._animateToShallow({
	         *      position: [10, 10]
	         *  })
	         *
	         *  // Animate shape, style and position in 100ms, delayed 100ms
	         *  el._animateToShallow({
	         *      shape: {
	         *          width: 500
	         *      },
	         *      style: {
	         *          fill: 'red'
	         *      }
	         *      position: [10, 10]
	         *  }, 100, 100)
	         */
	        _animateToShallow: function (path, source, target, time, delay) {
	            var objShallow = {};
	            var propertyCount = 0;
	            for (var name in target) {
	                if (!target.hasOwnProperty(name)) {
	                    continue;
	                }

	                if (source[name] != null) {
	                    if (isObject(target[name]) && !util.isArrayLike(target[name])) {
	                        this._animateToShallow(
	                            path ? path + '.' + name : name,
	                            source[name],
	                            target[name],
	                            time,
	                            delay
	                        );
	                    }
	                    else {
	                        objShallow[name] = target[name];
	                        propertyCount++;
	                    }
	                }
	                else if (target[name] != null) {
	                    // Attr directly if not has property
	                    // FIXME, if some property not needed for element ?
	                    if (!path) {
	                        this.attr(name, target[name]);
	                    }
	                    else {  // Shape or style
	                        var props = {};
	                        props[path] = {};
	                        props[path][name] = target[name];
	                        this.attr(props);
	                    }
	                }
	            }

	            if (propertyCount > 0) {
	                this.animate(path, false)
	                    .when(time == null ? 500 : time, objShallow)
	                    .delay(delay || 0);
	            }

	            return this;
	        }
	    };

	    module.exports = Animatable;


/***/ },
/* 20 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * @module echarts/animation/Animator
	 */


	    var Clip = __webpack_require__(21);
	    var color = __webpack_require__(23);
	    var util = __webpack_require__(5);
	    var isArrayLike = util.isArrayLike;

	    var arraySlice = Array.prototype.slice;

	    function defaultGetter(target, key) {
	        return target[key];
	    }

	    function defaultSetter(target, key, value) {
	        target[key] = value;
	    }

	    /**
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} percent
	     * @return {number}
	     */
	    function interpolateNumber(p0, p1, percent) {
	        return (p1 - p0) * percent + p0;
	    }

	    /**
	     * @param  {string} p0
	     * @param  {string} p1
	     * @param  {number} percent
	     * @return {string}
	     */
	    function interpolateString(p0, p1, percent) {
	        return percent > 0.5 ? p1 : p0;
	    }

	    /**
	     * @param  {Array} p0
	     * @param  {Array} p1
	     * @param  {number} percent
	     * @param  {Array} out
	     * @param  {number} arrDim
	     */
	    function interpolateArray(p0, p1, percent, out, arrDim) {
	        var len = p0.length;
	        if (arrDim == 1) {
	            for (var i = 0; i < len; i++) {
	                out[i] = interpolateNumber(p0[i], p1[i], percent);
	            }
	        }
	        else {
	            var len2 = p0[0].length;
	            for (var i = 0; i < len; i++) {
	                for (var j = 0; j < len2; j++) {
	                    out[i][j] = interpolateNumber(
	                        p0[i][j], p1[i][j], percent
	                    );
	                }
	            }
	        }
	    }

	    // arr0 is source array, arr1 is target array.
	    // Do some preprocess to avoid error happened when interpolating from arr0 to arr1
	    function fillArr(arr0, arr1, arrDim) {
	        var arr0Len = arr0.length;
	        var arr1Len = arr1.length;
	        if (arr0Len !== arr1Len) {
	            // FIXME Not work for TypedArray
	            var isPreviousLarger = arr0Len > arr1Len;
	            if (isPreviousLarger) {
	                // Cut the previous
	                arr0.length = arr1Len;
	            }
	            else {
	                // Fill the previous
	                for (var i = arr0Len; i < arr1Len; i++) {
	                    arr0.push(
	                        arrDim === 1 ? arr1[i] : arraySlice.call(arr1[i])
	                    );
	                }
	            }
	        }
	        // Handling NaN value
	        var len2 = arr0[0] && arr0[0].length;
	        for (var i = 0; i < arr0.length; i++) {
	            if (arrDim === 1) {
	                if (isNaN(arr0[i])) {
	                    arr0[i] = arr1[i];
	                }
	            }
	            else {
	                for (var j = 0; j < len2; j++) {
	                    if (isNaN(arr0[i][j])) {
	                        arr0[i][j] = arr1[i][j];
	                    }
	                }
	            }
	        }
	    }

	    /**
	     * @param  {Array} arr0
	     * @param  {Array} arr1
	     * @param  {number} arrDim
	     * @return {boolean}
	     */
	    function isArraySame(arr0, arr1, arrDim) {
	        if (arr0 === arr1) {
	            return true;
	        }
	        var len = arr0.length;
	        if (len !== arr1.length) {
	            return false;
	        }
	        if (arrDim === 1) {
	            for (var i = 0; i < len; i++) {
	                if (arr0[i] !== arr1[i]) {
	                    return false;
	                }
	            }
	        }
	        else {
	            var len2 = arr0[0].length;
	            for (var i = 0; i < len; i++) {
	                for (var j = 0; j < len2; j++) {
	                    if (arr0[i][j] !== arr1[i][j]) {
	                        return false;
	                    }
	                }
	            }
	        }
	        return true;
	    }

	    /**
	     * Catmull Rom interpolate array
	     * @param  {Array} p0
	     * @param  {Array} p1
	     * @param  {Array} p2
	     * @param  {Array} p3
	     * @param  {number} t
	     * @param  {number} t2
	     * @param  {number} t3
	     * @param  {Array} out
	     * @param  {number} arrDim
	     */
	    function catmullRomInterpolateArray(
	        p0, p1, p2, p3, t, t2, t3, out, arrDim
	    ) {
	        var len = p0.length;
	        if (arrDim == 1) {
	            for (var i = 0; i < len; i++) {
	                out[i] = catmullRomInterpolate(
	                    p0[i], p1[i], p2[i], p3[i], t, t2, t3
	                );
	            }
	        }
	        else {
	            var len2 = p0[0].length;
	            for (var i = 0; i < len; i++) {
	                for (var j = 0; j < len2; j++) {
	                    out[i][j] = catmullRomInterpolate(
	                        p0[i][j], p1[i][j], p2[i][j], p3[i][j],
	                        t, t2, t3
	                    );
	                }
	            }
	        }
	    }

	    /**
	     * Catmull Rom interpolate number
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @param  {number} p3
	     * @param  {number} t
	     * @param  {number} t2
	     * @param  {number} t3
	     * @return {number}
	     */
	    function catmullRomInterpolate(p0, p1, p2, p3, t, t2, t3) {
	        var v0 = (p2 - p0) * 0.5;
	        var v1 = (p3 - p1) * 0.5;
	        return (2 * (p1 - p2) + v0 + v1) * t3
	                + (-3 * (p1 - p2) - 2 * v0 - v1) * t2
	                + v0 * t + p1;
	    }

	    function cloneValue(value) {
	        if (isArrayLike(value)) {
	            var len = value.length;
	            if (isArrayLike(value[0])) {
	                var ret = [];
	                for (var i = 0; i < len; i++) {
	                    ret.push(arraySlice.call(value[i]));
	                }
	                return ret;
	            }

	            return arraySlice.call(value);
	        }

	        return value;
	    }

	    function rgba2String(rgba) {
	        rgba[0] = Math.floor(rgba[0]);
	        rgba[1] = Math.floor(rgba[1]);
	        rgba[2] = Math.floor(rgba[2]);

	        return 'rgba(' + rgba.join(',') + ')';
	    }

	    function createTrackClip (animator, easing, oneTrackDone, keyframes, propName) {
	        var getter = animator._getter;
	        var setter = animator._setter;
	        var useSpline = easing === 'spline';

	        var trackLen = keyframes.length;
	        if (!trackLen) {
	            return;
	        }
	        // Guess data type
	        var firstVal = keyframes[0].value;
	        var isValueArray = isArrayLike(firstVal);
	        var isValueColor = false;
	        var isValueString = false;

	        // For vertices morphing
	        var arrDim = (
	                isValueArray
	                && isArrayLike(firstVal[0])
	            )
	            ? 2 : 1;
	        var trackMaxTime;
	        // Sort keyframe as ascending
	        keyframes.sort(function(a, b) {
	            return a.time - b.time;
	        });

	        trackMaxTime = keyframes[trackLen - 1].time;
	        // Percents of each keyframe
	        var kfPercents = [];
	        // Value of each keyframe
	        var kfValues = [];
	        var prevValue = keyframes[0].value;
	        var isAllValueEqual = true;
	        for (var i = 0; i < trackLen; i++) {
	            kfPercents.push(keyframes[i].time / trackMaxTime);
	            // Assume value is a color when it is a string
	            var value = keyframes[i].value;

	            // Check if value is equal, deep check if value is array
	            if (!((isValueArray && isArraySame(value, prevValue, arrDim))
	                || (!isValueArray && value === prevValue))) {
	                isAllValueEqual = false;
	            }
	            prevValue = value;

	            // Try converting a string to a color array
	            if (typeof value == 'string') {
	                var colorArray = color.parse(value);
	                if (colorArray) {
	                    value = colorArray;
	                    isValueColor = true;
	                }
	                else {
	                    isValueString = true;
	                }
	            }
	            kfValues.push(value);
	        }
	        if (isAllValueEqual) {
	            return;
	        }

	        var lastValue = kfValues[trackLen - 1];
	        // Polyfill array and NaN value
	        for (var i = 0; i < trackLen - 1; i++) {
	            if (isValueArray) {
	                fillArr(kfValues[i], lastValue, arrDim);
	            }
	            else {
	                if (isNaN(kfValues[i]) && !isNaN(lastValue) && !isValueString && !isValueColor) {
	                    kfValues[i] = lastValue;
	                }
	            }
	        }
	        isValueArray && fillArr(getter(animator._target, propName), lastValue, arrDim);

	        // Cache the key of last frame to speed up when
	        // animation playback is sequency
	        var lastFrame = 0;
	        var lastFramePercent = 0;
	        var start;
	        var w;
	        var p0;
	        var p1;
	        var p2;
	        var p3;

	        if (isValueColor) {
	            var rgba = [0, 0, 0, 0];
	        }

	        var onframe = function (target, percent) {
	            // Find the range keyframes
	            // kf1-----kf2---------current--------kf3
	            // find kf2 and kf3 and do interpolation
	            var frame;
	            // In the easing function like elasticOut, percent may less than 0
	            if (percent < 0) {
	                frame = 0;
	            }
	            else if (percent < lastFramePercent) {
	                // Start from next key
	                // PENDING start from lastFrame ?
	                start = Math.min(lastFrame + 1, trackLen - 1);
	                for (frame = start; frame >= 0; frame--) {
	                    if (kfPercents[frame] <= percent) {
	                        break;
	                    }
	                }
	                // PENDING really need to do this ?
	                frame = Math.min(frame, trackLen - 2);
	            }
	            else {
	                for (frame = lastFrame; frame < trackLen; frame++) {
	                    if (kfPercents[frame] > percent) {
	                        break;
	                    }
	                }
	                frame = Math.min(frame - 1, trackLen - 2);
	            }
	            lastFrame = frame;
	            lastFramePercent = percent;

	            var range = (kfPercents[frame + 1] - kfPercents[frame]);
	            if (range === 0) {
	                return;
	            }
	            else {
	                w = (percent - kfPercents[frame]) / range;
	            }
	            if (useSpline) {
	                p1 = kfValues[frame];
	                p0 = kfValues[frame === 0 ? frame : frame - 1];
	                p2 = kfValues[frame > trackLen - 2 ? trackLen - 1 : frame + 1];
	                p3 = kfValues[frame > trackLen - 3 ? trackLen - 1 : frame + 2];
	                if (isValueArray) {
	                    catmullRomInterpolateArray(
	                        p0, p1, p2, p3, w, w * w, w * w * w,
	                        getter(target, propName),
	                        arrDim
	                    );
	                }
	                else {
	                    var value;
	                    if (isValueColor) {
	                        value = catmullRomInterpolateArray(
	                            p0, p1, p2, p3, w, w * w, w * w * w,
	                            rgba, 1
	                        );
	                        value = rgba2String(rgba);
	                    }
	                    else if (isValueString) {
	                        // String is step(0.5)
	                        return interpolateString(p1, p2, w);
	                    }
	                    else {
	                        value = catmullRomInterpolate(
	                            p0, p1, p2, p3, w, w * w, w * w * w
	                        );
	                    }
	                    setter(
	                        target,
	                        propName,
	                        value
	                    );
	                }
	            }
	            else {
	                if (isValueArray) {
	                    interpolateArray(
	                        kfValues[frame], kfValues[frame + 1], w,
	                        getter(target, propName),
	                        arrDim
	                    );
	                }
	                else {
	                    var value;
	                    if (isValueColor) {
	                        interpolateArray(
	                            kfValues[frame], kfValues[frame + 1], w,
	                            rgba, 1
	                        );
	                        value = rgba2String(rgba);
	                    }
	                    else if (isValueString) {
	                        // String is step(0.5)
	                        return interpolateString(kfValues[frame], kfValues[frame + 1], w);
	                    }
	                    else {
	                        value = interpolateNumber(kfValues[frame], kfValues[frame + 1], w);
	                    }
	                    setter(
	                        target,
	                        propName,
	                        value
	                    );
	                }
	            }
	        };

	        var clip = new Clip({
	            target: animator._target,
	            life: trackMaxTime,
	            loop: animator._loop,
	            delay: animator._delay,
	            onframe: onframe,
	            ondestroy: oneTrackDone
	        });

	        if (easing && easing !== 'spline') {
	            clip.easing = easing;
	        }

	        return clip;
	    }

	    /**
	     * @alias module:zrender/animation/Animator
	     * @constructor
	     * @param {Object} target
	     * @param {boolean} loop
	     * @param {Function} getter
	     * @param {Function} setter
	     */
	    var Animator = function(target, loop, getter, setter) {
	        this._tracks = {};
	        this._target = target;

	        this._loop = loop || false;

	        this._getter = getter || defaultGetter;
	        this._setter = setter || defaultSetter;

	        this._clipCount = 0;

	        this._delay = 0;

	        this._doneList = [];

	        this._onframeList = [];

	        this._clipList = [];
	    };

	    Animator.prototype = {
	        /**
	         * ç’å‰§ç–†é”ã„§æ•¾éæŠ½æ•­ç”¯ï¿½
	         * @param  {number} time éæŠ½æ•­ç”¯Ñ„æ¤‚é—‚è¾¾ç´é—æ›šç¶…é„ç—¬s
	         * @param  {Object} props éæŠ½æ•­ç”¯Ñ…æ®‘çžç‚´â‚¬Ñƒâ‚¬ç¡·ç´key-valueç›ã„§ãš
	         * @return {module:zrender/animation/Animator}
	         */
	        when: function(time /* ms */, props) {
	            var tracks = this._tracks;
	            for (var propName in props) {
	                if (!props.hasOwnProperty(propName)) {
	                    continue;
	                }

	                if (!tracks[propName]) {
	                    tracks[propName] = [];
	                    // Invalid value
	                    var value = this._getter(this._target, propName);
	                    if (value == null) {
	                        // zrLog('Invalid property ' + propName);
	                        continue;
	                    }
	                    // If time is 0
	                    //  Then props is given initialize value
	                    // Else
	                    //  Initialize value from current prop value
	                    if (time !== 0) {
	                        tracks[propName].push({
	                            time: 0,
	                            value: cloneValue(value)
	                        });
	                    }
	                }
	                tracks[propName].push({
	                    time: time,
	                    value: props[propName]
	                });
	            }
	            return this;
	        },
	        /**
	         * å¨£è¯²å§žé”ã„§æ•¾å§£å¿Žç«´ç”¯Ñ…æ®‘é¥ç‚¶çšŸé‘èŠ¥æšŸ
	         * @param  {Function} callback
	         * @return {module:zrender/animation/Animator}
	         */
	        during: function (callback) {
	            this._onframeList.push(callback);
	            return this;
	        },

	        _doneCallback: function () {
	            // Clear all tracks
	            this._tracks = {};
	            // Clear all clips
	            this._clipList.length = 0;

	            var doneList = this._doneList;
	            var len = doneList.length;
	            for (var i = 0; i < len; i++) {
	                doneList[i].call(this);
	            }
	        },
	        /**
	         * å¯®â‚¬æ¿®å¬«å¢½ç›å±½å§©é¢ï¿½
	         * @param  {string|Function} easing
	         *         é”ã„§æ•¾ç¼‚æ’³å§©é‘èŠ¥æšŸé”›å²ƒî‡›ç‘™äº„@link module:zrender/animation/easing}
	         * @return {module:zrender/animation/Animator}
	         */
	        start: function (easing) {

	            var self = this;
	            var clipCount = 0;

	            var oneTrackDone = function() {
	                clipCount--;
	                if (!clipCount) {
	                    self._doneCallback();
	                }
	            };

	            var lastClip;
	            for (var propName in this._tracks) {
	                if (!this._tracks.hasOwnProperty(propName)) {
	                    continue;
	                }
	                var clip = createTrackClip(
	                    this, easing, oneTrackDone,
	                    this._tracks[propName], propName
	                );
	                if (clip) {
	                    this._clipList.push(clip);
	                    clipCount++;

	                    // If start after added to animation
	                    if (this.animation) {
	                        this.animation.addClip(clip);
	                    }

	                    lastClip = clip;
	                }
	            }

	            // Add during callback on the last clip
	            if (lastClip) {
	                var oldOnFrame = lastClip.onframe;
	                lastClip.onframe = function (target, percent) {
	                    oldOnFrame(target, percent);

	                    for (var i = 0; i < self._onframeList.length; i++) {
	                        self._onframeList[i](target, percent);
	                    }
	                };
	            }

	            if (!clipCount) {
	                this._doneCallback();
	            }
	            return this;
	        },
	        /**
	         * é‹æ»„î„›é”ã„§æ•¾
	         * @param {boolean} forwardToLast If move to last frame before stop
	         */
	        stop: function (forwardToLast) {
	            var clipList = this._clipList;
	            var animation = this.animation;
	            for (var i = 0; i < clipList.length; i++) {
	                var clip = clipList[i];
	                if (forwardToLast) {
	                    // Move to last frame before stop
	                    clip.onframe(this._target, 1);
	                }
	                animation && animation.removeClip(clip);
	            }
	            clipList.length = 0;
	        },
	        /**
	         * ç’å‰§ç–†é”ã„§æ•¾å¯¤æƒ°ç¹œå¯®â‚¬æ¿®å¬¬æ®‘éƒå •æ£¿
	         * @param  {number} time é—æ›šç¶…ms
	         * @return {module:zrender/animation/Animator}
	         */
	        delay: function (time) {
	            this._delay = time;
	            return this;
	        },
	        /**
	         * å¨£è¯²å§žé”ã„§æ•¾ç¼æ’´æ½«é¨å‹«æ´–ç’‹ï¿½
	         * @param  {Function} cb
	         * @return {module:zrender/animation/Animator}
	         */
	        done: function(cb) {
	            if (cb) {
	                this._doneList.push(cb);
	            }
	            return this;
	        },

	        /**
	         * @return {Array.<module:zrender/animation/Clip>}
	         */
	        getClips: function () {
	            return this._clipList;
	        }
	    };

	    module.exports = Animator;


/***/ },
/* 21 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * é”ã„§æ•¾æ¶“ç»˜å¸¶é’è·ºæ«’
	 * @config target é”ã„§æ•¾ç€µç¡…è–„é”›å±½å½²æµ ãƒ¦æ§¸éæ‰®ç²é”›å±½î›§é‹æ»„æ§¸éæ‰®ç²é¨å‹®ç˜½æµ¼æ°­å£’é–²å¿“åžŽé™æ†ƒnframeç»›å¤‰ç°¨æµ ï¿½
	 * @config life(1000) é”ã„§æ•¾éƒå •æš±
	 * @config delay(0) é”ã„§æ•¾å¯¤æƒ°ç¹œéƒå •æ£¿
	 * @config loop(true)
	 * @config gap(0) å¯°î†å¹†é¨å‹¯æ£¿é—…æ—€æ¤‚é—‚ï¿½
	 * @config onframe
	 * @config easing(optional)
	 * @config ondestroy(optional)
	 * @config onrestart(optional)
	 *
	 * TODO pause
	 */


	    var easingFuncs = __webpack_require__(22);

	    function Clip(options) {

	        this._target = options.target;

	        // é¢ç†·æ‡¡é›ã„¦æ¹¡
	        this._life = options.life || 1000;
	        // å¯¤èˆµæ¤‚
	        this._delay = options.delay || 0;
	        // å¯®â‚¬æ¿®å¬«æ¤‚é—‚ï¿½
	        // this._startTime = new Date().getTime() + this._delay;// é—æ›šç¶…å§£î‚¤î—
	        this._initialized = false;

	        // é„îˆšæƒå¯°î†å¹†
	        this.loop = options.loop == null ? false : options.loop;

	        this.gap = options.gap || 0;

	        this.easing = options.easing || 'Linear';

	        this.onframe = options.onframe;
	        this.ondestroy = options.ondestroy;
	        this.onrestart = options.onrestart;
	    }

	    Clip.prototype = {

	        constructor: Clip,

	        step: function (globalTime) {
	            // Set startTime on first step, or _startTime may has milleseconds different between clips
	            // PENDING
	            if (!this._initialized) {
	                this._startTime = globalTime + this._delay;
	                this._initialized = true;
	            }

	            var percent = (globalTime - this._startTime) / this._life;

	            // æ©æ¨»ç—…å¯®â‚¬æ¿®ï¿½
	            if (percent < 0) {
	                return;
	            }

	            percent = Math.min(percent, 1);

	            var easing = this.easing;
	            var easingFunc = typeof easing == 'string' ? easingFuncs[easing] : easing;
	            var schedule = typeof easingFunc === 'function'
	                ? easingFunc(percent)
	                : percent;

	            this.fire('frame', schedule);

	            // ç¼æ’´æ½«
	            if (percent == 1) {
	                if (this.loop) {
	                    this.restart (globalTime);
	                    // é–²å¶†æŸŠå¯®â‚¬æ¿®å¬ªæ‡†éˆï¿½
	                    // éŽ¶æ¶˜åš­é‘°å±¼ç¬‰é„îˆœæ´¿éŽºãƒ¨çšŸé¢ã„¤ç°¨æµ å‰æ´¿é’ï¿½ stage.update éšåº¡å•€ç¼ç†¶ç«´ç’‹å†ªæ•¤æ©æ¬Žç°ºæµœå¬©æ¬¢
	                    return 'restart';
	                }

	                // é”ã„§æ•¾ç€¹å±¾åžšçå—šç¹–æ¶“î…å¸¶é’è·ºæ«’éå›ªç˜‘æ¶“å“„ç·Ÿé’çŠ»æ«Ž
	                // é¦Ë‹nimation.updateæ¶“î…¡ç¹˜ç›å±¾å£’é–²å¿“åž¹é—„ï¿½
	                this._needsRemove = true;
	                return 'destroy';
	            }

	            return null;
	        },

	        restart: function (globalTime) {
	            var remainder = (globalTime - this._startTime) % this._life;
	            this._startTime = globalTime - remainder + this.gap;

	            this._needsRemove = false;
	        },

	        fire: function(eventType, arg) {
	            eventType = 'on' + eventType;
	            if (this[eventType]) {
	                this[eventType](this._target, arg);
	            }
	        }
	    };

	    module.exports = Clip;



/***/ },
/* 22 */
/***/ function(module, exports) {

	/**
	 * ç¼‚æ’³å§©æµ ï½‡çˆœé‰ãƒ¨åšœ https://github.com/sole/tween.js/blob/master/src/Tween.js
	 * @see http://sole.github.io/tween.js/examples/03_graphs.html
	 * @exports zrender/animation/easing
	 */

	    var easing = {
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        linear: function (k) {
	            return k;
	        },

	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        quadraticIn: function (k) {
	            return k * k;
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        quadraticOut: function (k) {
	            return k * (2 - k);
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        quadraticInOut: function (k) {
	            if ((k *= 2) < 1) {
	                return 0.5 * k * k;
	            }
	            return -0.5 * (--k * (k - 2) - 1);
	        },

	        // æ¶“å¤‹î‚¼é‚åœ­æ®‘ç¼‚æ’³å§©é”›å±^3é”›ï¿½
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        cubicIn: function (k) {
	            return k * k * k;
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        cubicOut: function (k) {
	            return --k * k * k + 1;
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        cubicInOut: function (k) {
	            if ((k *= 2) < 1) {
	                return 0.5 * k * k * k;
	            }
	            return 0.5 * ((k -= 2) * k * k + 2);
	        },

	        // é¥æ¶™î‚¼é‚åœ­æ®‘ç¼‚æ’³å§©é”›å±^4é”›ï¿½
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        quarticIn: function (k) {
	            return k * k * k * k;
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        quarticOut: function (k) {
	            return 1 - (--k * k * k * k);
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        quarticInOut: function (k) {
	            if ((k *= 2) < 1) {
	                return 0.5 * k * k * k * k;
	            }
	            return -0.5 * ((k -= 2) * k * k * k - 2);
	        },

	        // æµœæ—€î‚¼é‚åœ­æ®‘ç¼‚æ’³å§©é”›å±^5é”›ï¿½
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        quinticIn: function (k) {
	            return k * k * k * k * k;
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        quinticOut: function (k) {
	            return --k * k * k * k * k + 1;
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        quinticInOut: function (k) {
	            if ((k *= 2) < 1) {
	                return 0.5 * k * k * k * k * k;
	            }
	            return 0.5 * ((k -= 2) * k * k * k * k + 2);
	        },

	        // å§ï½…é¸¡é‡èŒ¬åšŽé¨å‹­ç´¦é”îŸ’ç´™sin(t)é”›ï¿½
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        sinusoidalIn: function (k) {
	            return 1 - Math.cos(k * Math.PI / 2);
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        sinusoidalOut: function (k) {
	            return Math.sin(k * Math.PI / 2);
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        sinusoidalInOut: function (k) {
	            return 0.5 * (1 - Math.cos(Math.PI * k));
	        },

	        // éŽ¸å›¨æšŸé‡èŒ¬åšŽé¨å‹­ç´¦é”îŸ’ç´™2^té”›ï¿½
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        exponentialIn: function (k) {
	            return k === 0 ? 0 : Math.pow(1024, k - 1);
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        exponentialOut: function (k) {
	            return k === 1 ? 1 : 1 - Math.pow(2, -10 * k);
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        exponentialInOut: function (k) {
	            if (k === 0) {
	                return 0;
	            }
	            if (k === 1) {
	                return 1;
	            }
	            if ((k *= 2) < 1) {
	                return 0.5 * Math.pow(1024, k - 1);
	            }
	            return 0.5 * (-Math.pow(2, -10 * (k - 1)) + 2);
	        },

	        // é¦å——èˆ°é‡èŒ¬åšŽé¨å‹­ç´¦é”îŸ’ç´™sqrt(1-t^2)é”›ï¿½
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        circularIn: function (k) {
	            return 1 - Math.sqrt(1 - k * k);
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        circularOut: function (k) {
	            return Math.sqrt(1 - (--k * k));
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        circularInOut: function (k) {
	            if ((k *= 2) < 1) {
	                return -0.5 * (Math.sqrt(1 - k * k) - 1);
	            }
	            return 0.5 * (Math.sqrt(1 - (k -= 2) * k) + 1);
	        },

	        // é’æ¶˜ç¼“ç»«è®³æŠ€æµœåº¡è„Šç»¨Ñƒæ¹ªé‹æ»„î„›é“å¶†æ½µé¥ç‚´å°Ÿé‘½ï¼„æ®‘é”ã„§æ•¾
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        elasticIn: function (k) {
	            var s;
	            var a = 0.1;
	            var p = 0.4;
	            if (k === 0) {
	                return 0;
	            }
	            if (k === 1) {
	                return 1;
	            }
	            if (!a || a < 1) {
	                a = 1; s = p / 4;
	            }
	            else {
	                s = p * Math.asin(1 / a) / (2 * Math.PI);
	            }
	            return -(a * Math.pow(2, 10 * (k -= 1)) *
	                        Math.sin((k - s) * (2 * Math.PI) / p));
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        elasticOut: function (k) {
	            var s;
	            var a = 0.1;
	            var p = 0.4;
	            if (k === 0) {
	                return 0;
	            }
	            if (k === 1) {
	                return 1;
	            }
	            if (!a || a < 1) {
	                a = 1; s = p / 4;
	            }
	            else {
	                s = p * Math.asin(1 / a) / (2 * Math.PI);
	            }
	            return (a * Math.pow(2, -10 * k) *
	                    Math.sin((k - s) * (2 * Math.PI) / p) + 1);
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        elasticInOut: function (k) {
	            var s;
	            var a = 0.1;
	            var p = 0.4;
	            if (k === 0) {
	                return 0;
	            }
	            if (k === 1) {
	                return 1;
	            }
	            if (!a || a < 1) {
	                a = 1; s = p / 4;
	            }
	            else {
	                s = p * Math.asin(1 / a) / (2 * Math.PI);
	            }
	            if ((k *= 2) < 1) {
	                return -0.5 * (a * Math.pow(2, 10 * (k -= 1))
	                    * Math.sin((k - s) * (2 * Math.PI) / p));
	            }
	            return a * Math.pow(2, -10 * (k -= 1))
	                    * Math.sin((k - s) * (2 * Math.PI) / p) * 0.5 + 1;

	        },

	        // é¦ã„¦ç…‡æ¶“â‚¬é”ã„§æ•¾å¯®â‚¬æ¿®å¬«éƒ¨éŽ¸å›©ãšé¨å‹®çŸ¾å¯°å‹®ç¹˜ç›å±½å§©é¢è¯²î˜©éžå——å¢ ç»‹å¶‡â—¢é€è·ºæ´–ç’‡ãƒ¥å§©é¢è¤æ®‘ç»‰è¯²å§©
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        backIn: function (k) {
	            var s = 1.70158;
	            return k * k * ((s + 1) * k - s);
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        backOut: function (k) {
	            var s = 1.70158;
	            return --k * k * ((s + 1) * k + s) + 1;
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        backInOut: function (k) {
	            var s = 1.70158 * 1.525;
	            if ((k *= 2) < 1) {
	                return 0.5 * (k * k * ((s + 1) * k - s));
	            }
	            return 0.5 * ((k -= 2) * k * ((s + 1) * k + s) + 2);
	        },

	        // é’æ¶˜ç¼“å¯®ç¡…çƒ¦éå Ÿç‰
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        bounceIn: function (k) {
	            return 1 - easing.bounceOut(1 - k);
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        bounceOut: function (k) {
	            if (k < (1 / 2.75)) {
	                return 7.5625 * k * k;
	            }
	            else if (k < (2 / 2.75)) {
	                return 7.5625 * (k -= (1.5 / 2.75)) * k + 0.75;
	            }
	            else if (k < (2.5 / 2.75)) {
	                return 7.5625 * (k -= (2.25 / 2.75)) * k + 0.9375;
	            }
	            else {
	                return 7.5625 * (k -= (2.625 / 2.75)) * k + 0.984375;
	            }
	        },
	        /**
	        * @param {number} k
	        * @return {number}
	        */
	        bounceInOut: function (k) {
	            if (k < 0.5) {
	                return easing.bounceIn(k * 2) * 0.5;
	            }
	            return easing.bounceOut(k * 2 - 1) * 0.5 + 0.5;
	        }
	    };

	    module.exports = easing;




/***/ },
/* 23 */
/***/ function(module, exports) {

	/**
	 * @module zrender/tool/color
	 */


	    var kCSSColorTable = {
	        'transparent': [0,0,0,0], 'aliceblue': [240,248,255,1],
	        'antiquewhite': [250,235,215,1], 'aqua': [0,255,255,1],
	        'aquamarine': [127,255,212,1], 'azure': [240,255,255,1],
	        'beige': [245,245,220,1], 'bisque': [255,228,196,1],
	        'black': [0,0,0,1], 'blanchedalmond': [255,235,205,1],
	        'blue': [0,0,255,1], 'blueviolet': [138,43,226,1],
	        'brown': [165,42,42,1], 'burlywood': [222,184,135,1],
	        'cadetblue': [95,158,160,1], 'chartreuse': [127,255,0,1],
	        'chocolate': [210,105,30,1], 'coral': [255,127,80,1],
	        'cornflowerblue': [100,149,237,1], 'cornsilk': [255,248,220,1],
	        'crimson': [220,20,60,1], 'cyan': [0,255,255,1],
	        'darkblue': [0,0,139,1], 'darkcyan': [0,139,139,1],
	        'darkgoldenrod': [184,134,11,1], 'darkgray': [169,169,169,1],
	        'darkgreen': [0,100,0,1], 'darkgrey': [169,169,169,1],
	        'darkkhaki': [189,183,107,1], 'darkmagenta': [139,0,139,1],
	        'darkolivegreen': [85,107,47,1], 'darkorange': [255,140,0,1],
	        'darkorchid': [153,50,204,1], 'darkred': [139,0,0,1],
	        'darksalmon': [233,150,122,1], 'darkseagreen': [143,188,143,1],
	        'darkslateblue': [72,61,139,1], 'darkslategray': [47,79,79,1],
	        'darkslategrey': [47,79,79,1], 'darkturquoise': [0,206,209,1],
	        'darkviolet': [148,0,211,1], 'deeppink': [255,20,147,1],
	        'deepskyblue': [0,191,255,1], 'dimgray': [105,105,105,1],
	        'dimgrey': [105,105,105,1], 'dodgerblue': [30,144,255,1],
	        'firebrick': [178,34,34,1], 'floralwhite': [255,250,240,1],
	        'forestgreen': [34,139,34,1], 'fuchsia': [255,0,255,1],
	        'gainsboro': [220,220,220,1], 'ghostwhite': [248,248,255,1],
	        'gold': [255,215,0,1], 'goldenrod': [218,165,32,1],
	        'gray': [128,128,128,1], 'green': [0,128,0,1],
	        'greenyellow': [173,255,47,1], 'grey': [128,128,128,1],
	        'honeydew': [240,255,240,1], 'hotpink': [255,105,180,1],
	        'indianred': [205,92,92,1], 'indigo': [75,0,130,1],
	        'ivory': [255,255,240,1], 'khaki': [240,230,140,1],
	        'lavender': [230,230,250,1], 'lavenderblush': [255,240,245,1],
	        'lawngreen': [124,252,0,1], 'lemonchiffon': [255,250,205,1],
	        'lightblue': [173,216,230,1], 'lightcoral': [240,128,128,1],
	        'lightcyan': [224,255,255,1], 'lightgoldenrodyellow': [250,250,210,1],
	        'lightgray': [211,211,211,1], 'lightgreen': [144,238,144,1],
	        'lightgrey': [211,211,211,1], 'lightpink': [255,182,193,1],
	        'lightsalmon': [255,160,122,1], 'lightseagreen': [32,178,170,1],
	        'lightskyblue': [135,206,250,1], 'lightslategray': [119,136,153,1],
	        'lightslategrey': [119,136,153,1], 'lightsteelblue': [176,196,222,1],
	        'lightyellow': [255,255,224,1], 'lime': [0,255,0,1],
	        'limegreen': [50,205,50,1], 'linen': [250,240,230,1],
	        'magenta': [255,0,255,1], 'maroon': [128,0,0,1],
	        'mediumaquamarine': [102,205,170,1], 'mediumblue': [0,0,205,1],
	        'mediumorchid': [186,85,211,1], 'mediumpurple': [147,112,219,1],
	        'mediumseagreen': [60,179,113,1], 'mediumslateblue': [123,104,238,1],
	        'mediumspringgreen': [0,250,154,1], 'mediumturquoise': [72,209,204,1],
	        'mediumvioletred': [199,21,133,1], 'midnightblue': [25,25,112,1],
	        'mintcream': [245,255,250,1], 'mistyrose': [255,228,225,1],
	        'moccasin': [255,228,181,1], 'navajowhite': [255,222,173,1],
	        'navy': [0,0,128,1], 'oldlace': [253,245,230,1],
	        'olive': [128,128,0,1], 'olivedrab': [107,142,35,1],
	        'orange': [255,165,0,1], 'orangered': [255,69,0,1],
	        'orchid': [218,112,214,1], 'palegoldenrod': [238,232,170,1],
	        'palegreen': [152,251,152,1], 'paleturquoise': [175,238,238,1],
	        'palevioletred': [219,112,147,1], 'papayawhip': [255,239,213,1],
	        'peachpuff': [255,218,185,1], 'peru': [205,133,63,1],
	        'pink': [255,192,203,1], 'plum': [221,160,221,1],
	        'powderblue': [176,224,230,1], 'purple': [128,0,128,1],
	        'red': [255,0,0,1], 'rosybrown': [188,143,143,1],
	        'royalblue': [65,105,225,1], 'saddlebrown': [139,69,19,1],
	        'salmon': [250,128,114,1], 'sandybrown': [244,164,96,1],
	        'seagreen': [46,139,87,1], 'seashell': [255,245,238,1],
	        'sienna': [160,82,45,1], 'silver': [192,192,192,1],
	        'skyblue': [135,206,235,1], 'slateblue': [106,90,205,1],
	        'slategray': [112,128,144,1], 'slategrey': [112,128,144,1],
	        'snow': [255,250,250,1], 'springgreen': [0,255,127,1],
	        'steelblue': [70,130,180,1], 'tan': [210,180,140,1],
	        'teal': [0,128,128,1], 'thistle': [216,191,216,1],
	        'tomato': [255,99,71,1], 'turquoise': [64,224,208,1],
	        'violet': [238,130,238,1], 'wheat': [245,222,179,1],
	        'white': [255,255,255,1], 'whitesmoke': [245,245,245,1],
	        'yellow': [255,255,0,1], 'yellowgreen': [154,205,50,1]
	    };

	    function clampCssByte(i) {  // Clamp to integer 0 .. 255.
	        i = Math.round(i);  // Seems to be what Chrome does (vs truncation).
	        return i < 0 ? 0 : i > 255 ? 255 : i;
	    }

	    function clampCssAngle(i) {  // Clamp to integer 0 .. 360.
	        i = Math.round(i);  // Seems to be what Chrome does (vs truncation).
	        return i < 0 ? 0 : i > 360 ? 360 : i;
	    }

	    function clampCssFloat(f) {  // Clamp to float 0.0 .. 1.0.
	        return f < 0 ? 0 : f > 1 ? 1 : f;
	    }

	    function parseCssInt(str) {  // int or percentage.
	        if (str.length && str.charAt(str.length - 1) === '%') {
	            return clampCssByte(parseFloat(str) / 100 * 255);
	        }
	        return clampCssByte(parseInt(str, 10));
	    }

	    function parseCssFloat(str) {  // float or percentage.
	        if (str.length && str.charAt(str.length - 1) === '%') {
	            return clampCssFloat(parseFloat(str) / 100);
	        }
	        return clampCssFloat(parseFloat(str));
	    }

	    function cssHueToRgb(m1, m2, h) {
	        if (h < 0) {
	            h += 1;
	        }
	        else if (h > 1) {
	            h -= 1;
	        }

	        if (h * 6 < 1) {
	            return m1 + (m2 - m1) * h * 6;
	        }
	        if (h * 2 < 1) {
	            return m2;
	        }
	        if (h * 3 < 2) {
	            return m1 + (m2 - m1) * (2/3 - h) * 6;
	        }
	        return m1;
	    }

	    function lerp(a, b, p) {
	        return a + (b - a) * p;
	    }

	    /**
	     * @param {string} colorStr
	     * @return {Array.<number>}
	     * @memberOf module:zrender/util/color
	     */
	    function parse(colorStr) {
	        if (!colorStr) {
	            return;
	        }
	        // colorStr may be not string
	        colorStr = colorStr + '';
	        // Remove all whitespace, not compliant, but should just be more accepting.
	        var str = colorStr.replace(/ /g, '').toLowerCase();

	        // Color keywords (and transparent) lookup.
	        if (str in kCSSColorTable) {
	            return kCSSColorTable[str].slice();  // dup.
	        }

	        // #abc and #abc123 syntax.
	        if (str.charAt(0) === '#') {
	            if (str.length === 4) {
	                var iv = parseInt(str.substr(1), 16);  // TODO(deanm): Stricter parsing.
	                if (!(iv >= 0 && iv <= 0xfff)) {
	                    return;  // Covers NaN.
	                }
	                return [
	                    ((iv & 0xf00) >> 4) | ((iv & 0xf00) >> 8),
	                    (iv & 0xf0) | ((iv & 0xf0) >> 4),
	                    (iv & 0xf) | ((iv & 0xf) << 4),
	                    1
	                ];
	            }
	            else if (str.length === 7) {
	                var iv = parseInt(str.substr(1), 16);  // TODO(deanm): Stricter parsing.
	                if (!(iv >= 0 && iv <= 0xffffff)) {
	                    return;  // Covers NaN.
	                }
	                return [
	                    (iv & 0xff0000) >> 16,
	                    (iv & 0xff00) >> 8,
	                    iv & 0xff,
	                    1
	                ];
	            }

	            return;
	        }
	        var op = str.indexOf('('), ep = str.indexOf(')');
	        if (op !== -1 && ep + 1 === str.length) {
	            var fname = str.substr(0, op);
	            var params = str.substr(op + 1, ep - (op + 1)).split(',');
	            var alpha = 1;  // To allow case fallthrough.
	            switch (fname) {
	                case 'rgba':
	                    if (params.length !== 4) {
	                        return;
	                    }
	                    alpha = parseCssFloat(params.pop()); // jshint ignore:line
	                // Fall through.
	                case 'rgb':
	                    if (params.length !== 3) {
	                        return;
	                    }
	                    return [
	                        parseCssInt(params[0]),
	                        parseCssInt(params[1]),
	                        parseCssInt(params[2]),
	                        alpha
	                    ];
	                case 'hsla':
	                    if (params.length !== 4) {
	                        return;
	                    }
	                    params[3] = parseCssFloat(params[3]);
	                    return hsla2rgba(params);
	                case 'hsl':
	                    if (params.length !== 3) {
	                        return;
	                    }
	                    return hsla2rgba(params);
	                default:
	                    return;
	            }
	        }

	        return;
	    }

	    /**
	     * @param {Array.<number>} hsla
	     * @return {Array.<number>} rgba
	     */
	    function hsla2rgba(hsla) {
	        var h = (((parseFloat(hsla[0]) % 360) + 360) % 360) / 360;  // 0 .. 1
	        // NOTE(deanm): According to the CSS spec s/l should only be
	        // percentages, but we don't bother and let float or percentage.
	        var s = parseCssFloat(hsla[1]);
	        var l = parseCssFloat(hsla[2]);
	        var m2 = l <= 0.5 ? l * (s + 1) : l + s - l * s;
	        var m1 = l * 2 - m2;

	        var rgba = [
	            clampCssByte(cssHueToRgb(m1, m2, h + 1 / 3) * 255),
	            clampCssByte(cssHueToRgb(m1, m2, h) * 255),
	            clampCssByte(cssHueToRgb(m1, m2, h - 1 / 3) * 255)
	        ];

	        if (hsla.length === 4) {
	            rgba[3] = hsla[3];
	        }

	        return rgba;
	    }

	    /**
	     * @param {Array.<number>} rgba
	     * @return {Array.<number>} hsla
	     */
	    function rgba2hsla(rgba) {
	        if (!rgba) {
	            return;
	        }

	        // RGB from 0 to 255
	        var R = rgba[0] / 255;
	        var G = rgba[1] / 255;
	        var B = rgba[2] / 255;

	        var vMin = Math.min(R, G, B); // Min. value of RGB
	        var vMax = Math.max(R, G, B); // Max. value of RGB
	        var delta = vMax - vMin; // Delta RGB value

	        var L = (vMax + vMin) / 2;
	        var H;
	        var S;
	        // HSL results from 0 to 1
	        if (delta === 0) {
	            H = 0;
	            S = 0;
	        }
	        else {
	            if (L < 0.5) {
	                S = delta / (vMax + vMin);
	            }
	            else {
	                S = delta / (2 - vMax - vMin);
	            }

	            var deltaR = (((vMax - R) / 6) + (delta / 2)) / delta;
	            var deltaG = (((vMax - G) / 6) + (delta / 2)) / delta;
	            var deltaB = (((vMax - B) / 6) + (delta / 2)) / delta;

	            if (R === vMax) {
	                H = deltaB - deltaG;
	            }
	            else if (G === vMax) {
	                H = (1 / 3) + deltaR - deltaB;
	            }
	            else if (B === vMax) {
	                H = (2 / 3) + deltaG - deltaR;
	            }

	            if (H < 0) {
	                H += 1;
	            }

	            if (H > 1) {
	                H -= 1;
	            }
	        }

	        var hsla = [H * 360, S, L];

	        if (rgba[3] != null) {
	            hsla.push(rgba[3]);
	        }

	        return hsla;
	    }

	    /**
	     * @param {string} color
	     * @param {number} level
	     * @return {string}
	     * @memberOf module:zrender/util/color
	     */
	    function lift(color, level) {
	        var colorArr = parse(color);
	        if (colorArr) {
	            for (var i = 0; i < 3; i++) {
	                if (level < 0) {
	                    colorArr[i] = colorArr[i] * (1 - level) | 0;
	                }
	                else {
	                    colorArr[i] = ((255 - colorArr[i]) * level + colorArr[i]) | 0;
	                }
	            }
	            return stringify(colorArr, colorArr.length === 4 ? 'rgba' : 'rgb');
	        }
	    }

	    /**
	     * @param {string} color
	     * @return {string}
	     * @memberOf module:zrender/util/color
	     */
	    function toHex(color, level) {
	        var colorArr = parse(color);
	        if (colorArr) {
	            return ((1 << 24) + (colorArr[0] << 16) + (colorArr[1] << 8) + (+colorArr[2])).toString(16).slice(1);
	        }
	    }

	    /**
	     * Map value to color. Faster than mapToColor methods because color is represented by rgba array
	     * @param {number} normalizedValue A float between 0 and 1.
	     * @param {Array.<Array.<number>>} colors List of rgba color array
	     * @param {Array.<number>} [out] Mapped gba color array
	     * @return {Array.<number>}
	     */
	    function fastMapToColor(normalizedValue, colors, out) {
	        if (!(colors && colors.length)
	            || !(normalizedValue >= 0 && normalizedValue <= 1)
	        ) {
	            return;
	        }
	        out = out || [0, 0, 0, 0];
	        var value = normalizedValue * (colors.length - 1);
	        var leftIndex = Math.floor(value);
	        var rightIndex = Math.ceil(value);
	        var leftColor = colors[leftIndex];
	        var rightColor = colors[rightIndex];
	        var dv = value - leftIndex;
	        out[0] = clampCssByte(lerp(leftColor[0], rightColor[0], dv));
	        out[1] = clampCssByte(lerp(leftColor[1], rightColor[1], dv));
	        out[2] = clampCssByte(lerp(leftColor[2], rightColor[2], dv));
	        out[3] = clampCssByte(lerp(leftColor[3], rightColor[3], dv));
	        return out;
	    }
	    /**
	     * @param {number} normalizedValue A float between 0 and 1.
	     * @param {Array.<string>} colors Color list.
	     * @param {boolean=} fullOutput Default false.
	     * @return {(string|Object)} Result color. If fullOutput,
	     *                           return {color: ..., leftIndex: ..., rightIndex: ..., value: ...},
	     * @memberOf module:zrender/util/color
	     */
	    function mapToColor(normalizedValue, colors, fullOutput) {
	        if (!(colors && colors.length)
	            || !(normalizedValue >= 0 && normalizedValue <= 1)
	        ) {
	            return;
	        }

	        var value = normalizedValue * (colors.length - 1);
	        var leftIndex = Math.floor(value);
	        var rightIndex = Math.ceil(value);
	        var leftColor = parse(colors[leftIndex]);
	        var rightColor = parse(colors[rightIndex]);
	        var dv = value - leftIndex;

	        var color = stringify(
	            [
	                clampCssByte(lerp(leftColor[0], rightColor[0], dv)),
	                clampCssByte(lerp(leftColor[1], rightColor[1], dv)),
	                clampCssByte(lerp(leftColor[2], rightColor[2], dv)),
	                clampCssFloat(lerp(leftColor[3], rightColor[3], dv))
	            ],
	            'rgba'
	        );

	        return fullOutput
	            ? {
	                color: color,
	                leftIndex: leftIndex,
	                rightIndex: rightIndex,
	                value: value
	            }
	            : color;
	    }

	    /**
	     * @param {string} color
	     * @param {number=} h 0 ~ 360, ignore when null.
	     * @param {number=} s 0 ~ 1, ignore when null.
	     * @param {number=} l 0 ~ 1, ignore when null.
	     * @return {string} Color string in rgba format.
	     * @memberOf module:zrender/util/color
	     */
	    function modifyHSL(color, h, s, l) {
	        color = parse(color);

	        if (color) {
	            color = rgba2hsla(color);
	            h != null && (color[0] = clampCssAngle(h));
	            s != null && (color[1] = parseCssFloat(s));
	            l != null && (color[2] = parseCssFloat(l));

	            return stringify(hsla2rgba(color), 'rgba');
	        }
	    }

	    /**
	     * @param {string} color
	     * @param {number=} alpha 0 ~ 1
	     * @return {string} Color string in rgba format.
	     * @memberOf module:zrender/util/color
	     */
	    function modifyAlpha(color, alpha) {
	        color = parse(color);

	        if (color && alpha != null) {
	            color[3] = clampCssFloat(alpha);
	            return stringify(color, 'rgba');
	        }
	    }

	    /**
	     * @param {Array.<string>} colors Color list.
	     * @param {string} type 'rgba', 'hsva', ...
	     * @return {string} Result color.
	     */
	    function stringify(arrColor, type) {
	        var colorStr = arrColor[0] + ',' + arrColor[1] + ',' + arrColor[2];
	        if (type === 'rgba' || type === 'hsva' || type === 'hsla') {
	            colorStr += ',' + arrColor[3];
	        }
	        return type + '(' + colorStr + ')';
	    }

	    module.exports = {
	        parse: parse,
	        lift: lift,
	        toHex: toHex,
	        fastMapToColor: fastMapToColor,
	        mapToColor: mapToColor,
	        modifyHSL: modifyHSL,
	        modifyAlpha: modifyAlpha,
	        stringify: stringify
	    };




/***/ },
/* 24 */
/***/ function(module, exports, __webpack_require__) {

	
	        var config = __webpack_require__(25);

	        /**
	         * @exports zrender/tool/log
	         * @author Kener (@Kener-é‹æ¥€å˜², kener.linfeng@gmail.com)
	         */
	        module.exports = function() {
	            if (config.debugMode === 0) {
	                return;
	            }
	            else if (config.debugMode == 1) {
	                for (var k in arguments) {
	                    throw new Error(arguments[k]);
	                }
	            }
	            else if (config.debugMode > 1) {
	                for (var k in arguments) {
	                    console.log(arguments[k]);
	                }
	            }
	        };

	        /* for debug
	        return function(mes) {
	            document.getElementById('wrong-message').innerHTML =
	                mes + ' ' + (new Date() - 0)
	                + '<br/>'
	                + document.getElementById('wrong-message').innerHTML;
	        };
	        */
	    


/***/ },
/* 25 */
/***/ function(module, exports) {

	
	    var dpr = 1;
	    // If in browser environment
	    if (typeof window !== 'undefined') {
	        dpr = Math.max(window.devicePixelRatio || 1, 1);
	    }
	    /**
	     * configæ¦›æ¨¿î…»é–°å¶‡ç–†æ¤¤ï¿½
	     * @exports zrender/config
	     * @author Kener (@Kener-é‹æ¥€å˜², kener.linfeng@gmail.com)
	     */
	    var config = {
	        /**
	         * debugéƒãƒ¥ç¹”é–«å¤ã€é”›æ­atchBrushExceptionæ¶“ç°rueæ¶“å¬«æ¹éï¿½
	         * 0 : æ¶“å¶‡æ•“éŽ´æ‰ebugéç‰ˆåµé”›å±½å½‚ç”¯å†ªæ•¤
	         * 1 : å¯®å‚šçˆ¶éŽ¶æ¶˜åš­é”›å²ƒçšŸç’‡æ› æ•¤
	         * 2 : éŽºÑƒåŸ—é™æ‹Œç·­é‘çŒ´ç´ç’‹å†­ç˜¯é¢ï¿½
	         */
	        debugMode: 0,

	        // retina çžå¿“ç®·æµ¼æ¨ºå¯²
	        devicePixelRatio: dpr
	    };
	    module.exports = config;




/***/ },
/* 26 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * Mixin for drawing text in a element bounding rect
	 * @module zrender/mixin/RectText
	 */



	    var textContain = __webpack_require__(27);
	    var BoundingRect = __webpack_require__(28);

	    var tmpRect = new BoundingRect();

	    var RectText = function () {};

	    function parsePercent(value, maxValue) {
	        if (typeof value === 'string') {
	            if (value.lastIndexOf('%') >= 0) {
	                return parseFloat(value) / 100 * maxValue;
	            }
	            return parseFloat(value);
	        }
	        return value;
	    }

	    RectText.prototype = {

	        constructor: RectText,

	        /**
	         * Draw text in a rect with specified position.
	         * @param  {CanvasRenderingContext} ctx
	         * @param  {Object} rect Displayable rect
	         * @return {Object} textRect Alternative precalculated text bounding rect
	         */
	        drawRectText: function (ctx, rect, textRect) {
	            var style = this.style;
	            var text = style.text;
	            // Convert to string
	            text != null && (text += '');
	            if (!text) {
	                return;
	            }

	            // FIXME
	            ctx.save();

	            var x;
	            var y;
	            var textPosition = style.textPosition;
	            var textOffset = style.textOffset;
	            var distance = style.textDistance;
	            var align = style.textAlign;
	            var font = style.textFont || style.font;
	            var baseline = style.textBaseline;
	            var verticalAlign = style.textVerticalAlign;

	            textRect = textRect || textContain.getBoundingRect(text, font, align, baseline);

	            // Transform rect to view space
	            var transform = this.transform;
	            if (!style.textTransform) {
	                if (transform) {
	                    tmpRect.copy(rect);
	                    tmpRect.applyTransform(transform);
	                    rect = tmpRect;
	                }
	            }
	            else {
	                this.setTransform(ctx);
	            }

	            // Text position represented by coord
	            if (textPosition instanceof Array) {
	                // Percent
	                x = rect.x + parsePercent(textPosition[0], rect.width);
	                y = rect.y + parsePercent(textPosition[1], rect.height);
	                align = align || 'left';
	                baseline = baseline || 'top';

	                if (verticalAlign) {
	                    switch (verticalAlign) {
	                        case 'middle':
	                            y -= textRect.height / 2 - textRect.lineHeight / 2;
	                            break;
	                        case 'bottom':
	                            y -= textRect.height - textRect.lineHeight / 2;
	                            break;
	                        default:
	                            y += textRect.lineHeight / 2;
	                    }
	                    // Force bseline to be middle
	                    baseline = 'middle';
	                }
	            }
	            else {
	                var res = textContain.adjustTextPositionOnRect(
	                    textPosition, rect, textRect, distance
	                );
	                x = res.x;
	                y = res.y;
	                // Default align and baseline when has textPosition
	                align = align || res.textAlign;
	                baseline = baseline || res.textBaseline;
	            }

	            if (textOffset) {
	                x += textOffset[0];
	                y += textOffset[1];
	            }

	            // Use canvas default left textAlign. Giving invalid value will cause state not change
	            ctx.textAlign = align || 'left';
	            // Use canvas default alphabetic baseline
	            ctx.textBaseline = baseline || 'alphabetic';

	            var textFill = style.textFill;
	            var textStroke = style.textStroke;
	            textFill && (ctx.fillStyle = textFill);
	            textStroke && (ctx.strokeStyle = textStroke);

	            // TODO Invalid font
	            ctx.font = font || '12px sans-serif';

	            // Text shadow
	            // Always set shadowBlur and shadowOffset to avoid leak from displayable
	            ctx.shadowBlur = style.textShadowBlur;
	            ctx.shadowColor = style.textShadowColor || 'transparent';
	            ctx.shadowOffsetX = style.textShadowOffsetX;
	            ctx.shadowOffsetY = style.textShadowOffsetY;

	            var textLines = text.split('\n');

	            if (style.textRotation) {
	                transform && ctx.translate(transform[4], transform[5]);
	                ctx.rotate(style.textRotation);
	                transform && ctx.translate(-transform[4], -transform[5]);
	            }

	            for (var i = 0; i < textLines.length; i++) {
	                textFill && ctx.fillText(textLines[i], x, y);
	                textStroke && ctx.strokeText(textLines[i], x, y);
	                y += textRect.lineHeight;
	            }

	            ctx.restore();
	        }
	    };

	    module.exports = RectText;


/***/ },
/* 27 */
/***/ function(module, exports, __webpack_require__) {

	

	    var textWidthCache = {};
	    var textWidthCacheCounter = 0;
	    var TEXT_CACHE_MAX = 5000;

	    var util = __webpack_require__(5);
	    var BoundingRect = __webpack_require__(28);
	    var retrieve = util.retrieve;

	    function getTextWidth(text, textFont) {
	        var key = text + ':' + textFont;
	        if (textWidthCache[key]) {
	            return textWidthCache[key];
	        }

	        var textLines = (text + '').split('\n');
	        var width = 0;

	        for (var i = 0, l = textLines.length; i < l; i++) {
	            // measureText é™îˆ™äº’çšî‚¥î›«é©æ ¦äº’éç…Žî†æ¶“å¶†æ•®éŽ¸ï¿½ Canvas é¨å‹­å¹†æ¾§ï¿½
	            width = Math.max(textContain.measureText(textLines[i], textFont).width, width);
	        }

	        if (textWidthCacheCounter > TEXT_CACHE_MAX) {
	            textWidthCacheCounter = 0;
	            textWidthCache = {};
	        }
	        textWidthCacheCounter++;
	        textWidthCache[key] = width;

	        return width;
	    }

	    function getTextRect(text, textFont, textAlign, textBaseline) {
	        var textLineLen = ((text || '') + '').split('\n').length;

	        var width = getTextWidth(text, textFont);
	        // FIXME æ¥‚æ¨ºå®³ç’ï¼„ç•»å§£æ—‡ç·ç»®æ¥æ¯š
	        var lineHeight = getTextWidth('é¥ï¿½', textFont);
	        var height = textLineLen * lineHeight;

	        var rect = new BoundingRect(0, 0, width, height);
	        // Text has a special line height property
	        rect.lineHeight = lineHeight;

	        switch (textBaseline) {
	            case 'bottom':
	            case 'alphabetic':
	                rect.y -= lineHeight;
	                break;
	            case 'middle':
	                rect.y -= lineHeight / 2;
	                break;
	            // case 'hanging':
	            // case 'top':
	        }

	        // FIXME Right to left language
	        switch (textAlign) {
	            case 'end':
	            case 'right':
	                rect.x -= rect.width;
	                break;
	            case 'center':
	                rect.x -= rect.width / 2;
	                break;
	            // case 'start':
	            // case 'left':
	        }

	        return rect;
	    }

	    function adjustTextPositionOnRect(textPosition, rect, textRect, distance) {

	        var x = rect.x;
	        var y = rect.y;

	        var height = rect.height;
	        var width = rect.width;

	        var textHeight = textRect.height;

	        var halfHeight = height / 2 - textHeight / 2;

	        var textAlign = 'left';

	        switch (textPosition) {
	            case 'left':
	                x -= distance;
	                y += halfHeight;
	                textAlign = 'right';
	                break;
	            case 'right':
	                x += distance + width;
	                y += halfHeight;
	                textAlign = 'left';
	                break;
	            case 'top':
	                x += width / 2;
	                y -= distance + textHeight;
	                textAlign = 'center';
	                break;
	            case 'bottom':
	                x += width / 2;
	                y += height + distance;
	                textAlign = 'center';
	                break;
	            case 'inside':
	                x += width / 2;
	                y += halfHeight;
	                textAlign = 'center';
	                break;
	            case 'insideLeft':
	                x += distance;
	                y += halfHeight;
	                textAlign = 'left';
	                break;
	            case 'insideRight':
	                x += width - distance;
	                y += halfHeight;
	                textAlign = 'right';
	                break;
	            case 'insideTop':
	                x += width / 2;
	                y += distance;
	                textAlign = 'center';
	                break;
	            case 'insideBottom':
	                x += width / 2;
	                y += height - textHeight - distance;
	                textAlign = 'center';
	                break;
	            case 'insideTopLeft':
	                x += distance;
	                y += distance;
	                textAlign = 'left';
	                break;
	            case 'insideTopRight':
	                x += width - distance;
	                y += distance;
	                textAlign = 'right';
	                break;
	            case 'insideBottomLeft':
	                x += distance;
	                y += height - textHeight - distance;
	                break;
	            case 'insideBottomRight':
	                x += width - distance;
	                y += height - textHeight - distance;
	                textAlign = 'right';
	                break;
	        }

	        return {
	            x: x,
	            y: y,
	            textAlign: textAlign,
	            textBaseline: 'top'
	        };
	    }

	    /**
	     * Show ellipsis if overflow.
	     *
	     * @param  {string} text
	     * @param  {string} containerWidth
	     * @param  {string} textFont
	     * @param  {number} [ellipsis='...']
	     * @param  {Object} [options]
	     * @param  {number} [options.maxIterations=3]
	     * @param  {number} [options.minChar=0] If truncate result are less
	     *                  then minChar, ellipsis will not show, which is
	     *                  better for user hint in some cases.
	     * @param  {number} [options.placeholder=''] When all truncated, use the placeholder.
	     * @return {string}
	     */
	    function truncateText(text, containerWidth, textFont, ellipsis, options) {
	        if (!containerWidth) {
	            return '';
	        }

	        options = options || {};

	        ellipsis = retrieve(ellipsis, '...');
	        var maxIterations = retrieve(options.maxIterations, 2);
	        var minChar = retrieve(options.minChar, 0);
	        // FIXME
	        // Other languages?
	        var cnCharWidth = getTextWidth('é¥ï¿½', textFont);
	        // FIXME
	        // Consider proportional font?
	        var ascCharWidth = getTextWidth('a', textFont);
	        var placeholder = retrieve(options.placeholder, '');

	        // Example 1: minChar: 3, text: 'asdfzxcv', truncate result: 'asdf', but not: 'a...'.
	        // Example 2: minChar: 3, text: 'ç¼æ‘å®³', truncate result: 'ç¼ï¿½', but not: '...'.
	        var contentWidth = containerWidth = Math.max(0, containerWidth - 1); // Reserve some gap.
	        for (var i = 0; i < minChar && contentWidth >= ascCharWidth; i++) {
	            contentWidth -= ascCharWidth;
	        }

	        var ellipsisWidth = getTextWidth(ellipsis);
	        if (ellipsisWidth > contentWidth) {
	            ellipsis = '';
	            ellipsisWidth = 0;
	        }

	        contentWidth = containerWidth - ellipsisWidth;

	        var textLines = (text + '').split('\n');

	        for (var i = 0, len = textLines.length; i < len; i++) {
	            var textLine = textLines[i];
	            var lineWidth = getTextWidth(textLine, textFont);

	            if (lineWidth <= containerWidth) {
	                continue;
	            }

	            for (var j = 0;; j++) {
	                if (lineWidth <= contentWidth || j >= maxIterations) {
	                    textLine += ellipsis;
	                    break;
	                }

	                var subLength = j === 0
	                    ? estimateLength(textLine, contentWidth, ascCharWidth, cnCharWidth)
	                    : lineWidth > 0
	                    ? Math.floor(textLine.length * contentWidth / lineWidth)
	                    : 0;

	                textLine = textLine.substr(0, subLength);
	                lineWidth = getTextWidth(textLine, textFont);
	            }

	            if (textLine === '') {
	                textLine = placeholder;
	            }

	            textLines[i] = textLine;
	        }

	        return textLines.join('\n');
	    }

	    function estimateLength(text, contentWidth, ascCharWidth, cnCharWidth) {
	        var width = 0;
	        var i = 0;
	        for (var len = text.length; i < len && width < contentWidth; i++) {
	            var charCode = text.charCodeAt(i);
	            width += (0 <= charCode && charCode <= 127) ? ascCharWidth : cnCharWidth;
	        }
	        return i;
	    }

	    var textContain = {

	        getWidth: getTextWidth,

	        getBoundingRect: getTextRect,

	        adjustTextPositionOnRect: adjustTextPositionOnRect,

	        truncateText: truncateText,

	        measureText: function (text, textFont) {
	            var ctx = util.getContext();
	            ctx.font = textFont || '12px sans-serif';
	            return ctx.measureText(text);
	        }
	    };

	    module.exports = textContain;


/***/ },
/* 28 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	/**
	 * @module echarts/core/BoundingRect
	 */


	    var vec2 = __webpack_require__(18);
	    var matrix = __webpack_require__(17);

	    var v2ApplyTransform = vec2.applyTransform;
	    var mathMin = Math.min;
	    var mathMax = Math.max;
	    /**
	     * @alias module:echarts/core/BoundingRect
	     */
	    function BoundingRect(x, y, width, height) {

	        if (width < 0) {
	            x = x + width;
	            width = -width;
	        }
	        if (height < 0) {
	            y = y + height;
	            height = -height;
	        }

	        /**
	         * @type {number}
	         */
	        this.x = x;
	        /**
	         * @type {number}
	         */
	        this.y = y;
	        /**
	         * @type {number}
	         */
	        this.width = width;
	        /**
	         * @type {number}
	         */
	        this.height = height;
	    }

	    BoundingRect.prototype = {

	        constructor: BoundingRect,

	        /**
	         * @param {module:echarts/core/BoundingRect} other
	         */
	        union: function (other) {
	            var x = mathMin(other.x, this.x);
	            var y = mathMin(other.y, this.y);

	            this.width = mathMax(
	                    other.x + other.width,
	                    this.x + this.width
	                ) - x;
	            this.height = mathMax(
	                    other.y + other.height,
	                    this.y + this.height
	                ) - y;
	            this.x = x;
	            this.y = y;
	        },

	        /**
	         * @param {Array.<number>} m
	         * @methods
	         */
	        applyTransform: (function () {
	            var lt = [];
	            var rb = [];
	            var lb = [];
	            var rt = [];
	            return function (m) {
	                // In case usage like this
	                // el.getBoundingRect().applyTransform(el.transform)
	                // And element has no transform
	                if (!m) {
	                    return;
	                }
	                lt[0] = lb[0] = this.x;
	                lt[1] = rt[1] = this.y;
	                rb[0] = rt[0] = this.x + this.width;
	                rb[1] = lb[1] = this.y + this.height;

	                v2ApplyTransform(lt, lt, m);
	                v2ApplyTransform(rb, rb, m);
	                v2ApplyTransform(lb, lb, m);
	                v2ApplyTransform(rt, rt, m);

	                this.x = mathMin(lt[0], rb[0], lb[0], rt[0]);
	                this.y = mathMin(lt[1], rb[1], lb[1], rt[1]);
	                var maxX = mathMax(lt[0], rb[0], lb[0], rt[0]);
	                var maxY = mathMax(lt[1], rb[1], lb[1], rt[1]);
	                this.width = maxX - this.x;
	                this.height = maxY - this.y;
	            };
	        })(),

	        /**
	         * Calculate matrix of transforming from self to target rect
	         * @param  {module:zrender/core/BoundingRect} b
	         * @return {Array.<number>}
	         */
	        calculateTransform: function (b) {
	            var a = this;
	            var sx = b.width / a.width;
	            var sy = b.height / a.height;

	            var m = matrix.create();

	            // é­â•…æ¨€é™å……ç®»
	            matrix.translate(m, m, [-a.x, -a.y]);
	            matrix.scale(m, m, [sx, sy]);
	            matrix.translate(m, m, [b.x, b.y]);

	            return m;
	        },

	        /**
	         * @param {(module:echarts/core/BoundingRect|Object)} b
	         * @return {boolean}
	         */
	        intersect: function (b) {
	            if (!b) {
	                return false;
	            }

	            if (!(b instanceof BoundingRect)) {
	                // Normalize negative width/height.
	                b = BoundingRect.create(b);
	            }

	            var a = this;
	            var ax0 = a.x;
	            var ax1 = a.x + a.width;
	            var ay0 = a.y;
	            var ay1 = a.y + a.height;

	            var bx0 = b.x;
	            var bx1 = b.x + b.width;
	            var by0 = b.y;
	            var by1 = b.y + b.height;

	            return ! (ax1 < bx0 || bx1 < ax0 || ay1 < by0 || by1 < ay0);
	        },

	        contain: function (x, y) {
	            var rect = this;
	            return x >= rect.x
	                && x <= (rect.x + rect.width)
	                && y >= rect.y
	                && y <= (rect.y + rect.height);
	        },

	        /**
	         * @return {module:echarts/core/BoundingRect}
	         */
	        clone: function () {
	            return new BoundingRect(this.x, this.y, this.width, this.height);
	        },

	        /**
	         * Copy from another rect
	         */
	        copy: function (other) {
	            this.x = other.x;
	            this.y = other.y;
	            this.width = other.width;
	            this.height = other.height;
	        },

	        plain: function () {
	            return {
	                x: this.x,
	                y: this.y,
	                width: this.width,
	                height: this.height
	            };
	        }
	    };

	    /**
	     * @param {Object|module:zrender/core/BoundingRect} rect
	     * @param {number} rect.x
	     * @param {number} rect.y
	     * @param {number} rect.width
	     * @param {number} rect.height
	     * @return {module:zrender/core/BoundingRect}
	     */
	    BoundingRect.create = function (rect) {
	        return new BoundingRect(rect.x, rect.y, rect.width, rect.height);
	    };

	    module.exports = BoundingRect;


/***/ },
/* 29 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	/**
	 * Path æµ ï½‡æ‚Šé”›å±½å½²æµ ãƒ¥æ¹ª`buildPath`æ¶“î… æ•¤æµœåº¢æµ›æµ î–¦ctx`, æµ¼æ°«ç¹šç€›æ¨»ç˜¡æ¶“çŒµathéŽ¿å¶„ç¶”é¨å‹«æ‡¡æµ ã‚…åŸŒpathCommandsçžç‚´â‚¬Ñ‚è…‘
	 * é™îˆ™äº’é¢ã„¤ç°¬ isInsidePath é’ã‚†æŸ‡æµ ãƒ¥å¼·é‘¾å³°å½‡boundingRect
	 *
	 * @module zrender/core/PathProxy
	 * @author Yi Shen (http://www.github.com/pissang)
	 */

	 // TODO getTotalLength, getPointAtLength


	    var curve = __webpack_require__(30);
	    var vec2 = __webpack_require__(18);
	    var bbox = __webpack_require__(31);
	    var BoundingRect = __webpack_require__(28);
	    var dpr = __webpack_require__(25).devicePixelRatio;

	    var CMD = {
	        M: 1,
	        L: 2,
	        C: 3,
	        Q: 4,
	        A: 5,
	        Z: 6,
	        // Rect
	        R: 7
	    };

	    var min = [];
	    var max = [];
	    var min2 = [];
	    var max2 = [];
	    var mathMin = Math.min;
	    var mathMax = Math.max;
	    var mathCos = Math.cos;
	    var mathSin = Math.sin;
	    var mathSqrt = Math.sqrt;
	    var mathAbs = Math.abs;

	    var hasTypedArray = typeof Float32Array != 'undefined';

	    /**
	     * @alias module:zrender/core/PathProxy
	     * @constructor
	     */
	    var PathProxy = function () {

	        /**
	         * Path data. Stored as flat array
	         * @type {Array.<Object>}
	         */
	        this.data = [];

	        this._len = 0;

	        this._ctx = null;

	        this._xi = 0;
	        this._yi = 0;

	        this._x0 = 0;
	        this._y0 = 0;

	        // Unit x, Unit y. Provide for avoiding drawing that too short line segment
	        this._ux = 0;
	        this._uy = 0;
	    };

	    /**
	     * è¹‡î‚¦â‚¬ç†»î…¸ç» æ¡ºathé–å‘­æ´¿é©æŽžç´™éªžæœµç¬‰é„îˆ›æ¸¶çå¿“å¯˜é¥å¯¸æ´…é”›ï¿½
	     * @return {Object}
	     */
	    PathProxy.prototype = {

	        constructor: PathProxy,

	        _lineDash: null,

	        _dashOffset: 0,

	        _dashIdx: 0,

	        _dashSum: 0,

	        /**
	         * @readOnly
	         */
	        setScale: function (sx, sy) {
	            this._ux = mathAbs(1 / dpr / sx) || 0;
	            this._uy = mathAbs(1 / dpr / sy) || 0;
	        },

	        getContext: function () {
	            return this._ctx;
	        },

	        /**
	         * @param  {CanvasRenderingContext2D} ctx
	         * @return {module:zrender/core/PathProxy}
	         */
	        beginPath: function (ctx) {

	            this._ctx = ctx;

	            ctx && ctx.beginPath();

	            ctx && (this.dpr = ctx.dpr);

	            // Reset
	            this._len = 0;

	            if (this._lineDash) {
	                this._lineDash = null;

	                this._dashOffset = 0;
	            }

	            return this;
	        },

	        /**
	         * @param  {number} x
	         * @param  {number} y
	         * @return {module:zrender/core/PathProxy}
	         */
	        moveTo: function (x, y) {
	            this.addData(CMD.M, x, y);
	            this._ctx && this._ctx.moveTo(x, y);

	            // x0, y0, xi, yi é„îˆî†‡è¤°æ›žæ¹ª _dashedXXXXTo é‚è§„ç¡¶æ¶“î…å¨‡é¢ï¿½
	            // xi, yi ç’æ¿ç¶è¤°æ’³å¢ éï¿½, x0, y0 é¦ï¿½ closePath é¨å‹¬æ¤‚éŠæ¬æ´–é’æ‹Œæ£æ¿®å¬¬å£éŠ†ï¿½
	            // éˆå¤Šå½²é‘³è—‰æ¹ª beginPath æ¶”å¬ªæ‚—é©å­˜å¸´ç’‹å†ªæ•¤ lineToé”›å²ƒç¹–éƒè·ºâ‚¬ï¿½ x0, y0 é—‡â‚¬ç‘•ï¿½
	            // é¦ï¿½ lineTo é‚è§„ç¡¶æ¶“î…¡î†‡è¤°æ›ªç´æ©æ¬“å™·éå œç¬‰é‘°å†­æª»æ©æ¬‘î’éŽ¯å‘­å–Œé”›å®’ashed line æ¶”ç†·å½§é¦ï¿½ IE10- æ¶“î…ç¬‰é€îˆ›å¯”
	            this._x0 = x;
	            this._y0 = y;

	            this._xi = x;
	            this._yi = y;

	            return this;
	        },

	        /**
	         * @param  {number} x
	         * @param  {number} y
	         * @return {module:zrender/core/PathProxy}
	         */
	        lineTo: function (x, y) {
	            var exceedUnit = mathAbs(x - this._xi) > this._ux
	                || mathAbs(y - this._yi) > this._uy
	                // Force draw the first segment
	                || this._len < 5;

	            this.addData(CMD.L, x, y);

	            if (this._ctx && exceedUnit) {
	                this._needsDash() ? this._dashedLineTo(x, y)
	                    : this._ctx.lineTo(x, y);
	            }
	            if (exceedUnit) {
	                this._xi = x;
	                this._yi = y;
	            }

	            return this;
	        },

	        /**
	         * @param  {number} x1
	         * @param  {number} y1
	         * @param  {number} x2
	         * @param  {number} y2
	         * @param  {number} x3
	         * @param  {number} y3
	         * @return {module:zrender/core/PathProxy}
	         */
	        bezierCurveTo: function (x1, y1, x2, y2, x3, y3) {
	            this.addData(CMD.C, x1, y1, x2, y2, x3, y3);
	            if (this._ctx) {
	                this._needsDash() ? this._dashedBezierTo(x1, y1, x2, y2, x3, y3)
	                    : this._ctx.bezierCurveTo(x1, y1, x2, y2, x3, y3);
	            }
	            this._xi = x3;
	            this._yi = y3;
	            return this;
	        },

	        /**
	         * @param  {number} x1
	         * @param  {number} y1
	         * @param  {number} x2
	         * @param  {number} y2
	         * @return {module:zrender/core/PathProxy}
	         */
	        quadraticCurveTo: function (x1, y1, x2, y2) {
	            this.addData(CMD.Q, x1, y1, x2, y2);
	            if (this._ctx) {
	                this._needsDash() ? this._dashedQuadraticTo(x1, y1, x2, y2)
	                    : this._ctx.quadraticCurveTo(x1, y1, x2, y2);
	            }
	            this._xi = x2;
	            this._yi = y2;
	            return this;
	        },

	        /**
	         * @param  {number} cx
	         * @param  {number} cy
	         * @param  {number} r
	         * @param  {number} startAngle
	         * @param  {number} endAngle
	         * @param  {boolean} anticlockwise
	         * @return {module:zrender/core/PathProxy}
	         */
	        arc: function (cx, cy, r, startAngle, endAngle, anticlockwise) {
	            this.addData(
	                CMD.A, cx, cy, r, r, startAngle, endAngle - startAngle, 0, anticlockwise ? 0 : 1
	            );
	            this._ctx && this._ctx.arc(cx, cy, r, startAngle, endAngle, anticlockwise);

	            this._xi = mathCos(endAngle) * r + cx;
	            this._yi = mathSin(endAngle) * r + cx;
	            return this;
	        },

	        // TODO
	        arcTo: function (x1, y1, x2, y2, radius) {
	            if (this._ctx) {
	                this._ctx.arcTo(x1, y1, x2, y2, radius);
	            }
	            return this;
	        },

	        // TODO
	        rect: function (x, y, w, h) {
	            this._ctx && this._ctx.rect(x, y, w, h);
	            this.addData(CMD.R, x, y, w, h);
	            return this;
	        },

	        /**
	         * @return {module:zrender/core/PathProxy}
	         */
	        closePath: function () {
	            this.addData(CMD.Z);

	            var ctx = this._ctx;
	            var x0 = this._x0;
	            var y0 = this._y0;
	            if (ctx) {
	                this._needsDash() && this._dashedLineTo(x0, y0);
	                ctx.closePath();
	            }

	            this._xi = x0;
	            this._yi = y0;
	            return this;
	        },

	        /**
	         * Context æµ åº¡î˜»é–®ã„¤ç´¶éãƒ¯ç´é¥çŠ±è´Ÿéˆå¤Šå½²é‘³èŠ¥æ§¸ rebuildPath ç€¹å±¼ç®£éšåº¡å•€ filléŠ†ï¿½
	         * stroke éšå±¾ç‰±
	         * @param {CanvasRenderingContext2D} ctx
	         * @return {module:zrender/core/PathProxy}
	         */
	        fill: function (ctx) {
	            ctx && ctx.fill();
	            this.toStatic();
	        },

	        /**
	         * @param {CanvasRenderingContext2D} ctx
	         * @return {module:zrender/core/PathProxy}
	         */
	        stroke: function (ctx) {
	            ctx && ctx.stroke();
	            this.toStatic();
	        },

	        /**
	         * è¹‡å‘´ã€é¦ã„¥å¾ç€¹å†ªç²¯é’è·ºæ‡¡æµ ã‚…å¢ ç’‹å†ªæ•¤
	         * Must be invoked before all other path drawing methods
	         * @return {module:zrender/core/PathProxy}
	         */
	        setLineDash: function (lineDash) {
	            if (lineDash instanceof Array) {
	                this._lineDash = lineDash;

	                this._dashIdx = 0;

	                var lineDashSum = 0;
	                for (var i = 0; i < lineDash.length; i++) {
	                    lineDashSum += lineDash[i];
	                }
	                this._dashSum = lineDashSum;
	            }
	            return this;
	        },

	        /**
	         * è¹‡å‘´ã€é¦ã„¥å¾ç€¹å†ªç²¯é’è·ºæ‡¡æµ ã‚…å¢ ç’‹å†ªæ•¤
	         * Must be invoked before all other path drawing methods
	         * @return {module:zrender/core/PathProxy}
	         */
	        setLineDashOffset: function (offset) {
	            this._dashOffset = offset;
	            return this;
	        },

	        /**
	         *
	         * @return {boolean}
	         */
	        len: function () {
	            return this._len;
	        },

	        /**
	         * é©å­˜å¸´ç’å‰§ç–† Path éç‰ˆåµ
	         */
	        setData: function (data) {

	            var len = data.length;

	            if (! (this.data && this.data.length == len) && hasTypedArray) {
	                this.data = new Float32Array(len);
	            }

	            for (var i = 0; i < len; i++) {
	                this.data[i] = data[i];
	            }

	            this._len = len;
	        },

	        /**
	         * å¨£è¯²å§žç€›æ„¯çŸ¾å¯°ï¿½
	         * @param {module:zrender/core/PathProxy|Array.<module:zrender/core/PathProxy>} path
	         */
	        appendPath: function (path) {
	            if (!(path instanceof Array)) {
	                path = [path];
	            }
	            var len = path.length;
	            var appendSize = 0;
	            var offset = this._len;
	            for (var i = 0; i < len; i++) {
	                appendSize += path[i].len();
	            }
	            if (hasTypedArray && (this.data instanceof Float32Array)) {
	                this.data = new Float32Array(offset + appendSize);
	            }
	            for (var i = 0; i < len; i++) {
	                var appendPathData = path[i].data;
	                for (var k = 0; k < appendPathData.length; k++) {
	                    this.data[offset++] = appendPathData[k];
	                }
	            }
	            this._len = offset;
	        },

	        /**
	         * æ¿‰î‚¢åŽ– Path éç‰ˆåµéŠ†ï¿½
	         * çä»‹å™ºæ¾¶å¶‡æ•¤é‘°å±¼ç¬‰é¢è™«æ§‘é‚æ‰®æ®‘éæ‰®ç²éŠ†å‚šã‡é–®ã„¥åžŽé¥æƒ§èˆ°é–²å¶‡ç²¯é¨å‹¬å¯šæµ ã‚†æšŸéŽ¹î‡€æš±æ´ï¹‚å…˜é„îˆ™ç¬‰é™æ¨¼æ®‘éŠ†ï¿½
	         */
	        addData: function (cmd) {
	            var data = this.data;
	            if (this._len + arguments.length > data.length) {
	                // é¥çŠ±è´Ÿæ¶”å¬ªå¢ é¨å‹¬æšŸç¼å‹«å‡¡ç¼å¿šæµ†éŽ¹ãˆ¡åžšé—ˆæ¬â‚¬ä½ºæ®‘ Float32Array
	                // éŽµâ‚¬æµ ãƒ¤ç¬‰æ¾¶ç†ºæ•¤éƒå •æ¸¶ç‘•ä½¹å¢¿çžæ›šç«´æ¶“î…æŸŠé¨å‹«å§©éŽ¬ä½¹æšŸç¼ï¿½
	                this._expandData();
	                data = this.data;
	            }
	            for (var i = 0; i < arguments.length; i++) {
	                data[this._len++] = arguments[i];
	            }

	            this._prevCmd = cmd;
	        },

	        _expandData: function () {
	            // Only if data is Float32Array
	            if (!(this.data instanceof Array)) {
	                var newData = [];
	                for (var i = 0; i < this._len; i++) {
	                    newData[i] = this.data[i];
	                }
	                this.data = newData;
	            }
	        },

	        /**
	         * If needs js implemented dashed line
	         * @return {boolean}
	         * @private
	         */
	        _needsDash: function () {
	            return this._lineDash;
	        },

	        _dashedLineTo: function (x1, y1) {
	            var dashSum = this._dashSum;
	            var offset = this._dashOffset;
	            var lineDash = this._lineDash;
	            var ctx = this._ctx;

	            var x0 = this._xi;
	            var y0 = this._yi;
	            var dx = x1 - x0;
	            var dy = y1 - y0;
	            var dist = mathSqrt(dx * dx + dy * dy);
	            var x = x0;
	            var y = y0;
	            var dash;
	            var nDash = lineDash.length;
	            var idx;
	            dx /= dist;
	            dy /= dist;

	            if (offset < 0) {
	                // Convert to positive offset
	                offset = dashSum + offset;
	            }
	            offset %= dashSum;
	            x -= offset * dx;
	            y -= offset * dy;

	            while ((dx > 0 && x <= x1) || (dx < 0 && x >= x1)
	            || (dx == 0 && ((dy > 0 && y <= y1) || (dy < 0 && y >= y1)))) {
	                idx = this._dashIdx;
	                dash = lineDash[idx];
	                x += dx * dash;
	                y += dy * dash;
	                this._dashIdx = (idx + 1) % nDash;
	                // Skip positive offset
	                if ((dx > 0 && x < x0) || (dx < 0 && x > x0) || (dy > 0 && y < y0) || (dy < 0 && y > y0)) {
	                    continue;
	                }
	                ctx[idx % 2 ? 'moveTo' : 'lineTo'](
	                    dx >= 0 ? mathMin(x, x1) : mathMax(x, x1),
	                    dy >= 0 ? mathMin(y, y1) : mathMax(y, y1)
	                );
	            }
	            // Offset for next lineTo
	            dx = x - x1;
	            dy = y - y1;
	            this._dashOffset = -mathSqrt(dx * dx + dy * dy);
	        },

	        // Not accurate dashed line to
	        _dashedBezierTo: function (x1, y1, x2, y2, x3, y3) {
	            var dashSum = this._dashSum;
	            var offset = this._dashOffset;
	            var lineDash = this._lineDash;
	            var ctx = this._ctx;

	            var x0 = this._xi;
	            var y0 = this._yi;
	            var t;
	            var dx;
	            var dy;
	            var cubicAt = curve.cubicAt;
	            var bezierLen = 0;
	            var idx = this._dashIdx;
	            var nDash = lineDash.length;

	            var x;
	            var y;

	            var tmpLen = 0;

	            if (offset < 0) {
	                // Convert to positive offset
	                offset = dashSum + offset;
	            }
	            offset %= dashSum;
	            // Bezier approx length
	            for (t = 0; t < 1; t += 0.1) {
	                dx = cubicAt(x0, x1, x2, x3, t + 0.1)
	                    - cubicAt(x0, x1, x2, x3, t);
	                dy = cubicAt(y0, y1, y2, y3, t + 0.1)
	                    - cubicAt(y0, y1, y2, y3, t);
	                bezierLen += mathSqrt(dx * dx + dy * dy);
	            }

	            // Find idx after add offset
	            for (; idx < nDash; idx++) {
	                tmpLen += lineDash[idx];
	                if (tmpLen > offset) {
	                    break;
	                }
	            }
	            t = (tmpLen - offset) / bezierLen;

	            while (t <= 1) {

	                x = cubicAt(x0, x1, x2, x3, t);
	                y = cubicAt(y0, y1, y2, y3, t);

	                // Use line to approximate dashed bezier
	                // Bad result if dash is long
	                idx % 2 ? ctx.moveTo(x, y)
	                    : ctx.lineTo(x, y);

	                t += lineDash[idx] / bezierLen;

	                idx = (idx + 1) % nDash;
	            }

	            // Finish the last segment and calculate the new offset
	            (idx % 2 !== 0) && ctx.lineTo(x3, y3);
	            dx = x3 - x;
	            dy = y3 - y;
	            this._dashOffset = -mathSqrt(dx * dx + dy * dy);
	        },

	        _dashedQuadraticTo: function (x1, y1, x2, y2) {
	            // Convert quadratic to cubic using degree elevation
	            var x3 = x2;
	            var y3 = y2;
	            x2 = (x2 + 2 * x1) / 3;
	            y2 = (y2 + 2 * y1) / 3;
	            x1 = (this._xi + 2 * x1) / 3;
	            y1 = (this._yi + 2 * y1) / 3;

	            this._dashedBezierTo(x1, y1, x2, y2, x3, y3);
	        },

	        /**
	         * æžî„åžšé—ˆæ¬â‚¬ä½ºæ®‘ Float32Array é‘å¿“çš¯é«å——å”´ç€›æ¨ºå´°é¢ï¿½
	         * Convert dynamic array to static Float32Array
	         */
	        toStatic: function () {
	            var data = this.data;
	            if (data instanceof Array) {
	                data.length = this._len;
	                if (hasTypedArray) {
	                    this.data = new Float32Array(data);
	                }
	            }
	        },

	        /**
	         * @return {module:zrender/core/BoundingRect}
	         */
	        getBoundingRect: function () {
	            min[0] = min[1] = min2[0] = min2[1] = Number.MAX_VALUE;
	            max[0] = max[1] = max2[0] = max2[1] = -Number.MAX_VALUE;

	            var data = this.data;
	            var xi = 0;
	            var yi = 0;
	            var x0 = 0;
	            var y0 = 0;

	            for (var i = 0; i < data.length;) {
	                var cmd = data[i++];

	                if (i == 1) {
	                    // æ¿¡å‚›ç‰ç»—îƒ¿ç«´æ¶“î„æ‡¡æµ ã‚†æ§¸ L, C, Q
	                    // é’ï¿½ previous point éšå²€ç²¯é’è·ºæ‡¡æµ ã‚‡æ®‘ç»—îƒ¿ç«´æ¶“ï¿½ point
	                    //
	                    // ç»—îƒ¿ç«´æ¶“î„æ‡¡æµ ã‚„è´Ÿ Arc é¨å‹¬å„éå…¸ç¬…æµ¼æ°¬æ¹ªéšåº¨æ½°é—è§„ç•©æ¾¶å‹­æ‚Š
	                    xi = data[i];
	                    yi = data[i + 1];

	                    x0 = xi;
	                    y0 = yi;
	                }

	                switch (cmd) {
	                    case CMD.M:
	                        // moveTo é›æˆ’æŠ¤é–²å¶†æŸŠé’æ¶˜ç¼“æ¶“â‚¬æ¶“î…æŸŠé¨ï¿½ subpath, éªžæœµç¬–é‡å­˜æŸŠé‚æ‰®æ®‘ç’§é£Žå£
	                        // é¦ï¿½ closePath é¨å‹¬æ¤‚éŠæ¬Žå¨‡é¢ï¿½
	                        x0 = data[i++];
	                        y0 = data[i++];
	                        xi = x0;
	                        yi = y0;
	                        min2[0] = x0;
	                        min2[1] = y0;
	                        max2[0] = x0;
	                        max2[1] = y0;
	                        break;
	                    case CMD.L:
	                        bbox.fromLine(xi, yi, data[i], data[i + 1], min2, max2);
	                        xi = data[i++];
	                        yi = data[i++];
	                        break;
	                    case CMD.C:
	                        bbox.fromCubic(
	                            xi, yi, data[i++], data[i++], data[i++], data[i++], data[i], data[i + 1],
	                            min2, max2
	                        );
	                        xi = data[i++];
	                        yi = data[i++];
	                        break;
	                    case CMD.Q:
	                        bbox.fromQuadratic(
	                            xi, yi, data[i++], data[i++], data[i], data[i + 1],
	                            min2, max2
	                        );
	                        xi = data[i++];
	                        yi = data[i++];
	                        break;
	                    case CMD.A:
	                        // TODO Arc é’ã‚†æŸ‡é¨å‹«ç´‘é–¿â‚¬å§£æ—‡ç·æ¾¶ï¿½
	                        var cx = data[i++];
	                        var cy = data[i++];
	                        var rx = data[i++];
	                        var ry = data[i++];
	                        var startAngle = data[i++];
	                        var endAngle = data[i++] + startAngle;
	                        // TODO Arc éƒå¬­æµ†
	                        var psi = data[i++];
	                        var anticlockwise = 1 - data[i++];

	                        if (i == 1) {
	                            // é©å­˜å¸´æµ£è·¨æ•¤ arc é›æˆ’æŠ¤
	                            // ç»—îƒ¿ç«´æ¶“î„æ‡¡æµ ã‚ˆæ£éç¡…ç¹•éˆî„ç•¾æ¶”ï¿½
	                            x0 = mathCos(startAngle) * rx + cx;
	                            y0 = mathSin(startAngle) * ry + cy;
	                        }

	                        bbox.fromArc(
	                            cx, cy, rx, ry, startAngle, endAngle,
	                            anticlockwise, min2, max2
	                        );

	                        xi = mathCos(endAngle) * rx + cx;
	                        yi = mathSin(endAngle) * ry + cy;
	                        break;
	                    case CMD.R:
	                        x0 = xi = data[i++];
	                        y0 = yi = data[i++];
	                        var width = data[i++];
	                        var height = data[i++];
	                        // Use fromLine
	                        bbox.fromLine(x0, y0, x0 + width, y0 + height, min2, max2);
	                        break;
	                    case CMD.Z:
	                        xi = x0;
	                        yi = y0;
	                        break;
	                }

	                // Union
	                vec2.min(min, min, min2);
	                vec2.max(max, max, max2);
	            }

	            // No data
	            if (i === 0) {
	                min[0] = min[1] = max[0] = max[1] = 0;
	            }

	            return new BoundingRect(
	                min[0], min[1], max[0] - min[0], max[1] - min[1]
	            );
	        },

	        /**
	         * Rebuild path from current data
	         * Rebuild path will not consider javascript implemented line dash.
	         * @param {CanvasRenderingContext} ctx
	         */
	        rebuildPath: function (ctx) {
	            var d = this.data;
	            var x0, y0;
	            var xi, yi;
	            var x, y;
	            var ux = this._ux;
	            var uy = this._uy;
	            var len = this._len;
	            for (var i = 0; i < len;) {
	                var cmd = d[i++];

	                if (i == 1) {
	                    // æ¿¡å‚›ç‰ç»—îƒ¿ç«´æ¶“î„æ‡¡æµ ã‚†æ§¸ L, C, Q
	                    // é’ï¿½ previous point éšå²€ç²¯é’è·ºæ‡¡æµ ã‚‡æ®‘ç»—îƒ¿ç«´æ¶“ï¿½ point
	                    //
	                    // ç»—îƒ¿ç«´æ¶“î„æ‡¡æµ ã‚„è´Ÿ Arc é¨å‹¬å„éå…¸ç¬…æµ¼æ°¬æ¹ªéšåº¨æ½°é—è§„ç•©æ¾¶å‹­æ‚Š
	                    xi = d[i];
	                    yi = d[i + 1];

	                    x0 = xi;
	                    y0 = yi;
	                }
	                switch (cmd) {
	                    case CMD.M:
	                        x0 = xi = d[i++];
	                        y0 = yi = d[i++];
	                        ctx.moveTo(xi, yi);
	                        break;
	                    case CMD.L:
	                        x = d[i++];
	                        y = d[i++];
	                        // Not draw too small seg between
	                        if (mathAbs(x - xi) > ux || mathAbs(y - yi) > uy || i === len - 1) {
	                            ctx.lineTo(x, y);
	                            xi = x;
	                            yi = y;
	                        }
	                        break;
	                    case CMD.C:
	                        ctx.bezierCurveTo(
	                            d[i++], d[i++], d[i++], d[i++], d[i++], d[i++]
	                        );
	                        xi = d[i - 2];
	                        yi = d[i - 1];
	                        break;
	                    case CMD.Q:
	                        ctx.quadraticCurveTo(d[i++], d[i++], d[i++], d[i++]);
	                        xi = d[i - 2];
	                        yi = d[i - 1];
	                        break;
	                    case CMD.A:
	                        var cx = d[i++];
	                        var cy = d[i++];
	                        var rx = d[i++];
	                        var ry = d[i++];
	                        var theta = d[i++];
	                        var dTheta = d[i++];
	                        var psi = d[i++];
	                        var fs = d[i++];
	                        var r = (rx > ry) ? rx : ry;
	                        var scaleX = (rx > ry) ? 1 : rx / ry;
	                        var scaleY = (rx > ry) ? ry / rx : 1;
	                        var isEllipse = Math.abs(rx - ry) > 1e-3;
	                        var endAngle = theta + dTheta;
	                        if (isEllipse) {
	                            ctx.translate(cx, cy);
	                            ctx.rotate(psi);
	                            ctx.scale(scaleX, scaleY);
	                            ctx.arc(0, 0, r, theta, endAngle, 1 - fs);
	                            ctx.scale(1 / scaleX, 1 / scaleY);
	                            ctx.rotate(-psi);
	                            ctx.translate(-cx, -cy);
	                        }
	                        else {
	                            ctx.arc(cx, cy, r, theta, endAngle, 1 - fs);
	                        }

	                        if (i == 1) {
	                            // é©å­˜å¸´æµ£è·¨æ•¤ arc é›æˆ’æŠ¤
	                            // ç»—îƒ¿ç«´æ¶“î„æ‡¡æµ ã‚ˆæ£éç¡…ç¹•éˆî„ç•¾æ¶”ï¿½
	                            x0 = mathCos(theta) * rx + cx;
	                            y0 = mathSin(theta) * ry + cy;
	                        }
	                        xi = mathCos(endAngle) * rx + cx;
	                        yi = mathSin(endAngle) * ry + cy;
	                        break;
	                    case CMD.R:
	                        x0 = xi = d[i];
	                        y0 = yi = d[i + 1];
	                        ctx.rect(d[i++], d[i++], d[i++], d[i++]);
	                        break;
	                    case CMD.Z:
	                        ctx.closePath();
	                        xi = x0;
	                        yi = y0;
	                }
	            }
	        }
	    };

	    PathProxy.CMD = CMD;

	    module.exports = PathProxy;


/***/ },
/* 30 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	/**
	 * é‡èŒ¬åšŽæˆå‘­å§ªå¦¯â€³æ½¡
	 * @module zrender/core/curve
	 * @author pissang(https://www.github.com/pissang)
	 */


	    var vec2 = __webpack_require__(18);
	    var v2Create = vec2.create;
	    var v2DistSquare = vec2.distSquare;
	    var mathPow = Math.pow;
	    var mathSqrt = Math.sqrt;

	    var EPSILON = 1e-8;
	    var EPSILON_NUMERIC = 1e-4;

	    var THREE_SQRT = mathSqrt(3);
	    var ONE_THIRD = 1 / 3;

	    // æ¶“å­˜æ¤‚é™æ©€å™º
	    var _v0 = v2Create();
	    var _v1 = v2Create();
	    var _v2 = v2Create();
	    // var _v3 = vec2.create();

	    function isAroundZero(val) {
	        return val > -EPSILON && val < EPSILON;
	    }
	    function isNotAroundZero(val) {
	        return val > EPSILON || val < -EPSILON;
	    }
	    /**
	     * ç’ï¼„ç•»æ¶“å¤‹î‚¼ç’æ¿†î”£çæ–¿â‚¬ï¿½
	     * @memberOf module:zrender/core/curve
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @param  {number} p3
	     * @param  {number} t
	     * @return {number}
	     */
	    function cubicAt(p0, p1, p2, p3, t) {
	        var onet = 1 - t;
	        return onet * onet * (onet * p0 + 3 * t * p1)
	             + t * t * (t * p3 + 3 * onet * p2);
	    }

	    /**
	     * ç’ï¼„ç•»æ¶“å¤‹î‚¼ç’æ¿†î”£çæ–¿î‡±éæ¿â‚¬ï¿½
	     * @memberOf module:zrender/core/curve
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @param  {number} p3
	     * @param  {number} t
	     * @return {number}
	     */
	    function cubicDerivativeAt(p0, p1, p2, p3, t) {
	        var onet = 1 - t;
	        return 3 * (
	            ((p1 - p0) * onet + 2 * (p2 - p1) * t) * onet
	            + (p3 - p2) * t * t
	        );
	    }

	    /**
	     * ç’ï¼„ç•»æ¶“å¤‹î‚¼ç’æ¿†î”£çæ—€æŸŸç»‹å¬«ç‰´é”›å±¼å¨‡é¢ã„§æ´“é–²æˆå•å¯®ï¿½
	     * @memberOf module:zrender/core/curve
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @param  {number} p3
	     * @param  {number} val
	     * @param  {Array.<number>} roots
	     * @return {number} éˆå¤‹æ™¥éè§„æšŸé©ï¿½
	     */
	    function cubicRootAt(p0, p1, p2, p3, val, roots) {
	        // Evaluate roots of cubic functions
	        var a = p3 + 3 * (p1 - p2) - p0;
	        var b = 3 * (p2 - p1 * 2 + p0);
	        var c = 3 * (p1  - p0);
	        var d = p0 - val;

	        var A = b * b - 3 * a * c;
	        var B = b * c - 9 * a * d;
	        var C = c * c - 3 * b * d;

	        var n = 0;

	        if (isAroundZero(A) && isAroundZero(B)) {
	            if (isAroundZero(b)) {
	                roots[0] = 0;
	            }
	            else {
	                var t1 = -c / b;  //t1, t2, t3, b is not zero
	                if (t1 >= 0 && t1 <= 1) {
	                    roots[n++] = t1;
	                }
	            }
	        }
	        else {
	            var disc = B * B - 4 * A * C;

	            if (isAroundZero(disc)) {
	                var K = B / A;
	                var t1 = -b / a + K;  // t1, a is not zero
	                var t2 = -K / 2;  // t2, t3
	                if (t1 >= 0 && t1 <= 1) {
	                    roots[n++] = t1;
	                }
	                if (t2 >= 0 && t2 <= 1) {
	                    roots[n++] = t2;
	                }
	            }
	            else if (disc > 0) {
	                var discSqrt = mathSqrt(disc);
	                var Y1 = A * b + 1.5 * a * (-B + discSqrt);
	                var Y2 = A * b + 1.5 * a * (-B - discSqrt);
	                if (Y1 < 0) {
	                    Y1 = -mathPow(-Y1, ONE_THIRD);
	                }
	                else {
	                    Y1 = mathPow(Y1, ONE_THIRD);
	                }
	                if (Y2 < 0) {
	                    Y2 = -mathPow(-Y2, ONE_THIRD);
	                }
	                else {
	                    Y2 = mathPow(Y2, ONE_THIRD);
	                }
	                var t1 = (-b - (Y1 + Y2)) / (3 * a);
	                if (t1 >= 0 && t1 <= 1) {
	                    roots[n++] = t1;
	                }
	            }
	            else {
	                var T = (2 * A * b - 3 * a * B) / (2 * mathSqrt(A * A * A));
	                var theta = Math.acos(T) / 3;
	                var ASqrt = mathSqrt(A);
	                var tmp = Math.cos(theta);

	                var t1 = (-b - 2 * ASqrt * tmp) / (3 * a);
	                var t2 = (-b + ASqrt * (tmp + THREE_SQRT * Math.sin(theta))) / (3 * a);
	                var t3 = (-b + ASqrt * (tmp - THREE_SQRT * Math.sin(theta))) / (3 * a);
	                if (t1 >= 0 && t1 <= 1) {
	                    roots[n++] = t1;
	                }
	                if (t2 >= 0 && t2 <= 1) {
	                    roots[n++] = t2;
	                }
	                if (t3 >= 0 && t3 <= 1) {
	                    roots[n++] = t3;
	                }
	            }
	        }
	        return n;
	    }

	    /**
	     * ç’ï¼„ç•»æ¶“å¤‹î‚¼ç’æ¿†î”£çæ—€æŸŸç»‹å¬«ç€¬é—„æ„¬â‚¬è‚©æ®‘æµ£å¶‡ç–†
	     * @memberOf module:zrender/core/curve
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @param  {number} p3
	     * @param  {Array.<number>} extrema
	     * @return {number} éˆå¤‹æ™¥éæ‰®æ´°
	     */
	    function cubicExtrema(p0, p1, p2, p3, extrema) {
	        var b = 6 * p2 - 12 * p1 + 6 * p0;
	        var a = 9 * p1 + 3 * p3 - 3 * p0 - 9 * p2;
	        var c = 3 * p1 - 3 * p0;

	        var n = 0;
	        if (isAroundZero(a)) {
	            if (isNotAroundZero(b)) {
	                var t1 = -c / b;
	                if (t1 >= 0 && t1 <=1) {
	                    extrema[n++] = t1;
	                }
	            }
	        }
	        else {
	            var disc = b * b - 4 * a * c;
	            if (isAroundZero(disc)) {
	                extrema[0] = -b / (2 * a);
	            }
	            else if (disc > 0) {
	                var discSqrt = mathSqrt(disc);
	                var t1 = (-b + discSqrt) / (2 * a);
	                var t2 = (-b - discSqrt) / (2 * a);
	                if (t1 >= 0 && t1 <= 1) {
	                    extrema[n++] = t1;
	                }
	                if (t2 >= 0 && t2 <= 1) {
	                    extrema[n++] = t2;
	                }
	            }
	        }
	        return n;
	    }

	    /**
	     * ç¼å——åžŽæ¶“å¤‹î‚¼ç’æ¿†î”£çæ—€æ´¸ç»¾ï¿½
	     * @memberOf module:zrender/core/curve
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @param  {number} p3
	     * @param  {number} t
	     * @param  {Array.<number>} out
	     */
	    function cubicSubdivide(p0, p1, p2, p3, t, out) {
	        var p01 = (p1 - p0) * t + p0;
	        var p12 = (p2 - p1) * t + p1;
	        var p23 = (p3 - p2) * t + p2;

	        var p012 = (p12 - p01) * t + p01;
	        var p123 = (p23 - p12) * t + p12;

	        var p0123 = (p123 - p012) * t + p012;
	        // Seg0
	        out[0] = p0;
	        out[1] = p01;
	        out[2] = p012;
	        out[3] = p0123;
	        // Seg1
	        out[4] = p0123;
	        out[5] = p123;
	        out[6] = p23;
	        out[7] = p3;
	    }

	    /**
	     * éŽ¶æ›žçš éç‘°åŸŒæ¶“å¤‹î‚¼ç’æ¿†î”£çæ—€æ´¸ç»¾å¤¸ç¬‚é”›å²ƒç¹‘é¥ç‚´å§‡çå‹®çª›ç»‚æ±‡â‚¬ï¿½
	     * éŽ¶æ›žçš éè§„æ¹é™îˆå…˜æµ¼æ°­æ¹æ¶“â‚¬æ¶“î…åž¨é‘°å‘­î˜¿æ¶“îŽç´æ©æ¬“å™·é™î‡ç¹‘é¥ç‚²å¾æ¶“î…¡çª›ç»‚ç»˜æ¸¶é­î… æ®‘æ¶“â‚¬æ¶“î‚â‚¬ï¿½
	     * @param {number} x0
	     * @param {number} y0
	     * @param {number} x1
	     * @param {number} y1
	     * @param {number} x2
	     * @param {number} y2
	     * @param {number} x3
	     * @param {number} y3
	     * @param {number} x
	     * @param {number} y
	     * @param {Array.<number>} [out] éŽ¶æ›žçš éï¿½
	     * @return {number}
	     */
	    function cubicProjectPoint(
	        x0, y0, x1, y1, x2, y2, x3, y3,
	        x, y, out
	    ) {
	        // http://pomax.github.io/bezierinfo/#projections
	        var t;
	        var interval = 0.005;
	        var d = Infinity;
	        var prev;
	        var next;
	        var d1;
	        var d2;

	        _v0[0] = x;
	        _v0[1] = y;

	        // éå ¢çŸ–é£ãƒ¤åŠç’â€²ç«´æ¶“å¬ªå½²é‘³ç•Œæ®‘éˆâ‚¬çå¿šçª›ç»‚è¤æ®‘ t éŠï¿½
	        // PENDING
	        for (var _t = 0; _t < 1; _t += 0.05) {
	            _v1[0] = cubicAt(x0, x1, x2, x3, _t);
	            _v1[1] = cubicAt(y0, y1, y2, y3, _t);
	            d1 = v2DistSquare(_v0, _v1);
	            if (d1 < d) {
	                t = _t;
	                d = d1;
	            }
	        }
	        d = Infinity;

	        // At most 32 iteration
	        for (var i = 0; i < 32; i++) {
	            if (interval < EPSILON_NUMERIC) {
	                break;
	            }
	            prev = t - interval;
	            next = t + interval;
	            // t - interval
	            _v1[0] = cubicAt(x0, x1, x2, x3, prev);
	            _v1[1] = cubicAt(y0, y1, y2, y3, prev);

	            d1 = v2DistSquare(_v1, _v0);

	            if (prev >= 0 && d1 < d) {
	                t = prev;
	                d = d1;
	            }
	            else {
	                // t + interval
	                _v2[0] = cubicAt(x0, x1, x2, x3, next);
	                _v2[1] = cubicAt(y0, y1, y2, y3, next);
	                d2 = v2DistSquare(_v2, _v0);

	                if (next <= 1 && d2 < d) {
	                    t = next;
	                    d = d2;
	                }
	                else {
	                    interval *= 0.5;
	                }
	            }
	        }
	        // t
	        if (out) {
	            out[0] = cubicAt(x0, x1, x2, x3, t);
	            out[1] = cubicAt(y0, y1, y2, y3, t);
	        }
	        // console.log(interval, i);
	        return mathSqrt(d);
	    }

	    /**
	     * ç’ï¼„ç•»æµœå±¾î‚¼é‚ç¡…ç¤‰æ¿‰ç‚²çšµéŠï¿½
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @param  {number} t
	     * @return {number}
	     */
	    function quadraticAt(p0, p1, p2, t) {
	        var onet = 1 - t;
	        return onet * (onet * p0 + 2 * t * p1) + t * t * p2;
	    }

	    /**
	     * ç’ï¼„ç•»æµœå±¾î‚¼é‚ç¡…ç¤‰æ¿‰ç‚²çšµç€µå…¼æšŸéŠï¿½
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @param  {number} t
	     * @return {number}
	     */
	    function quadraticDerivativeAt(p0, p1, p2, t) {
	        return 2 * ((1 - t) * (p1 - p0) + t * (p2 - p1));
	    }

	    /**
	     * ç’ï¼„ç•»æµœå±¾î‚¼é‚ç¡…ç¤‰æ¿‰ç‚²çšµé‚åœ­â–¼éï¿½
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @param  {number} t
	     * @param  {Array.<number>} roots
	     * @return {number} éˆå¤‹æ™¥éè§„æšŸé©ï¿½
	     */
	    function quadraticRootAt(p0, p1, p2, val, roots) {
	        var a = p0 - 2 * p1 + p2;
	        var b = 2 * (p1 - p0);
	        var c = p0 - val;

	        var n = 0;
	        if (isAroundZero(a)) {
	            if (isNotAroundZero(b)) {
	                var t1 = -c / b;
	                if (t1 >= 0 && t1 <= 1) {
	                    roots[n++] = t1;
	                }
	            }
	        }
	        else {
	            var disc = b * b - 4 * a * c;
	            if (isAroundZero(disc)) {
	                var t1 = -b / (2 * a);
	                if (t1 >= 0 && t1 <= 1) {
	                    roots[n++] = t1;
	                }
	            }
	            else if (disc > 0) {
	                var discSqrt = mathSqrt(disc);
	                var t1 = (-b + discSqrt) / (2 * a);
	                var t2 = (-b - discSqrt) / (2 * a);
	                if (t1 >= 0 && t1 <= 1) {
	                    roots[n++] = t1;
	                }
	                if (t2 >= 0 && t2 <= 1) {
	                    roots[n++] = t2;
	                }
	            }
	        }
	        return n;
	    }

	    /**
	     * ç’ï¼„ç•»æµœå±¾î‚¼ç’æ¿†î”£çæ—€æŸŸç»‹å¬«ç€¬é—„æ„¬â‚¬ï¿½
	     * @memberOf module:zrender/core/curve
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @return {number}
	     */
	    function quadraticExtremum(p0, p1, p2) {
	        var divider = p0 + p2 - 2 * p1;
	        if (divider === 0) {
	            // p1 is center of p0 and p2
	            return 0.5;
	        }
	        else {
	            return (p0 - p1) / divider;
	        }
	    }

	    /**
	     * ç¼å——åžŽæµœå±¾î‚¼ç’æ¿†î”£çæ—€æ´¸ç»¾ï¿½
	     * @memberOf module:zrender/core/curve
	     * @param  {number} p0
	     * @param  {number} p1
	     * @param  {number} p2
	     * @param  {number} t
	     * @param  {Array.<number>} out
	     */
	    function quadraticSubdivide(p0, p1, p2, t, out) {
	        var p01 = (p1 - p0) * t + p0;
	        var p12 = (p2 - p1) * t + p1;
	        var p012 = (p12 - p01) * t + p01;

	        // Seg0
	        out[0] = p0;
	        out[1] = p01;
	        out[2] = p012;

	        // Seg1
	        out[3] = p012;
	        out[4] = p12;
	        out[5] = p2;
	    }

	    /**
	     * éŽ¶æ›žçš éç‘°åŸŒæµœå±¾î‚¼ç’æ¿†î”£çæ—€æ´¸ç»¾å¤¸ç¬‚é”›å²ƒç¹‘é¥ç‚´å§‡çå‹®çª›ç»‚æ±‡â‚¬ï¿½
	     * éŽ¶æ›žçš éè§„æ¹é™îˆå…˜æµ¼æ°­æ¹æ¶“â‚¬æ¶“î…åž¨é‘°å‘­î˜¿æ¶“îŽç´æ©æ¬“å™·é™î‡ç¹‘é¥ç‚²å¾æ¶“î…¡çª›ç»‚ç»˜æ¸¶é­î… æ®‘æ¶“â‚¬æ¶“î‚â‚¬ï¿½
	     * @param {number} x0
	     * @param {number} y0
	     * @param {number} x1
	     * @param {number} y1
	     * @param {number} x2
	     * @param {number} y2
	     * @param {number} x
	     * @param {number} y
	     * @param {Array.<number>} out éŽ¶æ›žçš éï¿½
	     * @return {number}
	     */
	    function quadraticProjectPoint(
	        x0, y0, x1, y1, x2, y2,
	        x, y, out
	    ) {
	        // http://pomax.github.io/bezierinfo/#projections
	        var t;
	        var interval = 0.005;
	        var d = Infinity;

	        _v0[0] = x;
	        _v0[1] = y;

	        // éå ¢çŸ–é£ãƒ¤åŠç’â€²ç«´æ¶“å¬ªå½²é‘³ç•Œæ®‘éˆâ‚¬çå¿šçª›ç»‚è¤æ®‘ t éŠï¿½
	        // PENDING
	        for (var _t = 0; _t < 1; _t += 0.05) {
	            _v1[0] = quadraticAt(x0, x1, x2, _t);
	            _v1[1] = quadraticAt(y0, y1, y2, _t);
	            var d1 = v2DistSquare(_v0, _v1);
	            if (d1 < d) {
	                t = _t;
	                d = d1;
	            }
	        }
	        d = Infinity;

	        // At most 32 iteration
	        for (var i = 0; i < 32; i++) {
	            if (interval < EPSILON_NUMERIC) {
	                break;
	            }
	            var prev = t - interval;
	            var next = t + interval;
	            // t - interval
	            _v1[0] = quadraticAt(x0, x1, x2, prev);
	            _v1[1] = quadraticAt(y0, y1, y2, prev);

	            var d1 = v2DistSquare(_v1, _v0);

	            if (prev >= 0 && d1 < d) {
	                t = prev;
	                d = d1;
	            }
	            else {
	                // t + interval
	                _v2[0] = quadraticAt(x0, x1, x2, next);
	                _v2[1] = quadraticAt(y0, y1, y2, next);
	                var d2 = v2DistSquare(_v2, _v0);
	                if (next <= 1 && d2 < d) {
	                    t = next;
	                    d = d2;
	                }
	                else {
	                    interval *= 0.5;
	                }
	            }
	        }
	        // t
	        if (out) {
	            out[0] = quadraticAt(x0, x1, x2, t);
	            out[1] = quadraticAt(y0, y1, y2, t);
	        }
	        // console.log(interval, i);
	        return mathSqrt(d);
	    }

	    module.exports = {

	        cubicAt: cubicAt,

	        cubicDerivativeAt: cubicDerivativeAt,

	        cubicRootAt: cubicRootAt,

	        cubicExtrema: cubicExtrema,

	        cubicSubdivide: cubicSubdivide,

	        cubicProjectPoint: cubicProjectPoint,

	        quadraticAt: quadraticAt,

	        quadraticDerivativeAt: quadraticDerivativeAt,

	        quadraticRootAt: quadraticRootAt,

	        quadraticExtremum: quadraticExtremum,

	        quadraticSubdivide: quadraticSubdivide,

	        quadraticProjectPoint: quadraticProjectPoint
	    };


/***/ },
/* 31 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * @author Yi Shen(https://github.com/pissang)
	 */


	    var vec2 = __webpack_require__(18);
	    var curve = __webpack_require__(30);

	    var bbox = {};
	    var mathMin = Math.min;
	    var mathMax = Math.max;
	    var mathSin = Math.sin;
	    var mathCos = Math.cos;

	    var start = vec2.create();
	    var end = vec2.create();
	    var extremity = vec2.create();

	    var PI2 = Math.PI * 2;
	    /**
	     * æµ åº¨ã€Šéè§„æšŸç¼å‹ªè…‘ç’ï¼„ç•»é‘çƒ˜æ¸¶çå¿“å¯˜é¥å¯¸æ´…é”›å±½å•“éî™¦min`éœå®max`æ¶“ï¿½
	     * @module zrender/core/bbox
	     * @param {Array<Object>} points æ¤¤å‰å£éæ‰®ç²
	     * @param {number} min
	     * @param {number} max
	     */
	    bbox.fromPoints = function(points, min, max) {
	        if (points.length === 0) {
	            return;
	        }
	        var p = points[0];
	        var left = p[0];
	        var right = p[0];
	        var top = p[1];
	        var bottom = p[1];
	        var i;

	        for (i = 1; i < points.length; i++) {
	            p = points[i];
	            left = mathMin(left, p[0]);
	            right = mathMax(right, p[0]);
	            top = mathMin(top, p[1]);
	            bottom = mathMax(bottom, p[1]);
	        }

	        min[0] = left;
	        min[1] = top;
	        max[0] = right;
	        max[1] = bottom;
	    };

	    /**
	     * @memberOf module:zrender/core/bbox
	     * @param {number} x0
	     * @param {number} y0
	     * @param {number} x1
	     * @param {number} y1
	     * @param {Array.<number>} min
	     * @param {Array.<number>} max
	     */
	    bbox.fromLine = function (x0, y0, x1, y1, min, max) {
	        min[0] = mathMin(x0, x1);
	        min[1] = mathMin(y0, y1);
	        max[0] = mathMax(x0, x1);
	        max[1] = mathMax(y0, y1);
	    };

	    var xDim = [];
	    var yDim = [];
	    /**
	     * æµ åºç¬é—ƒæƒ°ç¤‰æ¿‰ç‚²çšµé‡èŒ¬åšŽ(p0, p1, p2, p3)æ¶“î…¡î…¸ç» æ¥€åš­éˆâ‚¬çå¿“å¯˜é¥å¯¸æ´…é”›å±½å•“éî™¦min`éœå®max`æ¶“ï¿½
	     * @memberOf module:zrender/core/bbox
	     * @param {number} x0
	     * @param {number} y0
	     * @param {number} x1
	     * @param {number} y1
	     * @param {number} x2
	     * @param {number} y2
	     * @param {number} x3
	     * @param {number} y3
	     * @param {Array.<number>} min
	     * @param {Array.<number>} max
	     */
	    bbox.fromCubic = function(
	        x0, y0, x1, y1, x2, y2, x3, y3, min, max
	    ) {
	        var cubicExtrema = curve.cubicExtrema;
	        var cubicAt = curve.cubicAt;
	        var i;
	        var n = cubicExtrema(x0, x1, x2, x3, xDim);
	        min[0] = Infinity;
	        min[1] = Infinity;
	        max[0] = -Infinity;
	        max[1] = -Infinity;

	        for (i = 0; i < n; i++) {
	            var x = cubicAt(x0, x1, x2, x3, xDim[i]);
	            min[0] = mathMin(x, min[0]);
	            max[0] = mathMax(x, max[0]);
	        }
	        n = cubicExtrema(y0, y1, y2, y3, yDim);
	        for (i = 0; i < n; i++) {
	            var y = cubicAt(y0, y1, y2, y3, yDim[i]);
	            min[1] = mathMin(y, min[1]);
	            max[1] = mathMax(y, max[1]);
	        }

	        min[0] = mathMin(x0, min[0]);
	        max[0] = mathMax(x0, max[0]);
	        min[0] = mathMin(x3, min[0]);
	        max[0] = mathMax(x3, max[0]);

	        min[1] = mathMin(y0, min[1]);
	        max[1] = mathMax(y0, max[1]);
	        min[1] = mathMin(y3, min[1]);
	        max[1] = mathMax(y3, max[1]);
	    };

	    /**
	     * æµ åºç°©é—ƒæƒ°ç¤‰æ¿‰ç‚²çšµé‡èŒ¬åšŽ(p0, p1, p2)æ¶“î…¡î…¸ç» æ¥€åš­éˆâ‚¬çå¿“å¯˜é¥å¯¸æ´…é”›å±½å•“éî™¦min`éœå®max`æ¶“ï¿½
	     * @memberOf module:zrender/core/bbox
	     * @param {number} x0
	     * @param {number} y0
	     * @param {number} x1
	     * @param {number} y1
	     * @param {number} x2
	     * @param {number} y2
	     * @param {Array.<number>} min
	     * @param {Array.<number>} max
	     */
	    bbox.fromQuadratic = function(x0, y0, x1, y1, x2, y2, min, max) {
	        var quadraticExtremum = curve.quadraticExtremum;
	        var quadraticAt = curve.quadraticAt;
	        // Find extremities, where derivative in x dim or y dim is zero
	        var tx =
	            mathMax(
	                mathMin(quadraticExtremum(x0, x1, x2), 1), 0
	            );
	        var ty =
	            mathMax(
	                mathMin(quadraticExtremum(y0, y1, y2), 1), 0
	            );

	        var x = quadraticAt(x0, x1, x2, tx);
	        var y = quadraticAt(y0, y1, y2, ty);

	        min[0] = mathMin(x0, x2, x);
	        min[1] = mathMin(y0, y2, y);
	        max[0] = mathMax(x0, x2, x);
	        max[1] = mathMax(y0, y2, y);
	    };

	    /**
	     * æµ åº¡æ¸¾å¯®Ñ‚è…‘ç’ï¼„ç•»é‘çƒ˜æ¸¶çå¿“å¯˜é¥å¯¸æ´…é”›å±½å•“éî™¦min`éœå®max`æ¶“ï¿½
	     * @method
	     * @memberOf module:zrender/core/bbox
	     * @param {number} x
	     * @param {number} y
	     * @param {number} rx
	     * @param {number} ry
	     * @param {number} startAngle
	     * @param {number} endAngle
	     * @param {number} anticlockwise
	     * @param {Array.<number>} min
	     * @param {Array.<number>} max
	     */
	    bbox.fromArc = function (
	        x, y, rx, ry, startAngle, endAngle, anticlockwise, min, max
	    ) {
	        var vec2Min = vec2.min;
	        var vec2Max = vec2.max;

	        var diff = Math.abs(startAngle - endAngle);


	        if (diff % PI2 < 1e-4 && diff > 1e-4) {
	            // Is a circle
	            min[0] = x - rx;
	            min[1] = y - ry;
	            max[0] = x + rx;
	            max[1] = y + ry;
	            return;
	        }

	        start[0] = mathCos(startAngle) * rx + x;
	        start[1] = mathSin(startAngle) * ry + y;

	        end[0] = mathCos(endAngle) * rx + x;
	        end[1] = mathSin(endAngle) * ry + y;

	        vec2Min(min, start, end);
	        vec2Max(max, start, end);

	        // Thresh to [0, Math.PI * 2]
	        startAngle = startAngle % (PI2);
	        if (startAngle < 0) {
	            startAngle = startAngle + PI2;
	        }
	        endAngle = endAngle % (PI2);
	        if (endAngle < 0) {
	            endAngle = endAngle + PI2;
	        }

	        if (startAngle > endAngle && !anticlockwise) {
	            endAngle += PI2;
	        }
	        else if (startAngle < endAngle && anticlockwise) {
	            startAngle += PI2;
	        }
	        if (anticlockwise) {
	            var tmp = endAngle;
	            endAngle = startAngle;
	            startAngle = tmp;
	        }

	        // var number = 0;
	        // var step = (anticlockwise ? -Math.PI : Math.PI) / 2;
	        for (var angle = 0; angle < endAngle; angle += Math.PI / 2) {
	            if (angle > startAngle) {
	                extremity[0] = mathCos(angle) * rx + x;
	                extremity[1] = mathSin(angle) * ry + y;

	                vec2Min(min, extremity, min);
	                vec2Max(max, extremity, max);
	            }
	        }
	    };

	    module.exports = bbox;



/***/ },
/* 32 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';


	    var CMD = __webpack_require__(29).CMD;
	    var line = __webpack_require__(33);
	    var cubic = __webpack_require__(34);
	    var quadratic = __webpack_require__(35);
	    var arc = __webpack_require__(36);
	    var normalizeRadian = __webpack_require__(37).normalizeRadian;
	    var curve = __webpack_require__(30);

	    var windingLine = __webpack_require__(38);

	    var containStroke = line.containStroke;

	    var PI2 = Math.PI * 2;

	    var EPSILON = 1e-4;

	    function isAroundEqual(a, b) {
	        return Math.abs(a - b) < EPSILON;
	    }

	    // æ¶“å­˜æ¤‚éæ‰®ç²
	    var roots = [-1, -1, -1];
	    var extrema = [-1, -1];

	    function swapExtrema() {
	        var tmp = extrema[0];
	        extrema[0] = extrema[1];
	        extrema[1] = tmp;
	    }

	    function windingCubic(x0, y0, x1, y1, x2, y2, x3, y3, x, y) {
	        // Quick reject
	        if (
	            (y > y0 && y > y1 && y > y2 && y > y3)
	            || (y < y0 && y < y1 && y < y2 && y < y3)
	        ) {
	            return 0;
	        }
	        var nRoots = curve.cubicRootAt(y0, y1, y2, y3, y, roots);
	        if (nRoots === 0) {
	            return 0;
	        }
	        else {
	            var w = 0;
	            var nExtrema = -1;
	            var y0_, y1_;
	            for (var i = 0; i < nRoots; i++) {
	                var t = roots[i];

	                // Avoid winding error when intersection point is the connect point of two line of polygon
	                var unit = (t === 0 || t === 1) ? 0.5 : 1;

	                var x_ = curve.cubicAt(x0, x1, x2, x3, t);
	                if (x_ < x) { // Quick reject
	                    continue;
	                }
	                if (nExtrema < 0) {
	                    nExtrema = curve.cubicExtrema(y0, y1, y2, y3, extrema);
	                    if (extrema[1] < extrema[0] && nExtrema > 1) {
	                        swapExtrema();
	                    }
	                    y0_ = curve.cubicAt(y0, y1, y2, y3, extrema[0]);
	                    if (nExtrema > 1) {
	                        y1_ = curve.cubicAt(y0, y1, y2, y3, extrema[1]);
	                    }
	                }
	                if (nExtrema == 2) {
	                    // é’å—˜åžšæ¶“å¤‹î†Œé—æ›¡çšŸé‘èŠ¥æšŸ
	                    if (t < extrema[0]) {
	                        w += y0_ < y0 ? unit : -unit;
	                    }
	                    else if (t < extrema[1]) {
	                        w += y1_ < y0_ ? unit : -unit;
	                    }
	                    else {
	                        w += y3 < y1_ ? unit : -unit;
	                    }
	                }
	                else {
	                    // é’å—˜åžšæ¶“ã‚†î†Œé—æ›¡çšŸé‘èŠ¥æšŸ
	                    if (t < extrema[0]) {
	                        w += y0_ < y0 ? unit : -unit;
	                    }
	                    else {
	                        w += y3 < y0_ ? unit : -unit;
	                    }
	                }
	            }
	            return w;
	        }
	    }

	    function windingQuadratic(x0, y0, x1, y1, x2, y2, x, y) {
	        // Quick reject
	        if (
	            (y > y0 && y > y1 && y > y2)
	            || (y < y0 && y < y1 && y < y2)
	        ) {
	            return 0;
	        }
	        var nRoots = curve.quadraticRootAt(y0, y1, y2, y, roots);
	        if (nRoots === 0) {
	            return 0;
	        }
	        else {
	            var t = curve.quadraticExtremum(y0, y1, y2);
	            if (t >= 0 && t <= 1) {
	                var w = 0;
	                var y_ = curve.quadraticAt(y0, y1, y2, t);
	                for (var i = 0; i < nRoots; i++) {
	                    // Remove one endpoint.
	                    var unit = (roots[i] === 0 || roots[i] === 1) ? 0.5 : 1;

	                    var x_ = curve.quadraticAt(x0, x1, x2, roots[i]);
	                    if (x_ < x) {   // Quick reject
	                        continue;
	                    }
	                    if (roots[i] < t) {
	                        w += y_ < y0 ? unit : -unit;
	                    }
	                    else {
	                        w += y2 < y_ ? unit : -unit;
	                    }
	                }
	                return w;
	            }
	            else {
	                // Remove one endpoint.
	                var unit = (roots[0] === 0 || roots[0] === 1) ? 0.5 : 1;

	                var x_ = curve.quadraticAt(x0, x1, x2, roots[0]);
	                if (x_ < x) {   // Quick reject
	                    return 0;
	                }
	                return y2 < y0 ? unit : -unit;
	            }
	        }
	    }

	    // TODO
	    // Arc éƒå¬­æµ†
	    function windingArc(
	        cx, cy, r, startAngle, endAngle, anticlockwise, x, y
	    ) {
	        y -= cy;
	        if (y > r || y < -r) {
	            return 0;
	        }
	        var tmp = Math.sqrt(r * r - y * y);
	        roots[0] = -tmp;
	        roots[1] = tmp;

	        var diff = Math.abs(startAngle - endAngle);
	        if (diff < 1e-4) {
	            return 0;
	        }
	        if (diff % PI2 < 1e-4) {
	            // Is a circle
	            startAngle = 0;
	            endAngle = PI2;
	            var dir = anticlockwise ? 1 : -1;
	            if (x >= roots[0] + cx && x <= roots[1] + cx) {
	                return dir;
	            } else {
	                return 0;
	            }
	        }

	        if (anticlockwise) {
	            var tmp = startAngle;
	            startAngle = normalizeRadian(endAngle);
	            endAngle = normalizeRadian(tmp);
	        }
	        else {
	            startAngle = normalizeRadian(startAngle);
	            endAngle = normalizeRadian(endAngle);
	        }
	        if (startAngle > endAngle) {
	            endAngle += PI2;
	        }

	        var w = 0;
	        for (var i = 0; i < 2; i++) {
	            var x_ = roots[i];
	            if (x_ + cx > x) {
	                var angle = Math.atan2(y, x_);
	                var dir = anticlockwise ? 1 : -1;
	                if (angle < 0) {
	                    angle = PI2 + angle;
	                }
	                if (
	                    (angle >= startAngle && angle <= endAngle)
	                    || (angle + PI2 >= startAngle && angle + PI2 <= endAngle)
	                ) {
	                    if (angle > Math.PI / 2 && angle < Math.PI * 1.5) {
	                        dir = -dir;
	                    }
	                    w += dir;
	                }
	            }
	        }
	        return w;
	    }

	    function containPath(data, lineWidth, isStroke, x, y) {
	        var w = 0;
	        var xi = 0;
	        var yi = 0;
	        var x0 = 0;
	        var y0 = 0;

	        for (var i = 0; i < data.length;) {
	            var cmd = data[i++];
	            // Begin a new subpath
	            if (cmd === CMD.M && i > 1) {
	                // Close previous subpath
	                if (!isStroke) {
	                    w += windingLine(xi, yi, x0, y0, x, y);
	                }
	                // æ¿¡å‚›ç‰çšî‚¡æ¢æµ£æ›šç«´æ¶“ï¿½ subpath é–å‘­æƒˆ
	                // if (w !== 0) {
	                //     return true;
	                // }
	            }

	            if (i == 1) {
	                // æ¿¡å‚›ç‰ç»—îƒ¿ç«´æ¶“î„æ‡¡æµ ã‚†æ§¸ L, C, Q
	                // é’ï¿½ previous point éšå²€ç²¯é’è·ºæ‡¡æµ ã‚‡æ®‘ç»—îƒ¿ç«´æ¶“ï¿½ point
	                //
	                // ç»—îƒ¿ç«´æ¶“î„æ‡¡æµ ã‚„è´Ÿ Arc é¨å‹¬å„éå…¸ç¬…æµ¼æ°¬æ¹ªéšåº¨æ½°é—è§„ç•©æ¾¶å‹­æ‚Š
	                xi = data[i];
	                yi = data[i + 1];

	                x0 = xi;
	                y0 = yi;
	            }

	            switch (cmd) {
	                case CMD.M:
	                    // moveTo é›æˆ’æŠ¤é–²å¶†æŸŠé’æ¶˜ç¼“æ¶“â‚¬æ¶“î…æŸŠé¨ï¿½ subpath, éªžæœµç¬–é‡å­˜æŸŠé‚æ‰®æ®‘ç’§é£Žå£
	                    // é¦ï¿½ closePath é¨å‹¬æ¤‚éŠæ¬Žå¨‡é¢ï¿½
	                    x0 = data[i++];
	                    y0 = data[i++];
	                    xi = x0;
	                    yi = y0;
	                    break;
	                case CMD.L:
	                    if (isStroke) {
	                        if (containStroke(xi, yi, data[i], data[i + 1], lineWidth, x, y)) {
	                            return true;
	                        }
	                    }
	                    else {
	                        // NOTE é¦ã„§îƒ‡æ¶“â‚¬æ¶“î„æ‡¡æµ ã‚„è´Ÿ L, C, Q é¨å‹¬æ¤‚éŠæ¬Žç´°ç’ï¼„ç•»é‘ï¿½ NaN
	                        w += windingLine(xi, yi, data[i], data[i + 1], x, y) || 0;
	                    }
	                    xi = data[i++];
	                    yi = data[i++];
	                    break;
	                case CMD.C:
	                    if (isStroke) {
	                        if (cubic.containStroke(xi, yi,
	                            data[i++], data[i++], data[i++], data[i++], data[i], data[i + 1],
	                            lineWidth, x, y
	                        )) {
	                            return true;
	                        }
	                    }
	                    else {
	                        w += windingCubic(
	                            xi, yi,
	                            data[i++], data[i++], data[i++], data[i++], data[i], data[i + 1],
	                            x, y
	                        ) || 0;
	                    }
	                    xi = data[i++];
	                    yi = data[i++];
	                    break;
	                case CMD.Q:
	                    if (isStroke) {
	                        if (quadratic.containStroke(xi, yi,
	                            data[i++], data[i++], data[i], data[i + 1],
	                            lineWidth, x, y
	                        )) {
	                            return true;
	                        }
	                    }
	                    else {
	                        w += windingQuadratic(
	                            xi, yi,
	                            data[i++], data[i++], data[i], data[i + 1],
	                            x, y
	                        ) || 0;
	                    }
	                    xi = data[i++];
	                    yi = data[i++];
	                    break;
	                case CMD.A:
	                    // TODO Arc é’ã‚†æŸ‡é¨å‹«ç´‘é–¿â‚¬å§£æ—‡ç·æ¾¶ï¿½
	                    var cx = data[i++];
	                    var cy = data[i++];
	                    var rx = data[i++];
	                    var ry = data[i++];
	                    var theta = data[i++];
	                    var dTheta = data[i++];
	                    // TODO Arc éƒå¬­æµ†
	                    var psi = data[i++];
	                    var anticlockwise = 1 - data[i++];
	                    var x1 = Math.cos(theta) * rx + cx;
	                    var y1 = Math.sin(theta) * ry + cy;
	                    // æ¶“å¶†æ§¸é©å­˜å¸´æµ£è·¨æ•¤ arc é›æˆ’æŠ¤
	                    if (i > 1) {
	                        w += windingLine(xi, yi, x1, y1, x, y);
	                    }
	                    else {
	                        // ç»—îƒ¿ç«´æ¶“î„æ‡¡æµ ã‚ˆæ£éç¡…ç¹•éˆî„ç•¾æ¶”ï¿½
	                        x0 = x1;
	                        y0 = y1;
	                    }
	                    // zr æµ£è·¨æ•¤scaleé‰ãƒ¦ÄéŽ·ç†¸ãé¦ï¿½, æ©æ¬“å™·æ¶”ç†·î‡®xé‹æ°«ç«´ç€¹æ°±æ®‘ç¼‚â•‚æ–
	                    var _x = (x - cx) * ry / rx + cx;
	                    if (isStroke) {
	                        if (arc.containStroke(
	                            cx, cy, ry, theta, theta + dTheta, anticlockwise,
	                            lineWidth, _x, y
	                        )) {
	                            return true;
	                        }
	                    }
	                    else {
	                        w += windingArc(
	                            cx, cy, ry, theta, theta + dTheta, anticlockwise,
	                            _x, y
	                        );
	                    }
	                    xi = Math.cos(theta + dTheta) * rx + cx;
	                    yi = Math.sin(theta + dTheta) * ry + cy;
	                    break;
	                case CMD.R:
	                    x0 = xi = data[i++];
	                    y0 = yi = data[i++];
	                    var width = data[i++];
	                    var height = data[i++];
	                    var x1 = x0 + width;
	                    var y1 = y0 + height;
	                    if (isStroke) {
	                        if (containStroke(x0, y0, x1, y0, lineWidth, x, y)
	                          || containStroke(x1, y0, x1, y1, lineWidth, x, y)
	                          || containStroke(x1, y1, x0, y1, lineWidth, x, y)
	                          || containStroke(x0, y1, x0, y0, lineWidth, x, y)
	                        ) {
	                            return true;
	                        }
	                    }
	                    else {
	                        // FIXME Clockwise ?
	                        w += windingLine(x1, y0, x1, y1, x, y);
	                        w += windingLine(x0, y1, x0, y0, x, y);
	                    }
	                    break;
	                case CMD.Z:
	                    if (isStroke) {
	                        if (containStroke(
	                            xi, yi, x0, y0, lineWidth, x, y
	                        )) {
	                            return true;
	                        }
	                    }
	                    else {
	                        // Close a subpath
	                        w += windingLine(xi, yi, x0, y0, x, y);
	                        // æ¿¡å‚›ç‰çšî‚¡æ¢æµ£æ›šç«´æ¶“ï¿½ subpath é–å‘­æƒˆ
	                        // FIXME subpaths may overlap
	                        // if (w !== 0) {
	                        //     return true;
	                        // }
	                    }
	                    xi = x0;
	                    yi = y0;
	                    break;
	            }
	        }
	        if (!isStroke && !isAroundEqual(yi, y0)) {
	            w += windingLine(xi, yi, x0, y0, x, y) || 0;
	        }
	        return w !== 0;
	    }

	    module.exports = {
	        contain: function (pathData, x, y) {
	            return containPath(pathData, 0, false, x, y);
	        },

	        containStroke: function (pathData, lineWidth, x, y) {
	            return containPath(pathData, lineWidth, true, x, y);
	        }
	    };


/***/ },
/* 33 */
/***/ function(module, exports) {

	
	    module.exports = {
	        /**
	         * ç»¾æŒŽî†Œé–å‘­æƒˆé’ã‚†æŸ‡
	         * @param  {number}  x0
	         * @param  {number}  y0
	         * @param  {number}  x1
	         * @param  {number}  y1
	         * @param  {number}  lineWidth
	         * @param  {number}  x
	         * @param  {number}  y
	         * @return {boolean}
	         */
	        containStroke: function (x0, y0, x1, y1, lineWidth, x, y) {
	            if (lineWidth === 0) {
	                return false;
	            }
	            var _l = lineWidth;
	            var _a = 0;
	            var _b = x0;
	            // Quick reject
	            if (
	                (y > y0 + _l && y > y1 + _l)
	                || (y < y0 - _l && y < y1 - _l)
	                || (x > x0 + _l && x > x1 + _l)
	                || (x < x0 - _l && x < x1 - _l)
	            ) {
	                return false;
	            }

	            if (x0 !== x1) {
	                _a = (y0 - y1) / (x0 - x1);
	                _b = (x0 * y1 - x1 * y0) / (x0 - x1) ;
	            }
	            else {
	                return Math.abs(x - x0) <= _l / 2;
	            }
	            var tmp = _a * x - y + _b;
	            var _s = tmp * tmp / (_a * _a + 1);
	            return _s <= _l / 2 * _l / 2;
	        }
	    };


/***/ },
/* 34 */
/***/ function(module, exports, __webpack_require__) {

	

	    var curve = __webpack_require__(30);

	    module.exports = {
	        /**
	         * æ¶“å¤‹î‚¼ç’æ¿†î”£çæ—€æ´¸ç»¾æŒŽå¼¿æˆç‘°å¯˜éšî‚¢åž½é‚ï¿½
	         * @param  {number}  x0
	         * @param  {number}  y0
	         * @param  {number}  x1
	         * @param  {number}  y1
	         * @param  {number}  x2
	         * @param  {number}  y2
	         * @param  {number}  x3
	         * @param  {number}  y3
	         * @param  {number}  lineWidth
	         * @param  {number}  x
	         * @param  {number}  y
	         * @return {boolean}
	         */
	        containStroke: function(x0, y0, x1, y1, x2, y2, x3, y3, lineWidth, x, y) {
	            if (lineWidth === 0) {
	                return false;
	            }
	            var _l = lineWidth;
	            // Quick reject
	            if (
	                (y > y0 + _l && y > y1 + _l && y > y2 + _l && y > y3 + _l)
	                || (y < y0 - _l && y < y1 - _l && y < y2 - _l && y < y3 - _l)
	                || (x > x0 + _l && x > x1 + _l && x > x2 + _l && x > x3 + _l)
	                || (x < x0 - _l && x < x1 - _l && x < x2 - _l && x < x3 - _l)
	            ) {
	                return false;
	            }
	            var d = curve.cubicProjectPoint(
	                x0, y0, x1, y1, x2, y2, x3, y3,
	                x, y, null
	            );
	            return d <= _l / 2;
	        }
	    };


/***/ },
/* 35 */
/***/ function(module, exports, __webpack_require__) {

	

	    var curve = __webpack_require__(30);

	    module.exports = {
	        /**
	         * æµœå±¾î‚¼ç’æ¿†î”£çæ—€æ´¸ç»¾æŒŽå¼¿æˆç‘°å¯˜éšî‚¢åž½é‚ï¿½
	         * @param  {number}  x0
	         * @param  {number}  y0
	         * @param  {number}  x1
	         * @param  {number}  y1
	         * @param  {number}  x2
	         * @param  {number}  y2
	         * @param  {number}  lineWidth
	         * @param  {number}  x
	         * @param  {number}  y
	         * @return {boolean}
	         */
	        containStroke: function (x0, y0, x1, y1, x2, y2, lineWidth, x, y) {
	            if (lineWidth === 0) {
	                return false;
	            }
	            var _l = lineWidth;
	            // Quick reject
	            if (
	                (y > y0 + _l && y > y1 + _l && y > y2 + _l)
	                || (y < y0 - _l && y < y1 - _l && y < y2 - _l)
	                || (x > x0 + _l && x > x1 + _l && x > x2 + _l)
	                || (x < x0 - _l && x < x1 - _l && x < x2 - _l)
	            ) {
	                return false;
	            }
	            var d = curve.quadraticProjectPoint(
	                x0, y0, x1, y1, x2, y2,
	                x, y, null
	            );
	            return d <= _l / 2;
	        }
	    };


/***/ },
/* 36 */
/***/ function(module, exports, __webpack_require__) {

	

	    var normalizeRadian = __webpack_require__(37).normalizeRadian;
	    var PI2 = Math.PI * 2;

	    module.exports = {
	        /**
	         * é¦å——å§¬éŽ»å¿šç«Ÿé–å‘­æƒˆé’ã‚†æŸ‡
	         * @param  {number}  cx
	         * @param  {number}  cy
	         * @param  {number}  r
	         * @param  {number}  startAngle
	         * @param  {number}  endAngle
	         * @param  {boolean}  anticlockwise
	         * @param  {number} lineWidth
	         * @param  {number}  x
	         * @param  {number}  y
	         * @return {Boolean}
	         */
	        containStroke: function (
	            cx, cy, r, startAngle, endAngle, anticlockwise,
	            lineWidth, x, y
	        ) {

	            if (lineWidth === 0) {
	                return false;
	            }
	            var _l = lineWidth;

	            x -= cx;
	            y -= cy;
	            var d = Math.sqrt(x * x + y * y);

	            if ((d - _l > r) || (d + _l < r)) {
	                return false;
	            }
	            if (Math.abs(startAngle - endAngle) % PI2 < 1e-4) {
	                // Is a circle
	                return true;
	            }
	            if (anticlockwise) {
	                var tmp = startAngle;
	                startAngle = normalizeRadian(endAngle);
	                endAngle = normalizeRadian(tmp);
	            } else {
	                startAngle = normalizeRadian(startAngle);
	                endAngle = normalizeRadian(endAngle);
	            }
	            if (startAngle > endAngle) {
	                endAngle += PI2;
	            }

	            var angle = Math.atan2(y, x);
	            if (angle < 0) {
	                angle += PI2;
	            }
	            return (angle >= startAngle && angle <= endAngle)
	                || (angle + PI2 >= startAngle && angle + PI2 <= endAngle);
	        }
	    };


/***/ },
/* 37 */
/***/ function(module, exports) {

	

	    var PI2 = Math.PI * 2;
	    module.exports = {
	        normalizeRadian: function(angle) {
	            angle %= PI2;
	            if (angle < 0) {
	                angle += PI2;
	            }
	            return angle;
	        }
	    };


/***/ },
/* 38 */
/***/ function(module, exports) {

	
	    module.exports = function windingLine(x0, y0, x1, y1, x, y) {
	        if ((y > y0 && y > y1) || (y < y0 && y < y1)) {
	            return 0;
	        }
	        // Ignore horizontal line
	        if (y1 === y0) {
	            return 0;
	        }
	        var dir = y1 < y0 ? 1 : -1;
	        var t = (y - y0) / (y1 - y0);

	        // Avoid winding error when intersection point is the connect point of two line of polygon
	        if (t === 1 || t === 0) {
	            dir = y1 < y0 ? 0.5 : -0.5;
	        }

	        var x_ = t * (x1 - x0) + x0;

	        return x_ > x ? dir : 0;
	    };


/***/ },
/* 39 */
/***/ function(module, exports) {

	

	    var Pattern = function (image, repeat) {
	        this.image = image;
	        this.repeat = repeat;

	        // Can be cloned
	        this.type = 'pattern';
	    };

	    Pattern.prototype.getCanvasPattern = function (ctx) {

	        return this._canvasPattern
	            || (this._canvasPattern = ctx.createPattern(this.image, this.repeat));
	    };

	    module.exports = Pattern;


/***/ },
/* 40 */
/***/ function(module, exports, __webpack_require__) {

	

	    var CMD = __webpack_require__(29).CMD;
	    var vec2 = __webpack_require__(18);
	    var v2ApplyTransform = vec2.applyTransform;

	    var points = [[], [], []];
	    var mathSqrt = Math.sqrt;
	    var mathAtan2 = Math.atan2;
	    function transformPath(path, m) {
	        var data = path.data;
	        var cmd;
	        var nPoint;
	        var i;
	        var j;
	        var k;
	        var p;

	        var M = CMD.M;
	        var C = CMD.C;
	        var L = CMD.L;
	        var R = CMD.R;
	        var A = CMD.A;
	        var Q = CMD.Q;

	        for (i = 0, j = 0; i < data.length;) {
	            cmd = data[i++];
	            j = i;
	            nPoint = 0;

	            switch (cmd) {
	                case M:
	                    nPoint = 1;
	                    break;
	                case L:
	                    nPoint = 1;
	                    break;
	                case C:
	                    nPoint = 3;
	                    break;
	                case Q:
	                    nPoint = 2;
	                    break;
	                case A:
	                    var x = m[4];
	                    var y = m[5];
	                    var sx = mathSqrt(m[0] * m[0] + m[1] * m[1]);
	                    var sy = mathSqrt(m[2] * m[2] + m[3] * m[3]);
	                    var angle = mathAtan2(-m[1] / sy, m[0] / sx);
	                    // cx
	                    data[i++] += x;
	                    // cy
	                    data[i++] += y;
	                    // Scale rx and ry
	                    // FIXME Assume psi is 0 here
	                    data[i++] *= sx;
	                    data[i++] *= sy;

	                    // Start angle
	                    data[i++] += angle;
	                    // end angle
	                    data[i++] += angle;
	                    // FIXME psi
	                    i += 2;
	                    j = i;
	                    break;
	                case R:
	                    // x0, y0
	                    p[0] = data[i++];
	                    p[1] = data[i++];
	                    v2ApplyTransform(p, p, m);
	                    data[j++] = p[0];
	                    data[j++] = p[1];
	                    // x1, y1
	                    p[0] += data[i++];
	                    p[1] += data[i++];
	                    v2ApplyTransform(p, p, m);
	                    data[j++] = p[0];
	                    data[j++] = p[1];
	            }

	            for (k = 0; k < nPoint; k++) {
	                var p = points[k];
	                p[0] = data[i++];
	                p[1] = data[i++];

	                v2ApplyTransform(p, p, m);
	                // Write back
	                data[j++] = p[0];
	                data[j++] = p[1];
	            }
	        }
	    }

	    module.exports = transformPath;


/***/ },
/* 41 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * Groupé„îˆ™ç«´æ¶“î„î†é£îŸ’ç´é™îˆ™äº’éŽ»æŽ‘å†ç€›æ„¯å¦­éç™¸ç´Groupé¨å‹«å½‰éŽ¹î­ç¯ƒæµ¼æ°³î¦æ´æ—‚æ•¤é’æ¿ç“™é‘ºå‚œå£æ¶“ï¿½
	 * @module zrender/graphic/Group
	 * @example
	 *     var Group = require('zrender/lib/container/Group');
	 *     var Circle = require('zrender/lib/graphic/shape/Circle');
	 *     var g = new Group();
	 *     g.position[0] = 100;
	 *     g.position[1] = 100;
	 *     g.add(new Circle({
	 *         style: {
	 *             x: 100,
	 *             y: 100,
	 *             r: 20,
	 *         }
	 *     }));
	 *     zr.add(g);
	 */


	    var zrUtil = __webpack_require__(5);
	    var Element = __webpack_require__(13);
	    var BoundingRect = __webpack_require__(28);

	    /**
	     * @alias module:zrender/graphic/Group
	     * @constructor
	     * @extends module:zrender/mixin/Transformable
	     * @extends module:zrender/mixin/Eventful
	     */
	    var Group = function (opts) {

	        opts = opts || {};

	        Element.call(this, opts);

	        for (var key in opts) {
	            if (opts.hasOwnProperty(key)) {
	                this[key] = opts[key];
	            }
	        }

	        this._children = [];

	        this.__storage = null;

	        this.__dirty = true;
	    };

	    Group.prototype = {

	        constructor: Group,

	        isGroup: true,

	        /**
	         * @type {string}
	         */
	        type: 'group',

	        /**
	         * éŽµâ‚¬éˆå¤Šç“™ç€›æ¬åŽ“ç»±çŠ³æ§¸éšï¹€æ·æ´æ—ˆç´¶éå›¦ç°¨æµ ï¿½
	         * @name module:/zrender/container/Group#silent
	         * @type {boolean}
	         * @default false
	         */
	        silent: false,

	        /**
	         * @return {Array.<module:zrender/Element>}
	         */
	        children: function () {
	            return this._children.slice();
	        },

	        /**
	         * é‘¾å³°å½‡éŽ¸å›§ç•¾ index é¨å‹«åŠ¹ç€›æ„¯å¦­éï¿½
	         * @param  {number} idx
	         * @return {module:zrender/Element}
	         */
	        childAt: function (idx) {
	            return this._children[idx];
	        },

	        /**
	         * é‘¾å³°å½‡éŽ¸å›§ç•¾éšå¶…ç“§é¨å‹«åŠ¹ç€›æ„¯å¦­éï¿½
	         * @param  {string} name
	         * @return {module:zrender/Element}
	         */
	        childOfName: function (name) {
	            var children = this._children;
	            for (var i = 0; i < children.length; i++) {
	                if (children[i].name === name) {
	                    return children[i];
	                }
	             }
	        },

	        /**
	         * @return {number}
	         */
	        childCount: function () {
	            return this._children.length;
	        },

	        /**
	         * å¨£è¯²å§žç€›æ„¯å¦­éç‘°åŸŒéˆâ‚¬éšï¿½
	         * @param {module:zrender/Element} child
	         */
	        add: function (child) {
	            if (child && child !== this && child.parent !== this) {

	                this._children.push(child);

	                this._doAdd(child);
	            }

	            return this;
	        },

	        /**
	         * å¨£è¯²å§žç€›æ„¯å¦­éç‘°æ¹ª nextSibling æ¶”å¬ªå¢ 
	         * @param {module:zrender/Element} child
	         * @param {module:zrender/Element} nextSibling
	         */
	        addBefore: function (child, nextSibling) {
	            if (child && child !== this && child.parent !== this
	                && nextSibling && nextSibling.parent === this) {

	                var children = this._children;
	                var idx = children.indexOf(nextSibling);

	                if (idx >= 0) {
	                    children.splice(idx, 0, child);
	                    this._doAdd(child);
	                }
	            }

	            return this;
	        },

	        _doAdd: function (child) {
	            if (child.parent) {
	                child.parent.remove(child);
	            }

	            child.parent = this;

	            var storage = this.__storage;
	            var zr = this.__zr;
	            if (storage && storage !== child.__storage) {

	                storage.addToMap(child);

	                if (child instanceof Group) {
	                    child.addChildrenToStorage(storage);
	                }
	            }

	            zr && zr.refresh();
	        },

	        /**
	         * ç»‰å©šæ«Žç€›æ„¯å¦­éï¿½
	         * @param {module:zrender/Element} child
	         */
	        remove: function (child) {
	            var zr = this.__zr;
	            var storage = this.__storage;
	            var children = this._children;

	            var idx = zrUtil.indexOf(children, child);
	            if (idx < 0) {
	                return this;
	            }
	            children.splice(idx, 1);

	            child.parent = null;

	            if (storage) {

	                storage.delFromMap(child.id);

	                if (child instanceof Group) {
	                    child.delChildrenFromStorage(storage);
	                }
	            }

	            zr && zr.refresh();

	            return this;
	        },

	        /**
	         * ç»‰å©šæ«ŽéŽµâ‚¬éˆå¤Šç“™é‘ºå‚œå£
	         */
	        removeAll: function () {
	            var children = this._children;
	            var storage = this.__storage;
	            var child;
	            var i;
	            for (i = 0; i < children.length; i++) {
	                child = children[i];
	                if (storage) {
	                    storage.delFromMap(child.id);
	                    if (child instanceof Group) {
	                        child.delChildrenFromStorage(storage);
	                    }
	                }
	                child.parent = null;
	            }
	            children.length = 0;

	            return this;
	        },

	        /**
	         * é–¬å¶…å·»éŽµâ‚¬éˆå¤Šç“™é‘ºå‚œå£
	         * @param  {Function} cb
	         * @param  {}   context
	         */
	        eachChild: function (cb, context) {
	            var children = this._children;
	            for (var i = 0; i < children.length; i++) {
	                var child = children[i];
	                cb.call(context, child, i);
	            }
	            return this;
	        },

	        /**
	         * å¨£åžå®³æµ¼æ¨ºåŽ›é–¬å¶…å·»éŽµâ‚¬éˆå¤Šç“™ç€›æ¬’å¦­éï¿½
	         * @param  {Function} cb
	         * @param  {}   context
	         */
	        traverse: function (cb, context) {
	            for (var i = 0; i < this._children.length; i++) {
	                var child = this._children[i];
	                cb.call(context, child);

	                if (child.type === 'group') {
	                    child.traverse(cb, context);
	                }
	            }
	            return this;
	        },

	        addChildrenToStorage: function (storage) {
	            for (var i = 0; i < this._children.length; i++) {
	                var child = this._children[i];
	                storage.addToMap(child);
	                if (child instanceof Group) {
	                    child.addChildrenToStorage(storage);
	                }
	            }
	        },

	        delChildrenFromStorage: function (storage) {
	            for (var i = 0; i < this._children.length; i++) {
	                var child = this._children[i];
	                storage.delFromMap(child.id);
	                if (child instanceof Group) {
	                    child.delChildrenFromStorage(storage);
	                }
	            }
	        },

	        dirty: function () {
	            this.__dirty = true;
	            this.__zr && this.__zr.refresh();
	            return this;
	        },

	        /**
	         * @return {module:zrender/core/BoundingRect}
	         */
	        getBoundingRect: function (includeChildren) {
	            // TODO Caching
	            var rect = null;
	            var tmpRect = new BoundingRect(0, 0, 0, 0);
	            var children = includeChildren || this._children;
	            var tmpMat = [];

	            for (var i = 0; i < children.length; i++) {
	                var child = children[i];
	                if (child.ignore || child.invisible) {
	                    continue;
	                }

	                var childRect = child.getBoundingRect();
	                var transform = child.getLocalTransform(tmpMat);
	                // TODO
	                // The boundingRect cacluated by transforming original
	                // rect may be bigger than the actual bundingRect when rotation
	                // is used. (Consider a circle rotated aginst its center, where
	                // the actual boundingRect should be the same as that not be
	                // rotated.) But we can not find better approach to calculate
	                // actual boundingRect yet, considering performance.
	                if (transform) {
	                    tmpRect.copy(childRect);
	                    tmpRect.applyTransform(transform);
	                    rect = rect || tmpRect.clone();
	                    rect.union(tmpRect);
	                }
	                else {
	                    rect = rect || childRect.clone();
	                    rect.union(childRect);
	                }
	            }
	            return rect || tmpRect;
	        }
	    };

	    zrUtil.inherits(Group, Element);

	    module.exports = Group;


/***/ },
/* 42 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * Image element
	 * @module zrender/graphic/Image
	 */



	    var Displayable = __webpack_require__(11);
	    var BoundingRect = __webpack_require__(28);
	    var zrUtil = __webpack_require__(5);

	    var LRU = __webpack_require__(43);
	    var globalImageCache = new LRU(50);
	    /**
	     * @alias zrender/graphic/Image
	     * @extends module:zrender/graphic/Displayable
	     * @constructor
	     * @param {Object} opts
	     */
	    function ZImage(opts) {
	        Displayable.call(this, opts);
	    }

	    ZImage.prototype = {

	        constructor: ZImage,

	        type: 'image',

	        brush: function (ctx, prevEl) {
	            var style = this.style;
	            var src = style.image;
	            var image;

	            // Must bind each time
	            style.bind(ctx, this, prevEl);
	            // style.image is a url string
	            if (typeof src === 'string') {
	                image = this._image;
	            }
	            // style.image is an HTMLImageElement or HTMLCanvasElement or Canvas
	            else {
	                image = src;
	            }
	            // FIXME Case create many images with src
	            if (!image && src) {
	                // Try get from global image cache
	                var cachedImgObj = globalImageCache.get(src);
	                if (!cachedImgObj) {
	                    // Create a new image
	                    image = new Image();
	                    image.onload = function () {
	                        image.onload = null;
	                        for (var i = 0; i < cachedImgObj.pending.length; i++) {
	                            cachedImgObj.pending[i].dirty();
	                        }
	                    };
	                    cachedImgObj = {
	                        image: image,
	                        pending: [this]
	                    };
	                    image.src = src;
	                    globalImageCache.put(src, cachedImgObj);
	                    this._image = image;
	                    return;
	                }
	                else {
	                    image = cachedImgObj.image;
	                    this._image = image;
	                    // Image is not complete finish, add to pending list
	                    if (!image.width || !image.height) {
	                        cachedImgObj.pending.push(this);
	                        return;
	                    }
	                }
	            }

	            if (image) {
	                // é¥å‰§å¢–å®¸èŒ¬ç²¡é”çŠºæµ‡ç€¹å±¾åžš
	                // if (image.nodeName.toUpperCase() == 'IMG') {
	                //     if (!image.complete) {
	                //         return;
	                //     }
	                // }
	                // Else is canvas

	                var width = style.width || image.width;
	                var height = style.height || image.height;
	                var x = style.x || 0;
	                var y = style.y || 0;
	                // é¥å‰§å¢–é”çŠºæµ‡æ¾¶è¾«è§¦
	                if (!image.width || !image.height) {
	                    return;
	                }

	                // ç’å‰§ç–†transform
	                this.setTransform(ctx);


	                if (style.sWidth && style.sHeight) {
	                    var sx = style.sx || 0;
	                    var sy = style.sy || 0;
	                    ctx.drawImage(
	                        image,
	                        sx, sy, style.sWidth, style.sHeight,
	                        x, y, width, height
	                    );
	                }
	                else if (style.sx && style.sy) {
	                    var sx = style.sx;
	                    var sy = style.sy;
	                    var sWidth = width - sx;
	                    var sHeight = height - sy;
	                    ctx.drawImage(
	                        image,
	                        sx, sy, sWidth, sHeight,
	                        x, y, width, height
	                    );
	                }
	                else {
	                    ctx.drawImage(image, x, y, width, height);
	                }

	                // æ¿¡å‚›ç‰å¨ŒÂ¤î†•ç¼ƒî†¼î†”éœå²„ç®é¨å‹®ç˜½é‘·î„å§©éè§„åµé¥å‰§å¢–ç€¹ä»‹ç®ç’å‰§ç–†
	                if (style.width == null) {
	                    style.width = width;
	                }
	                if (style.height == null) {
	                    style.height = height;
	                }

	                this.restoreTransform(ctx);

	                // Draw rect text
	                if (style.text != null) {
	                    this.drawRectText(ctx, this.getBoundingRect());
	                }

	            }
	        },

	        getBoundingRect: function () {
	            var style = this.style;
	            if (! this._rect) {
	                this._rect = new BoundingRect(
	                    style.x || 0, style.y || 0, style.width || 0, style.height || 0
	                );
	            }
	            return this._rect;
	        }
	    };

	    zrUtil.inherits(ZImage, Displayable);

	    module.exports = ZImage;


/***/ },
/* 43 */
/***/ function(module, exports) {

	// Simple LRU cache use doubly linked list
	// @module zrender/core/LRU


	    /**
	     * Simple double linked list. Compared with array, it has O(1) remove operation.
	     * @constructor
	     */
	    var LinkedList = function() {

	        /**
	         * @type {module:zrender/core/LRU~Entry}
	         */
	        this.head = null;

	        /**
	         * @type {module:zrender/core/LRU~Entry}
	         */
	        this.tail = null;

	        this._len = 0;
	    };

	    var linkedListProto = LinkedList.prototype;
	    /**
	     * Insert a new value at the tail
	     * @param  {} val
	     * @return {module:zrender/core/LRU~Entry}
	     */
	    linkedListProto.insert = function(val) {
	        var entry = new Entry(val);
	        this.insertEntry(entry);
	        return entry;
	    };

	    /**
	     * Insert an entry at the tail
	     * @param  {module:zrender/core/LRU~Entry} entry
	     */
	    linkedListProto.insertEntry = function(entry) {
	        if (!this.head) {
	            this.head = this.tail = entry;
	        }
	        else {
	            this.tail.next = entry;
	            entry.prev = this.tail;
	            this.tail = entry;
	        }
	        this._len++;
	    };

	    /**
	     * Remove entry.
	     * @param  {module:zrender/core/LRU~Entry} entry
	     */
	    linkedListProto.remove = function(entry) {
	        var prev = entry.prev;
	        var next = entry.next;
	        if (prev) {
	            prev.next = next;
	        }
	        else {
	            // Is head
	            this.head = next;
	        }
	        if (next) {
	            next.prev = prev;
	        }
	        else {
	            // Is tail
	            this.tail = prev;
	        }
	        entry.next = entry.prev = null;
	        this._len--;
	    };

	    /**
	     * @return {number}
	     */
	    linkedListProto.len = function() {
	        return this._len;
	    };

	    /**
	     * @constructor
	     * @param {} val
	     */
	    var Entry = function(val) {
	        /**
	         * @type {}
	         */
	        this.value = val;

	        /**
	         * @type {module:zrender/core/LRU~Entry}
	         */
	        this.next;

	        /**
	         * @type {module:zrender/core/LRU~Entry}
	         */
	        this.prev;
	    };

	    /**
	     * LRU Cache
	     * @constructor
	     * @alias module:zrender/core/LRU
	     */
	    var LRU = function(maxSize) {

	        this._list = new LinkedList();

	        this._map = {};

	        this._maxSize = maxSize || 10;
	    };

	    var LRUProto = LRU.prototype;

	    /**
	     * @param  {string} key
	     * @param  {} value
	     */
	    LRUProto.put = function(key, value) {
	        var list = this._list;
	        var map = this._map;
	        if (map[key] == null) {
	            var len = list.len();
	            if (len >= this._maxSize && len > 0) {
	                // Remove the least recently used
	                var leastUsedEntry = list.head;
	                list.remove(leastUsedEntry);
	                delete map[leastUsedEntry.key];
	            }

	            var entry = list.insert(value);
	            entry.key = key;
	            map[key] = entry;
	        }
	    };

	    /**
	     * @param  {string} key
	     * @return {}
	     */
	    LRUProto.get = function(key) {
	        var entry = this._map[key];
	        var list = this._list;
	        if (entry != null) {
	            // Put the latest used entry in the tail
	            if (entry !== list.tail) {
	                list.remove(entry);
	                list.insertEntry(entry);
	            }

	            return entry.value;
	        }
	    };

	    /**
	     * Clear the cache
	     */
	    LRUProto.clear = function() {
	        this._list.clear();
	        this._map = {};
	    };

	    module.exports = LRU;


/***/ },
/* 44 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * Text element
	 * @module zrender/graphic/Text
	 *
	 * TODO Wrapping
	 *
	 * Text not support gradient
	 */



	    var Displayable = __webpack_require__(11);
	    var zrUtil = __webpack_require__(5);
	    var textContain = __webpack_require__(27);

	    /**
	     * @alias zrender/graphic/Text
	     * @extends module:zrender/graphic/Displayable
	     * @constructor
	     * @param {Object} opts
	     */
	    var Text = function (opts) {
	        Displayable.call(this, opts);
	    };

	    Text.prototype = {

	        constructor: Text,

	        type: 'text',

	        brush: function (ctx, prevEl) {
	            var style = this.style;
	            var x = style.x || 0;
	            var y = style.y || 0;
	            // Convert to string
	            var text = style.text;

	            // Convert to string
	            text != null && (text += '');

	            // Always bind style
	            style.bind(ctx, this, prevEl);

	            if (text) {

	                this.setTransform(ctx);

	                var textBaseline;
	                var textAlign = style.textAlign;
	                var font = style.textFont || style.font;
	                if (style.textVerticalAlign) {
	                    var rect = textContain.getBoundingRect(
	                        text, font, style.textAlign, 'top'
	                    );
	                    // Ignore textBaseline
	                    textBaseline = 'middle';
	                    switch (style.textVerticalAlign) {
	                        case 'middle':
	                            y -= rect.height / 2 - rect.lineHeight / 2;
	                            break;
	                        case 'bottom':
	                            y -= rect.height - rect.lineHeight / 2;
	                            break;
	                        default:
	                            y += rect.lineHeight / 2;
	                    }
	                }
	                else {
	                    textBaseline = style.textBaseline;
	                }

	                // TODO Invalid font
	                ctx.font = font || '12px sans-serif';
	                ctx.textAlign = textAlign || 'left';
	                // Use canvas default left textAlign. Giving invalid value will cause state not change
	                if (ctx.textAlign !== textAlign) {
	                    ctx.textAlign = 'left';
	                }
	                ctx.textBaseline = textBaseline || 'alphabetic';
	                // Use canvas default alphabetic baseline
	                if (ctx.textBaseline !== textBaseline) {
	                    ctx.textBaseline = 'alphabetic';
	                }

	                var lineHeight = textContain.measureText('é¥ï¿½', ctx.font).width;

	                var textLines = text.split('\n');
	                for (var i = 0; i < textLines.length; i++) {
	                    style.hasFill() && ctx.fillText(textLines[i], x, y);
	                    style.hasStroke() && ctx.strokeText(textLines[i], x, y);
	                    y += lineHeight;
	                }

	                this.restoreTransform(ctx);
	            }
	        },

	        getBoundingRect: function () {
	            if (!this._rect) {
	                var style = this.style;
	                var textVerticalAlign = style.textVerticalAlign;
	                var rect = textContain.getBoundingRect(
	                    style.text + '', style.textFont || style.font, style.textAlign,
	                    textVerticalAlign ? 'top' : style.textBaseline
	                );
	                switch (textVerticalAlign) {
	                    case 'middle':
	                        rect.y -= rect.height / 2;
	                        break;
	                    case 'bottom':
	                        rect.y -= rect.height;
	                        break;
	                }
	                rect.x += style.x || 0;
	                rect.y += style.y || 0;
	                this._rect = rect;
	            }
	            return this._rect;
	        }
	    };

	    zrUtil.inherits(Text, Displayable);

	    module.exports = Text;


/***/ },
/* 45 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	/**
	 * é¦å——èˆ°
	 * @module zrender/shape/Circle
	 */



	    module.exports = __webpack_require__(10).extend({

	        type: 'circle',

	        shape: {
	            cx: 0,
	            cy: 0,
	            r: 0
	        },


	        buildPath : function (ctx, shape, inBundle) {
	            // Better stroking in ShapeBundle
	            // Always do it may have performence issue ( fill may be 2x more cost)
	            if (inBundle) {
	                ctx.moveTo(shape.cx + shape.r, shape.cy);
	            }
	            // Better stroking in ShapeBundle
	            // ctx.moveTo(shape.cx + shape.r, shape.cy);
	            ctx.arc(shape.cx, shape.cy, shape.r, 0, Math.PI * 2, true);
	        }
	    });



/***/ },
/* 46 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * éŽµå›§èˆ°
	 * @module zrender/graphic/shape/Sector
	 */



	    var env = __webpack_require__(47);
	    var Path = __webpack_require__(10);

	    var shadowTemp = [
	        ['shadowBlur', 0],
	        ['shadowColor', '#000'],
	        ['shadowOffsetX', 0],
	        ['shadowOffsetY', 0]
	    ];

	    module.exports = Path.extend({

	        type: 'sector',

	        shape: {

	            cx: 0,

	            cy: 0,

	            r0: 0,

	            r: 0,

	            startAngle: 0,

	            endAngle: Math.PI * 2,

	            clockwise: true
	        },

	        brush: (env.browser.ie && env.browser.version >= 11) // version: '11.0'
	            // Fix weird bug in some version of IE11 (like 11.0.9600.17801),
	            // where exception "unexpected call to method or property access"
	            // might be thrown when calling ctx.fill after a path whose area size
	            // is zero is drawn and ctx.clip() is called and shadowBlur is set.
	            // (e.g.,
	            //  ctx.moveTo(10, 10);
	            //  ctx.lineTo(20, 10);
	            //  ctx.closePath();
	            //  ctx.clip();
	            //  ctx.shadowBlur = 10;
	            //  ...
	            //  ctx.fill();
	            // )
	            ? function () {
	                var clipPaths = this.__clipPaths;
	                var style = this.style;
	                var modified;

	                if (clipPaths) {
	                    for (var i = 0; i < clipPaths.length; i++) {
	                        var shape = clipPaths[i] && clipPaths[i].shape;
	                        if (shape && shape.startAngle === shape.endAngle) {
	                            for (var j = 0; j < shadowTemp.length; j++) {
	                                shadowTemp[j][2] = style[shadowTemp[j][0]];
	                                style[shadowTemp[j][0]] = shadowTemp[j][1];
	                            }
	                            modified = true;
	                            break;
	                        }
	                    }
	                }

	                Path.prototype.brush.apply(this, arguments);

	                if (modified) {
	                    for (var j = 0; j < shadowTemp.length; j++) {
	                        style[shadowTemp[j][0]] = shadowTemp[j][2];
	                    }
	                }
	            }
	            : Path.prototype.brush,

	        buildPath: function (ctx, shape) {

	            var x = shape.cx;
	            var y = shape.cy;
	            var r0 = Math.max(shape.r0 || 0, 0);
	            var r = Math.max(shape.r, 0);
	            var startAngle = shape.startAngle;
	            var endAngle = shape.endAngle;
	            var clockwise = shape.clockwise;

	            var unitX = Math.cos(startAngle);
	            var unitY = Math.sin(startAngle);

	            ctx.moveTo(unitX * r0 + x, unitY * r0 + y);

	            ctx.lineTo(unitX * r + x, unitY * r + y);

	            ctx.arc(x, y, r, startAngle, endAngle, !clockwise);

	            ctx.lineTo(
	                Math.cos(endAngle) * r0 + x,
	                Math.sin(endAngle) * r0 + y
	            );

	            if (r0 !== 0) {
	                ctx.arc(x, y, r0, endAngle, startAngle, clockwise);
	            }

	            ctx.closePath();
	        }
	    });



/***/ },
/* 47 */
/***/ function(module, exports) {

	/**
	 * echartsç’æƒ§î˜¬éœîˆšî•¨ç’‡å——åŸ†
	 *
	 * @desc echartsé©è½°ç°¬Canvasé”›å²€å‡½Javascripté¥æã€ƒæ´æ“„ç´éŽ»æ„ªç·µé©ç£‹î‡é”›å²€æ•“é”îŸ’ç´é™îˆ™æ°¦æµœæŽžç´é™îˆ™é‡œéŽ¬Ñƒå¯²ç€¹æ°¬åŸ—é¨å‹¬æšŸéŽ¹î†¾ç²ºç’â€³æµ˜ç›ã„£â‚¬ï¿½
	 * @author firede[firede@firede.us]
	 * @desc thanks zepto.
	 */

	    var env = {};
	    if (typeof navigator === 'undefined') {
	        // In node
	        env = {
	            browser: {},
	            os: {},
	            node: true,
	            // Assume canvas is supported
	            canvasSupported: true
	        };
	    }
	    else {
	        env = detect(navigator.userAgent);
	    }

	    module.exports = env;

	    // Zepto.js
	    // (c) 2010-2013 Thomas Fuchs
	    // Zepto.js may be freely distributed under the MIT license.

	    function detect(ua) {
	        var os = {};
	        var browser = {};
	        // var webkit = ua.match(/Web[kK]it[\/]{0,1}([\d.]+)/);
	        // var android = ua.match(/(Android);?[\s\/]+([\d.]+)?/);
	        // var ipad = ua.match(/(iPad).*OS\s([\d_]+)/);
	        // var ipod = ua.match(/(iPod)(.*OS\s([\d_]+))?/);
	        // var iphone = !ipad && ua.match(/(iPhone\sOS)\s([\d_]+)/);
	        // var webos = ua.match(/(webOS|hpwOS)[\s\/]([\d.]+)/);
	        // var touchpad = webos && ua.match(/TouchPad/);
	        // var kindle = ua.match(/Kindle\/([\d.]+)/);
	        // var silk = ua.match(/Silk\/([\d._]+)/);
	        // var blackberry = ua.match(/(BlackBerry).*Version\/([\d.]+)/);
	        // var bb10 = ua.match(/(BB10).*Version\/([\d.]+)/);
	        // var rimtabletos = ua.match(/(RIM\sTablet\sOS)\s([\d.]+)/);
	        // var playbook = ua.match(/PlayBook/);
	        // var chrome = ua.match(/Chrome\/([\d.]+)/) || ua.match(/CriOS\/([\d.]+)/);
	        var firefox = ua.match(/Firefox\/([\d.]+)/);
	        // var safari = webkit && ua.match(/Mobile\//) && !chrome;
	        // var webview = ua.match(/(iPhone|iPod|iPad).*AppleWebKit(?!.*Safari)/) && !chrome;
	        var ie = ua.match(/MSIE\s([\d.]+)/)
	            // IE 11 Trident/7.0; rv:11.0
	            || ua.match(/Trident\/.+?rv:(([\d.]+))/);
	        var edge = ua.match(/Edge\/([\d.]+)/); // IE 12 and 12+

	        var weChat = (/micromessenger/i).test(ua);

	        // Todo: clean this up with a better OS/browser seperation:
	        // - discern (more) between multiple browsers on android
	        // - decide if kindle fire in silk mode is android or not
	        // - Firefox on Android doesn't specify the Android version
	        // - possibly devide in os, device and browser hashes

	        // if (browser.webkit = !!webkit) browser.version = webkit[1];

	        // if (android) os.android = true, os.version = android[2];
	        // if (iphone && !ipod) os.ios = os.iphone = true, os.version = iphone[2].replace(/_/g, '.');
	        // if (ipad) os.ios = os.ipad = true, os.version = ipad[2].replace(/_/g, '.');
	        // if (ipod) os.ios = os.ipod = true, os.version = ipod[3] ? ipod[3].replace(/_/g, '.') : null;
	        // if (webos) os.webos = true, os.version = webos[2];
	        // if (touchpad) os.touchpad = true;
	        // if (blackberry) os.blackberry = true, os.version = blackberry[2];
	        // if (bb10) os.bb10 = true, os.version = bb10[2];
	        // if (rimtabletos) os.rimtabletos = true, os.version = rimtabletos[2];
	        // if (playbook) browser.playbook = true;
	        // if (kindle) os.kindle = true, os.version = kindle[1];
	        // if (silk) browser.silk = true, browser.version = silk[1];
	        // if (!silk && os.android && ua.match(/Kindle Fire/)) browser.silk = true;
	        // if (chrome) browser.chrome = true, browser.version = chrome[1];
	        if (firefox) {
	            browser.firefox = true;
	            browser.version = firefox[1];
	        }
	        // if (safari && (ua.match(/Safari/) || !!os.ios)) browser.safari = true;
	        // if (webview) browser.webview = true;

	        if (ie) {
	            browser.ie = true;
	            browser.version = ie[1];
	        }

	        if (edge) {
	            browser.edge = true;
	            browser.version = edge[1];
	        }

	        // It is difficult to detect WeChat in Win Phone precisely, because ua can
	        // not be set on win phone. So we do not consider Win Phone.
	        if (weChat) {
	            browser.weChat = true;
	        }

	        // os.tablet = !!(ipad || playbook || (android && !ua.match(/Mobile/)) ||
	        //     (firefox && ua.match(/Tablet/)) || (ie && !ua.match(/Phone/) && ua.match(/Touch/)));
	        // os.phone  = !!(!os.tablet && !os.ipod && (android || iphone || webos ||
	        //     (chrome && ua.match(/Android/)) || (chrome && ua.match(/CriOS\/([\d.]+)/)) ||
	        //     (firefox && ua.match(/Mobile/)) || (ie && ua.match(/Touch/))));

	        return {
	            browser: browser,
	            os: os,
	            node: false,
	            // é˜ç†ºæ•“canvasé€îˆ›å¯”é”›å±¾æ•¼é‹ä½ºî¬éé€›ç°¡
	            // canvasSupported : !(browser.ie && parseFloat(browser.version) < 9)
	            canvasSupported : document.createElement('canvas').getContext ? true : false,
	            // @see <http://stackoverflow.com/questions/4817029/whats-the-best-way-to-detect-a-touch-screen-device-using-javascript>
	            // works on most browsers
	            // IE10/11 does not support touch event, and MS Edge supports them but not by
	            // default, so we dont check navigator.maxTouchPoints for them here.
	            touchEventsSupported: 'ontouchstart' in window && !browser.ie && !browser.edge,
	            // <http://caniuse.com/#search=pointer%20event>.
	            pointerEventsSupported: 'onpointerdown' in window
	                // Firefox supports pointer but not by default, only MS browsers are reliable on pointer
	                // events currently. So we dont use that on other browsers unless tested sufficiently.
	                // Although IE 10 supports pointer event, it use old style and is different from the
	                // standard. So we exclude that. (IE 10 is hardly used on touch device)
	                && (browser.edge || (browser.ie && browser.version >= 11))
	        };
	    }


/***/ },
/* 48 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * é¦å—™å¹†
	 * @module zrender/graphic/shape/Ring
	 */


	    module.exports = __webpack_require__(10).extend({

	        type: 'ring',

	        shape: {
	            cx: 0,
	            cy: 0,
	            r: 0,
	            r0: 0
	        },

	        buildPath: function (ctx, shape) {
	            var x = shape.cx;
	            var y = shape.cy;
	            var PI2 = Math.PI * 2;
	            ctx.moveTo(x + shape.r, y);
	            ctx.arc(x, y, shape.r, 0, PI2, false);
	            ctx.moveTo(x + shape.r0, y);
	            ctx.arc(x, y, shape.r0, 0, PI2, true);
	        }
	    });



/***/ },
/* 49 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * æ¾¶æ°³ç«Ÿè¤°ï¿½
	 * @module zrender/shape/Polygon
	 */


	    var polyHelper = __webpack_require__(50);

	    module.exports = __webpack_require__(10).extend({
	        
	        type: 'polygon',

	        shape: {
	            points: null,

	            smooth: false,

	            smoothConstraint: null
	        },

	        buildPath: function (ctx, shape) {
	            polyHelper.buildPath(ctx, shape, true);
	        }
	    });


/***/ },
/* 50 */
/***/ function(module, exports, __webpack_require__) {

	

	    var smoothSpline = __webpack_require__(51);
	    var smoothBezier = __webpack_require__(52);

	    module.exports = {
	        buildPath: function (ctx, shape, closePath) {
	            var points = shape.points;
	            var smooth = shape.smooth;
	            if (points && points.length >= 2) {
	                if (smooth && smooth !== 'spline') {
	                    var controlPoints = smoothBezier(
	                        points, smooth, closePath, shape.smoothConstraint
	                    );

	                    ctx.moveTo(points[0][0], points[0][1]);
	                    var len = points.length;
	                    for (var i = 0; i < (closePath ? len : len - 1); i++) {
	                        var cp1 = controlPoints[i * 2];
	                        var cp2 = controlPoints[i * 2 + 1];
	                        var p = points[(i + 1) % len];
	                        ctx.bezierCurveTo(
	                            cp1[0], cp1[1], cp2[0], cp2[1], p[0], p[1]
	                        );
	                    }
	                }
	                else {
	                    if (smooth === 'spline') {
	                        points = smoothSpline(points, closePath);
	                    }

	                    ctx.moveTo(points[0][0], points[0][1]);
	                    for (var i = 1, l = points.length; i < l; i++) {
	                        ctx.lineTo(points[i][0], points[i][1]);
	                    }
	                }

	                closePath && ctx.closePath();
	            }
	        }
	    };


/***/ },
/* 51 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * Catmull-Rom spline éŽ»æŽ‘â‚¬å…¼å§Œç»¾ï¿½
	 * @module zrender/shape/util/smoothSpline
	 * @author pissang (https://www.github.com/pissang)
	 *         Kener (@Kener-é‹æ¥€å˜², kener.linfeng@gmail.com)
	 *         errorrik (errorrik@gmail.com)
	 */

	    var vec2 = __webpack_require__(18);

	    /**
	     * @inner
	     */
	    function interpolate(p0, p1, p2, p3, t, t2, t3) {
	        var v0 = (p2 - p0) * 0.5;
	        var v1 = (p3 - p1) * 0.5;
	        return (2 * (p1 - p2) + v0 + v1) * t3
	                + (-3 * (p1 - p2) - 2 * v0 - v1) * t2
	                + v0 * t + p1;
	    }

	    /**
	     * @alias module:zrender/shape/util/smoothSpline
	     * @param {Array} points ç»¾æŒŽî†Œæ¤¤å‰å£éæ‰®ç²
	     * @param {boolean} isLoop
	     * @return {Array}
	     */
	    module.exports = function (points, isLoop) {
	        var len = points.length;
	        var ret = [];

	        var distance = 0;
	        for (var i = 1; i < len; i++) {
	            distance += vec2.distance(points[i - 1], points[i]);
	        }

	        var segs = distance / 2;
	        segs = segs < len ? len : segs;
	        for (var i = 0; i < segs; i++) {
	            var pos = i / (segs - 1) * (isLoop ? len : len - 1);
	            var idx = Math.floor(pos);

	            var w = pos - idx;

	            var p0;
	            var p1 = points[idx % len];
	            var p2;
	            var p3;
	            if (!isLoop) {
	                p0 = points[idx === 0 ? idx : idx - 1];
	                p2 = points[idx > len - 2 ? len - 1 : idx + 1];
	                p3 = points[idx > len - 3 ? len - 1 : idx + 2];
	            }
	            else {
	                p0 = points[(idx - 1 + len) % len];
	                p2 = points[(idx + 1) % len];
	                p3 = points[(idx + 2) % len];
	            }

	            var w2 = w * w;
	            var w3 = w * w2;

	            ret.push([
	                interpolate(p0[0], p1[0], p2[0], p3[0], w, w2, w3),
	                interpolate(p0[1], p1[1], p2[1], p3[1], w, w2, w3)
	            ]);
	        }
	        return ret;
	    };



/***/ },
/* 52 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * ç’æ¿†î”£çæ–¿é’©å©Šæˆžæ´¸ç»¾ï¿½
	 * @module zrender/shape/util/smoothBezier
	 * @author pissang (https://www.github.com/pissang)
	 *         Kener (@Kener-é‹æ¥€å˜², kener.linfeng@gmail.com)
	 *         errorrik (errorrik@gmail.com)
	 */


	    var vec2 = __webpack_require__(18);
	    var v2Min = vec2.min;
	    var v2Max = vec2.max;
	    var v2Scale = vec2.scale;
	    var v2Distance = vec2.distance;
	    var v2Add = vec2.add;

	    /**
	     * ç’æ¿†î”£çæ–¿é’©å©Šæˆžæ´¸ç»¾ï¿½
	     * @alias module:zrender/shape/util/smoothBezier
	     * @param {Array} points ç»¾æŒŽî†Œæ¤¤å‰å£éæ‰®ç²
	     * @param {number} smooth éªžè™«ç²¦ç»›å¤Œéª‡, 0-1
	     * @param {boolean} isLoop
	     * @param {Array} constraint çå—šî…¸ç» æ¥€åš­é‰ãƒ§æ®‘éŽºÑƒåŸ—éåœ­å®³é‰ç†·æ¹ªæ¶“â‚¬æ¶“î„å¯˜é¥å¯¸æ´…éï¿½
	     *                           å§£æ–¿î›§ [[0, 0], [100, 100]], æ©æ¬Žé‡œé–å‘­æ´¿é©æŽç´°æ¶“ï¿½
	     *                           éç¿ é‡œéŽ¶æ¨¼åšŽé¨å‹«å¯˜é¥å¯¸æ´…é‹æ°«ç«´æ¶“î„è‹Ÿé—†å—™æ•¤é‰ãƒ§å®³é‰ç†¸å¸¶é’å‰å£éŠ†ï¿½
	     * @param {Array} ç’ï¼„ç•»é‘çƒ˜æ½µé¨å‹¬å¸¶é’å‰å£éæ‰®ç²
	     */
	    module.exports = function (points, smooth, isLoop, constraint) {
	        var cps = [];

	        var v = [];
	        var v1 = [];
	        var v2 = [];
	        var prevPoint;
	        var nextPoint;

	        var min, max;
	        if (constraint) {
	            min = [Infinity, Infinity];
	            max = [-Infinity, -Infinity];
	            for (var i = 0, len = points.length; i < len; i++) {
	                v2Min(min, min, points[i]);
	                v2Max(max, max, points[i]);
	            }
	            // æ¶“åº¢å¯šç€¹æ°±æ®‘é–å‘­æ´¿é©æŽ‘ä»›éªžå •æ³¦
	            v2Min(min, min, constraint[0]);
	            v2Max(max, max, constraint[1]);
	        }

	        for (var i = 0, len = points.length; i < len; i++) {
	            var point = points[i];

	            if (isLoop) {
	                prevPoint = points[i ? i - 1 : len - 1];
	                nextPoint = points[(i + 1) % len];
	            }
	            else {
	                if (i === 0 || i === len - 1) {
	                    cps.push(vec2.clone(points[i]));
	                    continue;
	                }
	                else {
	                    prevPoint = points[i - 1];
	                    nextPoint = points[i + 1];
	                }
	            }

	            vec2.sub(v, nextPoint, prevPoint);

	            // use degree to scale the handle length
	            v2Scale(v, v, smooth);

	            var d0 = v2Distance(point, prevPoint);
	            var d1 = v2Distance(point, nextPoint);
	            var sum = d0 + d1;
	            if (sum !== 0) {
	                d0 /= sum;
	                d1 /= sum;
	            }

	            v2Scale(v1, v, -d0);
	            v2Scale(v2, v, d1);
	            var cp0 = v2Add([], point, v1);
	            var cp1 = v2Add([], point, v2);
	            if (constraint) {
	                v2Max(cp0, cp0, min);
	                v2Min(cp0, cp0, max);
	                v2Max(cp1, cp1, min);
	                v2Min(cp1, cp1, max);
	            }
	            cps.push(cp0);
	            cps.push(cp1);
	        }

	        if (isLoop) {
	            cps.push(cps.shift());
	        }

	        return cps;
	    };



/***/ },
/* 53 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * @module zrender/graphic/shape/Polyline
	 */


	    var polyHelper = __webpack_require__(50);

	    module.exports = __webpack_require__(10).extend({
	        
	        type: 'polyline',

	        shape: {
	            points: null,

	            smooth: false,

	            smoothConstraint: null
	        },

	        style: {
	            stroke: '#000',

	            fill: null
	        },

	        buildPath: function (ctx, shape) {
	            polyHelper.buildPath(ctx, shape, false);
	        }
	    });


/***/ },
/* 54 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * é­â•èˆ°
	 * @module zrender/graphic/shape/Rect
	 */


	    var roundRectHelper = __webpack_require__(55);

	    module.exports = __webpack_require__(10).extend({

	        type: 'rect',

	        shape: {
	            // å®¸ï¸¿ç¬‚éŠ†ä½¸å½¸æ¶“å¨¿â‚¬ä½¸å½¸æ¶“å¬¨â‚¬ä½¸ä¹æ¶“å¬­î—é¨å‹«å´å¯°å‹ªç··å¨†â€²è´Ÿr1éŠ†ä¹º2éŠ†ä¹º3éŠ†ä¹º4
	            // rç¼‚â•å•“æ¶“ï¿½1         é©ç¨¿ç¶‹æµœï¿½ [1, 1, 1, 1]
	            // rç¼‚â•å•“æ¶“ç¯¬1]       é©ç¨¿ç¶‹æµœï¿½ [1, 1, 1, 1]
	            // rç¼‚â•å•“æ¶“ç¯¬1, 2]    é©ç¨¿ç¶‹æµœï¿½ [1, 2, 1, 2]
	            // rç¼‚â•å•“æ¶“ç¯¬1, 2, 3] é©ç¨¿ç¶‹æµœï¿½ [1, 2, 3, 2]
	            r: 0,

	            x: 0,
	            y: 0,
	            width: 0,
	            height: 0
	        },

	        buildPath: function (ctx, shape) {
	            var x = shape.x;
	            var y = shape.y;
	            var width = shape.width;
	            var height = shape.height;
	            if (!shape.r) {
	                ctx.rect(x, y, width, height);
	            }
	            else {
	                roundRectHelper.buildPath(ctx, shape);
	            }
	            ctx.closePath();
	            return;
	        }
	    });



/***/ },
/* 55 */
/***/ function(module, exports) {

	

	    module.exports = {
	        buildPath: function (ctx, shape) {
	            var x = shape.x;
	            var y = shape.y;
	            var width = shape.width;
	            var height = shape.height;
	            var r = shape.r;
	            var r1;
	            var r2;
	            var r3;
	            var r4;

	            // Convert width and height to positive for better borderRadius
	            if (width < 0) {
	                x = x + width;
	                width = -width;
	            }
	            if (height < 0) {
	                y = y + height;
	                height = -height;
	            }

	            if (typeof r === 'number') {
	                r1 = r2 = r3 = r4 = r;
	            }
	            else if (r instanceof Array) {
	                if (r.length === 1) {
	                    r1 = r2 = r3 = r4 = r[0];
	                }
	                else if (r.length === 2) {
	                    r1 = r3 = r[0];
	                    r2 = r4 = r[1];
	                }
	                else if (r.length === 3) {
	                    r1 = r[0];
	                    r2 = r4 = r[1];
	                    r3 = r[2];
	                }
	                else {
	                    r1 = r[0];
	                    r2 = r[1];
	                    r3 = r[2];
	                    r4 = r[3];
	                }
	            }
	            else {
	                r1 = r2 = r3 = r4 = 0;
	            }

	            var total;
	            if (r1 + r2 > width) {
	                total = r1 + r2;
	                r1 *= width / total;
	                r2 *= width / total;
	            }
	            if (r3 + r4 > width) {
	                total = r3 + r4;
	                r3 *= width / total;
	                r4 *= width / total;
	            }
	            if (r2 + r3 > height) {
	                total = r2 + r3;
	                r2 *= height / total;
	                r3 *= height / total;
	            }
	            if (r1 + r4 > height) {
	                total = r1 + r4;
	                r1 *= height / total;
	                r4 *= height / total;
	            }
	            ctx.moveTo(x + r1, y);
	            ctx.lineTo(x + width - r2, y);
	            r2 !== 0 && ctx.quadraticCurveTo(
	                x + width, y, x + width, y + r2
	            );
	            ctx.lineTo(x + width, y + height - r3);
	            r3 !== 0 && ctx.quadraticCurveTo(
	                x + width, y + height, x + width - r3, y + height
	            );
	            ctx.lineTo(x + r4, y + height);
	            r4 !== 0 && ctx.quadraticCurveTo(
	                x, y + height, x, y + height - r4
	            );
	            ctx.lineTo(x, y + r1);
	            r1 !== 0 && ctx.quadraticCurveTo(x, y, x + r1, y);
	        }
	    };


/***/ },
/* 56 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * é©å¯¸åšŽ
	 * @module zrender/graphic/shape/Line
	 */

	    module.exports = __webpack_require__(10).extend({

	        type: 'line',

	        shape: {
	            // Start point
	            x1: 0,
	            y1: 0,
	            // End point
	            x2: 0,
	            y2: 0,

	            percent: 1
	        },

	        style: {
	            stroke: '#000',
	            fill: null
	        },

	        buildPath: function (ctx, shape) {
	            var x1 = shape.x1;
	            var y1 = shape.y1;
	            var x2 = shape.x2;
	            var y2 = shape.y2;
	            var percent = shape.percent;

	            if (percent === 0) {
	                return;
	            }

	            ctx.moveTo(x1, y1);

	            if (percent < 1) {
	                x2 = x1 * (1 - percent) + x2 * percent;
	                y2 = y1 * (1 - percent) + y2 * percent;
	            }
	            ctx.lineTo(x2, y2);
	        },

	        /**
	         * Get point at percent
	         * @param  {number} percent
	         * @return {Array.<number>}
	         */
	        pointAt: function (p) {
	            var shape = this.shape;
	            return [
	                shape.x1 * (1 - p) + shape.x2 * p,
	                shape.y1 * (1 - p) + shape.y2 * p
	            ];
	        }
	    });



/***/ },
/* 57 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	/**
	 * ç’æ¿†î”£çæ—€æ´¸ç»¾ï¿½
	 * @module zrender/shape/BezierCurve
	 */


	    var curveTool = __webpack_require__(30);
	    var vec2 = __webpack_require__(18);
	    var quadraticSubdivide = curveTool.quadraticSubdivide;
	    var cubicSubdivide = curveTool.cubicSubdivide;
	    var quadraticAt = curveTool.quadraticAt;
	    var cubicAt = curveTool.cubicAt;
	    var quadraticDerivativeAt = curveTool.quadraticDerivativeAt;
	    var cubicDerivativeAt = curveTool.cubicDerivativeAt;

	    var out = [];

	    function someVectorAt(shape, t, isTangent) {
	        var cpx2 = shape.cpx2;
	        var cpy2 = shape.cpy2;
	        if (cpx2 === null || cpy2 === null) {
	            return [
	                (isTangent ? cubicDerivativeAt : cubicAt)(shape.x1, shape.cpx1, shape.cpx2, shape.x2, t),
	                (isTangent ? cubicDerivativeAt : cubicAt)(shape.y1, shape.cpy1, shape.cpy2, shape.y2, t)
	            ];
	        }
	        else {
	            return [
	                (isTangent ? quadraticDerivativeAt : quadraticAt)(shape.x1, shape.cpx1, shape.x2, t),
	                (isTangent ? quadraticDerivativeAt : quadraticAt)(shape.y1, shape.cpy1, shape.y2, t)
	            ];
	        }
	    }
	    module.exports = __webpack_require__(10).extend({

	        type: 'bezier-curve',

	        shape: {
	            x1: 0,
	            y1: 0,
	            x2: 0,
	            y2: 0,
	            cpx1: 0,
	            cpy1: 0,
	            // cpx2: 0,
	            // cpy2: 0

	            // Curve show percent, for animating
	            percent: 1
	        },

	        style: {
	            stroke: '#000',
	            fill: null
	        },

	        buildPath: function (ctx, shape) {
	            var x1 = shape.x1;
	            var y1 = shape.y1;
	            var x2 = shape.x2;
	            var y2 = shape.y2;
	            var cpx1 = shape.cpx1;
	            var cpy1 = shape.cpy1;
	            var cpx2 = shape.cpx2;
	            var cpy2 = shape.cpy2;
	            var percent = shape.percent;
	            if (percent === 0) {
	                return;
	            }

	            ctx.moveTo(x1, y1);

	            if (cpx2 == null || cpy2 == null) {
	                if (percent < 1) {
	                    quadraticSubdivide(
	                        x1, cpx1, x2, percent, out
	                    );
	                    cpx1 = out[1];
	                    x2 = out[2];
	                    quadraticSubdivide(
	                        y1, cpy1, y2, percent, out
	                    );
	                    cpy1 = out[1];
	                    y2 = out[2];
	                }

	                ctx.quadraticCurveTo(
	                    cpx1, cpy1,
	                    x2, y2
	                );
	            }
	            else {
	                if (percent < 1) {
	                    cubicSubdivide(
	                        x1, cpx1, cpx2, x2, percent, out
	                    );
	                    cpx1 = out[1];
	                    cpx2 = out[2];
	                    x2 = out[3];
	                    cubicSubdivide(
	                        y1, cpy1, cpy2, y2, percent, out
	                    );
	                    cpy1 = out[1];
	                    cpy2 = out[2];
	                    y2 = out[3];
	                }
	                ctx.bezierCurveTo(
	                    cpx1, cpy1,
	                    cpx2, cpy2,
	                    x2, y2
	                );
	            }
	        },

	        /**
	         * Get point at percent
	         * @param  {number} t
	         * @return {Array.<number>}
	         */
	        pointAt: function (t) {
	            return someVectorAt(this.shape, t, false);
	        },

	        /**
	         * Get tangent at percent
	         * @param  {number} t
	         * @return {Array.<number>}
	         */
	        tangentAt: function (t) {
	            var p = someVectorAt(this.shape, t, true);
	            return vec2.normalize(p, p);
	        }
	    });



/***/ },
/* 58 */
/***/ function(module, exports, __webpack_require__) {

	/**
	 * é¦å——å§¬
	 * @module zrender/graphic/shape/Arc
	 */
	 

	    module.exports = __webpack_require__(10).extend({

	        type: 'arc',

	        shape: {

	            cx: 0,

	            cy: 0,

	            r: 0,

	            startAngle: 0,

	            endAngle: Math.PI * 2,

	            clockwise: true
	        },

	        style: {

	            stroke: '#000',

	            fill: null
	        },

	        buildPath: function (ctx, shape) {

	            var x = shape.cx;
	            var y = shape.cy;
	            var r = Math.max(shape.r, 0);
	            var startAngle = shape.startAngle;
	            var endAngle = shape.endAngle;
	            var clockwise = shape.clockwise;

	            var unitX = Math.cos(startAngle);
	            var unitY = Math.sin(startAngle);

	            ctx.moveTo(unitX * r + x, unitY * r + y);
	            ctx.arc(x, y, r, startAngle, endAngle, !clockwise);
	        }
	    });


/***/ },
/* 59 */
/***/ function(module, exports, __webpack_require__) {

	// CompoundPath to improve performance


	    var Path = __webpack_require__(10);
	    module.exports = Path.extend({

	        type: 'compound',

	        shape: {

	            paths: null
	        },

	        _updatePathDirty: function () {
	            var dirtyPath = this.__dirtyPath;
	            var paths = this.shape.paths;
	            for (var i = 0; i < paths.length; i++) {
	                // Mark as dirty if any subpath is dirty
	                dirtyPath = dirtyPath || paths[i].__dirtyPath;
	            }
	            this.__dirtyPath = dirtyPath;
	            this.__dirty = this.__dirty || dirtyPath;
	        },

	        beforeBrush: function () {
	            this._updatePathDirty();
	            var paths = this.shape.paths || [];
	            var scale = this.getGlobalScale();
	            // Update path scale
	            for (var i = 0; i < paths.length; i++) {
	                paths[i].path.setScale(scale[0], scale[1]);
	            }
	        },

	        buildPath: function (ctx, shape) {
	            var paths = shape.paths || [];
	            for (var i = 0; i < paths.length; i++) {
	                paths[i].buildPath(ctx, paths[i].shape, true);
	            }
	        },

	        afterBrush: function () {
	            var paths = this.shape.paths;
	            for (var i = 0; i < paths.length; i++) {
	                paths[i].__dirtyPath = false;
	            }
	        },

	        getBoundingRect: function () {
	            this._updatePathDirty();
	            return Path.prototype.getBoundingRect.call(this);
	        }
	    });


/***/ },
/* 60 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';


	    var zrUtil = __webpack_require__(5);

	    var Gradient = __webpack_require__(61);

	    /**
	     * x, y, x2, y2 are all percent from 0 to 1
	     * @param {number} [x=0]
	     * @param {number} [y=0]
	     * @param {number} [x2=1]
	     * @param {number} [y2=0]
	     * @param {Array.<Object>} colorStops
	     * @param {boolean} [globalCoord=false]
	     */
	    var LinearGradient = function (x, y, x2, y2, colorStops, globalCoord) {
	        this.x = x == null ? 0 : x;

	        this.y = y == null ? 0 : y;

	        this.x2 = x2 == null ? 1 : x2;

	        this.y2 = y2 == null ? 0 : y2;

	        // Can be cloned
	        this.type = 'linear';

	        // If use global coord
	        this.global = globalCoord || false;

	        Gradient.call(this, colorStops);
	    };

	    LinearGradient.prototype = {

	        constructor: LinearGradient
	    };

	    zrUtil.inherits(LinearGradient, Gradient);

	    module.exports = LinearGradient;


/***/ },
/* 61 */
/***/ function(module, exports) {

	

	    /**
	     * @param {Array.<Object>} colorStops
	     */
	    var Gradient = function (colorStops) {

	        this.colorStops = colorStops || [];
	    };

	    Gradient.prototype = {

	        constructor: Gradient,

	        addColorStop: function (offset, color) {
	            this.colorStops.push({

	                offset: offset,

	                color: color
	            });
	        }
	    };

	    module.exports = Gradient;


/***/ },
/* 62 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';


	    var zrUtil = __webpack_require__(5);

	    var Gradient = __webpack_require__(61);

	    /**
	     * x, y, r are all percent from 0 to 1
	     * @param {number} [x=0.5]
	     * @param {number} [y=0.5]
	     * @param {number} [r=0.5]
	     * @param {Array.<Object>} [colorStops]
	     * @param {boolean} [globalCoord=false]
	     */
	    var RadialGradient = function (x, y, r, colorStops, globalCoord) {
	        this.x = x == null ? 0.5 : x;

	        this.y = y == null ? 0.5 : y;

	        this.r = r == null ? 0.5 : r;

	        // Can be cloned
	        this.type = 'radial';

	        // If use global coord
	        this.global = globalCoord || false;

	        Gradient.call(this, colorStops);
	    };

	    RadialGradient.prototype = {

	        constructor: RadialGradient
	    };

	    zrUtil.inherits(RadialGradient, Gradient);

	    module.exports = RadialGradient;


/***/ },
/* 63 */
/***/ function(module, exports, __webpack_require__) {

	var echarts = __webpack_require__(2);

	module.exports = echarts.graphic.extendShape({
	    type: 'ec-liquid-fill',

	    shape: {
	        waveLength: 0,
	        radius: 0,
	        cx: 0,
	        cy: 0,
	        waterLevel: 0,
	        amplitude: 0,
	        phase: 0,
	        inverse: false
	    },

	    style: {
	        fill: '#0f0'
	    },

	    buildPath: function (ctx, shape) {
	        var curves = Math.ceil(2 * shape.radius / shape.waveLength * 4) * 2;
	        var controls = [[0, 0]];
	        var positions = [];

	        // map phase to [-Math.PI * 2, 0]
	        while (shape.phase < -Math.PI * 2) {
	            shape.phase += Math.PI * 2;
	        }
	        while (shape.phase > 0) {
	            shape.phase -= Math.PI * 2;
	        }
	        var phase = shape.phase / Math.PI / 2 * shape.waveLength;

	        var left = shape.cx - shape.radius + phase - shape.radius * 2;

	        /**
	         * top-left corner as start point
	         *
	         * draws this point
	         *  |
	         * \|/
	         *  ~~~~~~~~
	         *  |      |
	         *  +------+
	         */
	        ctx.moveTo(left, shape.waterLevel);

	        /**
	         * top wave
	         *
	         * ~~~~~~~~ <- draws this sine wave
	         * |      |
	         * +------+
	         */
	        var waveLeft = 0;
	        var waveRight = 0;
	        for (var c = 0; c < curves; ++c) {
	            var stage = c % 4;
	            var pos = getWaterPositions(c * shape.waveLength / 4, stage,
	                shape.waveLength, shape.amplitude);
	            ctx.bezierCurveTo(pos[0][0] + left, -pos[0][1] + shape.waterLevel,
	                pos[1][0] + left, -pos[1][1] + shape.waterLevel,
	                pos[2][0] + left, -pos[2][1] + shape.waterLevel);

	            if (c === curves - 1) {
	                waveRight = pos[2][0];
	            }
	        }

	        if (shape.inverse) {
	            /**
	             * top-right corner
	             *                  2. draws this line
	             *                          |
	             *                       +------+
	             * 3. draws this line -> |      | <- 1. draws this line
	             *                       ~~~~~~~~
	             */
	            ctx.lineTo(waveRight + left, shape.cy - shape.radius);
	            ctx.lineTo(left, shape.cy - shape.radius);
	            ctx.lineTo(left, shape.waterLevel);
	        }
	        else {
	            /**
	             * top-right corner
	             *
	             *                       ~~~~~~~~
	             * 3. draws this line -> |      | <- 1. draws this line
	             *                       +------+
	             *                          ^
	             *                          |
	             *                  2. draws this line
	             */
	            ctx.lineTo(waveRight + left, shape.cy + shape.radius);
	            ctx.lineTo(left, shape.cy + shape.radius);
	            ctx.lineTo(left, shape.waterLevel);
	        }

	        ctx.closePath();
	    }
	});



	/**
	 * Using Bezier curves to fit sine wave.
	 * There is 4 control points for each curve of wave,
	 * which is at 1/4 wave length of the sine wave.
	 *
	 * The control points for a wave from (a) to (d) are a-b-c-d:
	 *          c *----* d
	 *     b *
	 *       |
	 * ... a * ..................
	 *
	 * whose positions are a: (0, 0), b: (0.5, 0.5), c: (1, 1), d: (PI / 2, 1)
	 *
	 * @param {number} x          x position of the left-most point (a)
	 * @param {number} stage      0-3, stating which part of the wave it is
	 * @param {number} waveLength wave length of the sine wave
	 * @param {number} amplitude  wave amplitude
	 */
	function getWaterPositions(x, stage, waveLength, amplitude) {
	    if (stage === 0) {
	        return [
	            [x + 1 / 2 * waveLength / Math.PI / 2, amplitude / 2],
	            [x + 1 / 2 * waveLength / Math.PI,     amplitude],
	            [x + waveLength / 4,                   amplitude]
	        ];
	    }
	    else if (stage === 1) {
	        return [
	            [x + 1 / 2 * waveLength / Math.PI / 2 * (Math.PI - 2),
	            amplitude],
	            [x + 1 / 2 * waveLength / Math.PI / 2 * (Math.PI - 1),
	            amplitude / 2],
	            [x + waveLength / 4,                   0]
	        ]
	    }
	    else if (stage === 2) {
	        return [
	            [x + 1 / 2 * waveLength / Math.PI / 2, -amplitude / 2],
	            [x + 1 / 2 * waveLength / Math.PI,     -amplitude],
	            [x + waveLength / 4,                   -amplitude]
	        ]
	    }
	    else {
	        return [
	            [x + 1 / 2 * waveLength / Math.PI / 2 * (Math.PI - 2),
	            -amplitude],
	            [x + 1 / 2 * waveLength / Math.PI / 2 * (Math.PI - 1),
	            -amplitude / 2],
	            [x + waveLength / 4,                   0]
	        ]
	    }
	}


/***/ },
/* 64 */
/***/ function(module, exports) {

	// Pick color from palette for each data item


	    module.exports = function (seriesType, ecModel) {
	        // Pie and funnel may use diferrent scope
	        var paletteScope = {};
	        ecModel.eachRawSeriesByType(seriesType, function (seriesModel) {
	            var dataAll = seriesModel.getRawData();
	            var idxMap = {};
	            if (!ecModel.isSeriesFiltered(seriesModel)) {
	                var data = seriesModel.getData();
	                data.each(function (idx) {
	                    var rawIdx = data.getRawIndex(idx);
	                    idxMap[rawIdx] = idx;
	                });
	                dataAll.each(function (rawIdx) {
	                    // FIXME Performance
	                    var itemModel = dataAll.getItemModel(rawIdx);
	                    var filteredIdx = idxMap[rawIdx];

	                    // If series.itemStyle.normal.color is a function. itemVisual may be encoded
	                    var singleDataColor = filteredIdx != null
	                        && data.getItemVisual(filteredIdx, 'color', true);

	                    if (!singleDataColor) {
	                        var color = itemModel.get('itemStyle.normal.color')
	                            || seriesModel.getColorFromPalette(dataAll.getName(rawIdx), paletteScope);
	                        // Legend may use the visual info in data before processed
	                        dataAll.setItemVisual(rawIdx, 'color', color);

	                        // Data is not filtered
	                        if (filteredIdx != null) {
	                            data.setItemVisual(filteredIdx, 'color', color);
	                        }
	                    }
	                    else {
	                        // Set data all color for legend
	                        dataAll.setItemVisual(rawIdx, 'color', singleDataColor);
	                    }
	                });
	            }
	        });
	    };


/***/ }
/******/ ])
});
;