// Transcrypt'ed from Python, 2019-05-01 01:24:09
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {app, h} from './node_modules.hyperapp.src.index.js';
import {SolNumber} from './imperial_calendar.SolNumber.js';
import {ImperialDateTime} from './imperial_calendar.ImperialDateTime.js';
import {imperial_date_time_to_sol_number, sol_number_to_imperial_date_time} from './imperial_calendar.js';
var __name__ = '__main__';
export var action_sync_by_sol_number = function (state, event) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'state': var state = __allkwargs0__ [__attrib0__]; break;
					case 'event': var event = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	event.stopPropagation ();
	event.preventDefault ();
	var sol_number = SolNumber (float (document.getElementById (state ['sol_number_ref']).value));
	var imperial_date_time = sol_number_to_imperial_date_time (state.sol_number);
	return dict ({'sol_number': sol_number, 'imperial_date_time': imperial_date_time});
};
export var action_sync_by_imperial_date_time = function (state, event) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'state': var state = __allkwargs0__ [__attrib0__]; break;
					case 'event': var event = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	event.stopPropagation ();
	event.preventDefault ();
	var imperial_date_time = ImperialDateTime (int (document.getElementById (state ['imperial_date_time_year_ref']).value), int (document.getElementById (state ['imperial_date_time_month_ref']).value), int (document.getElementById (state ['imperial_date_time_day_ref']).value), int (document.getElementById (state ['imperial_date_time_hour_ref']).value), int (document.getElementById (state ['imperial_date_time_minute_ref']).value), int (document.getElementById (state ['imperial_date_time_second_ref']).value));
	var sol_number = imperial_date_time_to_sol_number (imperial_date_time);
	return dict ({'sol_number': sol_number, 'imperial_date_time': imperial_date_time});
};
export var view = function (state, actions) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'state': var state = __allkwargs0__ [__attrib0__]; break;
					case 'actions': var actions = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return h ('div', dict ({}), [h ('div', dict ({}), [h ('label', dict ({'for': state ['sol_number_ref']}), 'SolNumber: '), h ('input', dict ({'id': state ['sol_number_ref'], 'step': '0.00001', 'type': 'number', 'value': state ['sol_number'].sol_number}), ''), h ('button', dict ({'onclick': (function __lambda__ (event) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'event': var event = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return actions ['sync_by_sol_number'] (event);
	})}), 'Sync')]), h ('div', dict ({}), [h ('label', dict ({'for': state ['imperial_date_time_year_ref']}), 'ImperialDateTime: '), h ('input', dict ({'id': state ['imperial_date_time_year_ref'], 'type': 'number', 'value': state ['imperial_date_time'].year}), ''), h ('span', dict ({}), '-'), h ('input', dict ({'id': state ['imperial_date_time_month_ref'], 'type': 'number', 'value': state ['imperial_date_time'].month}), ''), h ('span', dict ({}), '-'), h ('input', dict ({'id': state ['imperial_date_time_day_ref'], 'type': 'number', 'value': state ['imperial_date_time'].day}), ''), h ('span', dict ({}), 'T'), h ('input', dict ({'id': state ['imperial_date_time_hour_ref'], 'type': 'number', 'value': state ['imperial_date_time'].hour}), ''), h ('span', dict ({}), ':'), h ('input', dict ({'id': state ['imperial_date_time_minute_ref'], 'type': 'number', 'value': state ['imperial_date_time'].minute}), ''), h ('span', dict ({}), ':'), h ('input', dict ({'id': state ['imperial_date_time_second_ref'], 'type': 'number', 'value': state ['imperial_date_time'].second}), ''), h ('button', dict ({'onclick': (function __lambda__ (event) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'event': var event = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return actions ['sync_by_imperial_date_time'] (event);
	})}), 'Sync')])]);
};
export var main = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	var sol_number = SolNumber (0);
	var state = dict ({'sol_number': sol_number, 'sol_number_ref': 'sol_number' + Math.random (), 'imperial_date_time': sol_number_to_imperial_date_time (sol_number), 'imperial_date_time_year_ref': 'imperial_date_time_year' + Math.random (), 'imperial_date_time_month_ref': 'imperial_date_time_month' + Math.random (), 'imperial_date_time_day_ref': 'imperial_date_time_day' + Math.random (), 'imperial_date_time_hour_ref': 'imperial_date_time_hour' + Math.random (), 'imperial_date_time_minute_ref': 'imperial_date_time_minute' + Math.random (), 'imperial_date_time_second_ref': 'imperial_date_time_second' + Math.random ()});
	var actions = dict ({'sync_by_sol_number': (function __lambda__ (event) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'event': var event = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return (function __lambda__ (state) {
			if (arguments.length) {
				var __ilastarg0__ = arguments.length - 1;
				if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
					var __allkwargs0__ = arguments [__ilastarg0__--];
					for (var __attrib0__ in __allkwargs0__) {
						switch (__attrib0__) {
							case 'state': var state = __allkwargs0__ [__attrib0__]; break;
						}
					}
				}
			}
			else {
			}
			return action_sync_by_sol_number (state, event);
		});
	}), 'sync_by_imperial_date_time': (function __lambda__ (event) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'event': var event = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return (function __lambda__ (state) {
			if (arguments.length) {
				var __ilastarg0__ = arguments.length - 1;
				if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
					var __allkwargs0__ = arguments [__ilastarg0__--];
					for (var __attrib0__ in __allkwargs0__) {
						switch (__attrib0__) {
							case 'state': var state = __allkwargs0__ [__attrib0__]; break;
						}
					}
				}
			}
			else {
			}
			return action_sync_by_imperial_date_time (state, event);
		});
	})});
	app (state, actions, view, document.getElementById ('app'));
};

//# sourceMappingURL=main.map