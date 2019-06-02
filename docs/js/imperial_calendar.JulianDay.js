// Transcrypt'ed from Python, 2019-06-03 00:26:34
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {juld_to_grdt} from './imperial_calendar.transform.juld_to_grdt.js';
import {grdt_to_juld} from './imperial_calendar.transform.grdt_to_juld.js';
import {GregorianDateTime} from './imperial_calendar.GregorianDateTime.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
var __name__ = 'imperial_calendar.JulianDay';
export var julian_day_to_julian_year = function (juld) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'juld': var juld = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var julian_day_to_julian_year_intercept = 1721117.5;
	var tweaked_julian_day = juld.julian_day - julian_day_to_julian_year_intercept;
	var quadrennium = divmod (tweaked_julian_day, 365 * 4 + 1);
	if (quadrennium [1] < 365) {
		var quadrennial_year = 0;
	}
	else if (quadrennium [1] < 365 * 2) {
		var quadrennial_year = 1;
	}
	else if (quadrennium [1] < 365 * 3) {
		var quadrennial_year = 2;
	}
	else {
		var quadrennial_year = 3;
	}
	var julian_year = quadrennium [0] * 4 + quadrennial_year;
	var annual_day = quadrennium [1] - quadrennial_year * 365;
	if (annual_day >= 306) {
		julian_year++;
		annual_day -= 306;
	}
	else if (__mod__ (julian_year, 4) == 0) {
		annual_day += 31 + 29;
	}
	else {
		annual_day += 31 + 28;
	}
	if (__mod__ (julian_year, 4) == 0) {
		julian_year += annual_day / 366;
	}
	else {
		julian_year += annual_day / 365;
	}
	return julian_year;
};
export var julian_day_to_gregorian_year = function (juld) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'juld': var juld = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var year = juld_to_grdt (juld, 0).year;
	var january_1st = grdt_to_juld (GregorianDateTime (year, 1, 1, 0, 0, 0, 0));
	var next_january_1st = grdt_to_juld (GregorianDateTime (year + 1, 1, 1, 0, 0, 0, 0));
	var annual_day = (juld.julian_day - january_1st.julian_day) / (next_january_1st.julian_day - january_1st.julian_day);
	return year + annual_day;
};
export var JulianDay =  __class__ ('JulianDay', [object], {
	__module__: __name__,
	calendar_reform: 2299160.5,
	get __init__ () {return __get__ (this, function (self, julian_day) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'julian_day': var julian_day = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.julian_day = julian_day;
	});},
	get __eq__ () {return __get__ (this, function (self, other) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'other': var other = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (!(isinstance (other, JulianDay))) {
			return false;
		}
		return math.isclose (self.julian_day, other.julian_day, __kwargtrans__ ({abs_tol: 1e-05}));
	});},
	get _get_delta_t () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (self.julian_day < self.calendar_reform) {
			var year_number = julian_day_to_julian_year (self);
		}
		else {
			var year_number = julian_day_to_gregorian_year (self);
		}
		if (year_number < -(500)) {
			var delta_u = (year_number - 1820) / 100;
			return -(20) + 32 * Math.pow (delta_u, 2);
		}
		else if (year_number < 500) {
			var delta_u = year_number / 100;
			return (((((10583.6 - 1014.41 * delta_u) + 33.78311 * Math.pow (delta_u, 2)) - 5.952053 * Math.pow (delta_u, 3)) - 0.1798452 * Math.pow (delta_u, 4)) + 0.022174192 * Math.pow (delta_u, 5)) + 0.0090316521 * Math.pow (delta_u, 6);
		}
		else if (year_number < 1600) {
			var delta_u = (year_number - 1000) / 100;
			return (((((1574.2 - 556.01 * delta_u) + 71.23472 * Math.pow (delta_u, 2)) + 0.319781 * Math.pow (delta_u, 3)) - 0.8503463 * Math.pow (delta_u, 4)) - 0.005050998 * Math.pow (delta_u, 5)) + 0.0083572073 * Math.pow (delta_u, 6);
		}
		else if (year_number < 1700) {
			var delta_u = year_number - 1600;
			return ((120 - 0.9808 * delta_u) - 0.01532 * Math.pow (delta_u, 2)) + Math.pow (delta_u, 3) / 7129;
		}
		else if (year_number < 1800) {
			var delta_u = year_number - 1700;
			return (((8.83 + 0.1603 * delta_u) - 0.0059285 * Math.pow (delta_u, 2)) + 0.00013336 * Math.pow (delta_u, 3)) - Math.pow (delta_u, 4) / 1174000;
		}
		else if (year_number < 1860) {
			var delta_u = year_number - 1800;
			return ((((((13.72 - 0.332447 * delta_u) + 0.0068612 * Math.pow (delta_u, 2)) + 0.0041116 * Math.pow (delta_u, 3)) - 0.00037436 * Math.pow (delta_u, 4)) + 1.21272e-05 * Math.pow (delta_u, 5)) - 1.699e-07 * Math.pow (delta_u, 6)) + 8.75e-10 * Math.pow (delta_u, 7);
		}
		else if (year_number < 1900) {
			var delta_u = year_number - 1860;
			return ((((7.62 + 0.5737 * delta_u) - 0.251754 * Math.pow (delta_u, 2)) + 0.01680668 * Math.pow (delta_u, 3)) - 0.0004473624 * Math.pow (delta_u, 4)) + Math.pow (delta_u, 5) / 233174;
		}
		else if (year_number < 1920) {
			var delta_u = year_number - 1900;
			return (((-(2.79) + 1.494119 * delta_u) - 0.0598939 * Math.pow (delta_u, 2)) + 0.0061966 * Math.pow (delta_u, 3)) - 0.000197 * Math.pow (delta_u, 4);
		}
		else if (year_number < 1941) {
			var delta_u = year_number - 1920;
			return ((21.2 + 0.84493 * delta_u) - 0.0761 * Math.pow (delta_u, 2)) + 0.0020936 * Math.pow (delta_u, 3);
		}
		else if (year_number < 1961) {
			var delta_u = year_number - 1950;
			return ((29.07 + 0.407 * delta_u) - Math.pow (delta_u, 2) / 233) + Math.pow (delta_u, 3) / 2547;
		}
		else if (year_number < 1986) {
			var delta_u = year_number - 1975;
			return ((45.45 + 1.067 * delta_u) - Math.pow (delta_u, 2) / 260) - Math.pow (delta_u, 3) / 718;
		}
		else if (year_number < 2005) {
			var delta_u = year_number - 2000;
			return ((((63.86 + 0.3345 * delta_u) - 0.060734 * Math.pow (delta_u, 2)) + 0.0017275 * Math.pow (delta_u, 3)) + 0.000651814 * Math.pow (delta_u, 4)) + 2.373599e-05 * Math.pow (delta_u, 5);
		}
		else if (year_number < 2050) {
			var delta_u = year_number - 2000;
			return (63.795 + 0.1287 * delta_u) + 0.0091 * Math.pow (delta_u, 2);
		}
		else if (year_number < 2150) {
			return (-(20) + 32 * Math.pow ((year_number - 1820) / 100, 2)) - 0.5628 * (2150 - year_number);
		}
		else {
			var delta_u = (year_number - 1820) / 100;
			return -(20) + 32 * Math.pow (delta_u, 2);
		}
	});}
});
Object.defineProperty (JulianDay, 'delta_t', property.call (JulianDay, JulianDay._get_delta_t));;

//# sourceMappingURL=imperial_calendar.JulianDay.map