// Transcrypt'ed from Python, 2019-05-01 03:11:10
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
import {SolNumber} from './imperial_calendar.SolNumber.js';
import {ImperialYear} from './imperial_calendar.ImperialYear.js';
import {ImperialMonth} from './imperial_calendar.ImperialMonth.js';
import {ImperialDateTime} from './imperial_calendar.ImperialDateTime.js';
export {ImperialMonth, ImperialYear, ImperialDateTime, SolNumber};
var __name__ = 'imperial_calendar';
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
export var imperial_year_to_sol_number_table = [0];
for (var year = 0; year < 999; year++) {
	imperial_year_to_sol_number_table.insert (year + 1, ImperialYear (year).days ());
}
export var imperial_millennium_days = sum (imperial_year_to_sol_number_table) + ImperialYear (999).days ();
var imperial_year_to_sol_number_table = sums (imperial_year_to_sol_number_table);
export var imperial_month_to_sol_number_table = [0];
for (var month = 1; month < 24; month++) {
	imperial_month_to_sol_number_table.insert (month, ImperialMonth (month).days ());
}
var imperial_month_to_sol_number_table = sums (imperial_month_to_sol_number_table);
export var sol_number_to_imperial_date_time = function (sol_number) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'sol_number': var sol_number = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var __left0__ = divmod (sol_number.date, imperial_millennium_days);
	var millennium = __left0__ [0];
	var days_in_millennium = __left0__ [1];
	var years_in_millennium = len (list (filter ((function __lambda__ (x) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return x <= days_in_millennium;
	}), imperial_year_to_sol_number_table))) - 1;
	var days_before_new_years_day = imperial_year_to_sol_number_table [years_in_millennium];
	var days_in_year = days_in_millennium - days_before_new_years_day;
	var month = len (list (filter ((function __lambda__ (x) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return x <= days_in_year;
	}), imperial_month_to_sol_number_table)));
	var days_before_first_day_of_the_month = imperial_month_to_sol_number_table [month - 1];
	return ImperialDateTime (millennium * 1000 + years_in_millennium, month, (days_in_year - days_before_first_day_of_the_month) + 1, math.floor (sol_number.time * 24), math.floor (__mod__ ((sol_number.time * 24) * 60, 60)), math.floor (__mod__ (((sol_number.time * 24) * 60) * 60, 60)));
};
export var imperial_date_time_to_sol_number = function (imperial_date_time) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'imperial_date_time': var imperial_date_time = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var days_of_millennium = (Math.floor (imperial_date_time.year / 1000)) * imperial_millennium_days;
	var days_in_millennium = imperial_year_to_sol_number_table [__mod__ (imperial_date_time.year, 1000)];
	var days_in_year = imperial_month_to_sol_number_table [imperial_date_time.month - 1];
	var decimal_time = (imperial_date_time.hour / 24 + imperial_date_time.minute / (24 * 60)) + imperial_date_time.second / ((24 * 60) * 60);
	return SolNumber ((((days_of_millennium + days_in_millennium) + days_in_year) + (imperial_date_time.day - 1)) + decimal_time);
};
export var __all__ = ['ImperialDateTime', 'ImperialMonth', 'ImperialYear', 'imperial_date_time_to_sol_number', 'SolNumber', 'sol_number_to_imperial_date_time'];

//# sourceMappingURL=imperial_calendar.map