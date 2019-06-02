// Transcrypt'ed from Python, 2019-06-03 00:26:34
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {juld_to_tert} from './imperial_calendar.transform.juld_to_tert.js';
import {TerrestrialTime} from './imperial_calendar.TerrestrialTime.js';
import {JulianDay} from './imperial_calendar.JulianDay.js';
var __name__ = 'imperial_calendar.transform.tert_to_juld';
export var tert_to_juld = function (tert) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'tert': var tert = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var delta_t = JulianDay (tert.terrestrial_time).delta_t;
	var juld_prime = JulianDay (tert.terrestrial_time - delta_t / ((24 * 60) * 60));
	var tert_prime = juld_to_tert (juld_prime);
	return JulianDay ((juld_prime.julian_day + tert.terrestrial_time) - tert_prime.terrestrial_time);
};

//# sourceMappingURL=imperial_calendar.transform.tert_to_juld.map