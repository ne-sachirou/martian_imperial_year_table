// Transcrypt'ed from Python, 2019-06-03 00:26:34
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {imperial_millennium_days, imperial_month_to_imsn_table, imperial_year_to_imsn_table} from './imperial_calendar.transform.consts.js';
import {ImperialSolNumber} from './imperial_calendar.ImperialSolNumber.js';
import {ImperialDateTime} from './imperial_calendar.ImperialDateTime.js';
var __name__ = 'imperial_calendar.transform.imdt_to_imsn';
export var imdt_to_imsn = function (imdt) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'imdt': var imdt = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var days_of_millennium = (Math.floor (imdt.year / 1000)) * imperial_millennium_days;
	var days_in_millennium = imperial_year_to_imsn_table [__mod__ (imdt.year, 1000)];
	var days_in_year = imperial_month_to_imsn_table [imdt.month - 1];
	var decimal_time = (imdt.hour / 24 + imdt.minute / (24 * 60)) + imdt.second / ((24 * 60) * 60);
	return ImperialSolNumber (((((days_of_millennium + days_in_millennium) + days_in_year) + (imdt.day - 1)) + decimal_time) - imdt.timezone / 24);
};

//# sourceMappingURL=imperial_calendar.transform.imdt_to_imsn.map