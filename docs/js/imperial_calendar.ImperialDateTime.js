// Transcrypt'ed from Python, 2019-06-03 00:40:54
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'imperial_calendar.ImperialDateTime';
export var ImperialDateTime =  __class__ ('ImperialDateTime', [object], {
	__module__: __name__,
	get parse_timezone_str () {return __getcm__ (this, function (cls, timezone_str) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'cls': var cls = __allkwargs0__ [__attrib0__]; break;
						case 'timezone_str': var timezone_str = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return 0.0;
	});},
	get __init__ () {return __get__ (this, function (self, year, month, day, hour, minute, second, timezone) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'year': var year = __allkwargs0__ [__attrib0__]; break;
						case 'month': var month = __allkwargs0__ [__attrib0__]; break;
						case 'day': var day = __allkwargs0__ [__attrib0__]; break;
						case 'hour': var hour = __allkwargs0__ [__attrib0__]; break;
						case 'minute': var minute = __allkwargs0__ [__attrib0__]; break;
						case 'second': var second = __allkwargs0__ [__attrib0__]; break;
						case 'timezone': var timezone = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.year = year;
		self.month = month;
		self.day = day;
		self.hour = hour;
		self.minute = minute;
		self.second = second;
		self.timezone = timezone;
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
		if (!(isinstance (other, ImperialDateTime))) {
			return false;
		}
		return self.__dict__ == other.__dict__;
	});},
	get _get_timezone_str () {return __get__ (this, function (self) {
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
		return '+00:00';
	});}
});
Object.defineProperty (ImperialDateTime, 'timezone_str', property.call (ImperialDateTime, ImperialDateTime._get_timezone_str));;

//# sourceMappingURL=imperial_calendar.ImperialDateTime.map