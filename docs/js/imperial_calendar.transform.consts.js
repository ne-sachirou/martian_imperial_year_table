// Transcrypt'ed from Python, 2019-06-03 01:38:32
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {ImperialYear} from './imperial_calendar.ImperialYear.js';
import {ImperialMonth} from './imperial_calendar.ImperialMonth.js';
var __name__ = 'imperial_calendar.transform.consts';
export var sums = function (lst) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'lst': var lst = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var s = 0;
	var sums = [];
	for (var item of lst) {
		s += item;
		sums.append (s);
	}
	return sums;
};
export var imperial_year_to_imsn_table = [0];
for (var year = 0; year < 999; year++) {
	imperial_year_to_imsn_table.insert (year + 1, ImperialYear (year).days ());
}
export var imperial_millennium_days = sum (imperial_year_to_imsn_table) + ImperialYear (999).days ();
var imperial_year_to_imsn_table = sums (imperial_year_to_imsn_table);
export var imperial_month_to_imsn_table = [0];
for (var month = 1; month < 24; month++) {
	imperial_month_to_imsn_table.insert (month, ImperialMonth (month).days ());
}
var imperial_month_to_imsn_table = sums (imperial_month_to_imsn_table);

//# sourceMappingURL=imperial_calendar.transform.consts.map