// Transcrypt'ed from Python, 2019-06-02 22:59:41
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
import {JulianDay} from './imperial_calendar.JulianDay.js';
import {GregorianDateTime} from './imperial_calendar.GregorianDateTime.js';
var __name__ = 'imperial_calendar.transform.grdt_to_juld';
export var grdt_to_juld = function (grdt) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'grdt': var grdt = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	if (__in__ (grdt.month, [1, 2])) {
		var tweaked_year = grdt.year - 1;
		var tweaked_month = grdt.month + 12;
	}
	else {
		var tweaked_year = grdt.year;
		var tweaked_month = grdt.month;
	}
	return JulianDay (((((((((math.floor (tweaked_year * 365.25) + math.floor (tweaked_year / 400)) - math.floor (tweaked_year / 100)) + math.floor ((tweaked_month - 2) * 30.59)) + grdt.day) + grdt.hour / 24) + grdt.minute / (24 * 60)) + grdt.second / ((24 * 60) * 60)) - grdt.timezone / 24) + grdt.intercept);
};

//# sourceMappingURL=imperial_calendar.transform.grdt_to_juld.map