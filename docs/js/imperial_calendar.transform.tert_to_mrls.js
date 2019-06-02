// Transcrypt'ed from Python, 2019-06-03 00:26:34
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
import {TerrestrialTime} from './imperial_calendar.TerrestrialTime.js';
var __name__ = 'imperial_calendar.transform.tert_to_mrls';
export var tert_to_offset_t_j2000 = function (tert) {
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
	return tert.terrestrial_time - 2451545.0;
};
export var offset_t_j2000_to_mars_mean_anomaly = function (offset_t_j2000) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'offset_t_j2000': var offset_t_j2000 = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return 19.3871 + 0.52402073 * offset_t_j2000;
};
export var offset_t_j2000_to_angle_of_fictitious_mean_sun = function (offset_t_j2000) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'offset_t_j2000': var offset_t_j2000 = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return 270.3871 + 0.524038496 * offset_t_j2000;
};
export var offset_t_j2000_to_perturbers = function (offset_t_j2000) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'offset_t_j2000': var offset_t_j2000 = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var amp = [0.0071, 0.0057, 0.0039, 0.0037, 0.0021, 0.002, 0.0018];
	var tau = [2.2353, 2.7543, 1.1177, 15.7866, 2.1354, 2.4694, 32.8493];
	var phi = [49.409, 168.173, 191.837, 21.736, 15.704, 95.528, 49.095];
	var perturbers = 0;
	for (var i = 0; i < len (amp); i++) {
		var angle = ((360 / 365.25) * offset_t_j2000) / tau [i] + phi [i];
		perturbers += amp [i] * math.cos (math.radians (angle));
	}
	return perturbers;
};
export var offset_t_j2000_to_equation_of_center = function (offset_t_j2000) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'offset_t_j2000': var offset_t_j2000 = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var m_m_a = offset_t_j2000_to_mars_mean_anomaly (offset_t_j2000);
	var angle_m = math.radians (m_m_a);
	var pbs = offset_t_j2000_to_perturbers (offset_t_j2000);
	return (((((10.691 + (3.0 * Math.pow (10, -(7))) * offset_t_j2000) * math.sin (angle_m) + 0.623 * math.sin (2 * angle_m)) + 0.05 * math.sin (3 * angle_m)) + 0.005 * math.sin (4 * angle_m)) + 0.0005 * math.sin (5 * angle_m)) + pbs;
};
export var offset_t_j2000_to_areocentric_solar_longitude = function (offset_t_j2000) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'offset_t_j2000': var offset_t_j2000 = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return __mod__ (offset_t_j2000_to_angle_of_fictitious_mean_sun (offset_t_j2000) + offset_t_j2000_to_equation_of_center (offset_t_j2000), 360);
};
export var tert_to_mrls = function (tert) {
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
	return offset_t_j2000_to_areocentric_solar_longitude (tert_to_offset_t_j2000 (tert));
};

//# sourceMappingURL=imperial_calendar.transform.tert_to_mrls.map