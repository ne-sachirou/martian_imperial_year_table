// Transcrypt'ed from Python, 2019-04-21 18:24:50
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
import {SolNumber} from './martian_calendar.SolNumber.js';
import {MartianYear} from './martian_calendar.MartianYear.js';
import {MartianMonth} from './martian_calendar.MartianMonth.js';
import {MartianDateTime} from './martian_calendar.MartianDateTime.js';
export {SolNumber, MartianDateTime, MartianMonth, MartianYear};
var __name__ = 'martian_calendar';
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
export var martian_year_to_sol_number_table = [0];
for (var year = 0; year < 999; year++) {
	martian_year_to_sol_number_table.insert (year + 1, MartianYear (year).days ());
}
export var martian_millennium_days = sum (martian_year_to_sol_number_table) + MartianYear (999).days ();
var martian_year_to_sol_number_table = sums (martian_year_to_sol_number_table);
export var martian_month_to_sol_number_table = [0];
for (var month = 1; month < 24; month++) {
	martian_month_to_sol_number_table.insert (month, MartianMonth (month).days ());
}
var martian_month_to_sol_number_table = sums (martian_month_to_sol_number_table);
export var sol_number_to_martian_date_time = function (sol_number) {
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
	var __left0__ = divmod (sol_number.date, martian_millennium_days);
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
	}), martian_year_to_sol_number_table))) - 1;
	var days_before_new_years_day = martian_year_to_sol_number_table [years_in_millennium];
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
	}), martian_month_to_sol_number_table)));
	var days_before_first_day_of_the_month = martian_month_to_sol_number_table [month - 1];
	return MartianDateTime (millennium * 1000 + years_in_millennium, month, (days_in_year - days_before_first_day_of_the_month) + 1, math.floor (sol_number.time * 24), math.floor (__mod__ ((sol_number.time * 24) * 60, 60)), math.floor (__mod__ (((sol_number.time * 24) * 60) * 60, 60)));
};
export var martian_date_time_to_sol_number = function (martian_date_time) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'martian_date_time': var martian_date_time = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var days_of_millennium = (Math.floor (martian_date_time.year / 1000)) * martian_millennium_days;
	var days_in_millennium = martian_year_to_sol_number_table [__mod__ (martian_date_time.year, 1000)];
	var days_in_year = martian_month_to_sol_number_table [martian_date_time.month - 1];
	var decimal_time = (martian_date_time.hour / 24 + martian_date_time.minute / (24 * 60)) + martian_date_time.second / ((24 * 60) * 60);
	return SolNumber ((((days_of_millennium + days_in_millennium) + days_in_year) + (martian_date_time.day - 1)) + decimal_time);
};
export var __all__ = ['MartianDateTime', 'MartianMonth', 'MartianYear', 'martian_date_time_to_sol_number', 'SolNumber', 'sol_number_to_martian_date_time'];

//# sourceMappingURL=martian_calendar.map