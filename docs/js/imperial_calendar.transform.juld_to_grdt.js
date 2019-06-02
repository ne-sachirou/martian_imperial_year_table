// Transcrypt'ed from Python, 2019-06-03 00:26:34
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
import {JulianDay} from './imperial_calendar.JulianDay.js';
import {GregorianDateTime} from './imperial_calendar.GregorianDateTime.js';
var __name__ = 'imperial_calendar.transform.juld_to_grdt';
export var juld_to_grdt = function (juld, timezone) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'juld': var juld = __allkwargs0__ [__attrib0__]; break;
					case 'timezone': var timezone = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var A = math.floor ((juld.julian_day + timezone / 24) + 68569.5);
	var B = (juld.julian_day + timezone / 24) + 0.5;
	var a = math.floor (A / 36524.25);
	var b = A - math.floor (36524.25 * a + 0.75);
	var c = math.floor ((b + 1) / 365.25025);
	var d = (b - math.floor (365.25 * c)) + 31;
	var e = math.floor (d / 30.59);
	var f = math.floor (e / 11);
	var u = (100 * (a - 49) + c) + f;
	var v = (e - 12 * f) + 2;
	var w = (d - math.floor (30.59 * e)) + __mod__ (B, 1);
	var x = (__mod__ (w, 1)) * 24;
	var y = (__mod__ (x, 1)) * 60;
	var z = (__mod__ (y, 1)) * 60;
	return GregorianDateTime (u, v, math.floor (w), math.floor (x), math.floor (y), math.floor (z), timezone);
};

//# sourceMappingURL=imperial_calendar.transform.juld_to_grdt.map