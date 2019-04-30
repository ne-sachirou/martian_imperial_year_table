// Transcrypt'ed from Python, 2019-04-30 23:29:32
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {app, h} from './node_modules.hyperapp.src.index.js';
import {SolNumber} from './martian_calendar.SolNumber.js';
import {sol_number_to_martian_date_time} from './martian_calendar.js';
var __name__ = '__main__';
export var action_sol_number_to_martian_date_time = function (state, event) {
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
	return dict ({'sol_number': SolNumber (float (document.getElementById (state ['sol_number_ref']).value))});
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
	var martian_date_time = sol_number_to_martian_date_time (state.sol_number);
	return h ('div', dict ({}), [h ('form', dict ({}), [h ('div', dict ({}), [h ('label', dict ({'for': state ['sol_number_ref']}), 'SolNumber: '), h ('input', dict ({'id': state ['sol_number_ref'], 'step': '0.00001', 'type': 'number', 'value': state ['sol_number'].sol_number}), '')]), h ('button', dict ({'onclick': (function __lambda__ (event) {
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
		return actions ['sol_number_to_martian_date_time'] (event);
	})}), 'to MartianDateTime')]), h ('div', dict ({}), 'MartianDateTime: {}-{}-{}T{}:{}:{}'.format (martian_date_time.year, martian_date_time.month, martian_date_time.day, martian_date_time.hour, martian_date_time.minute, martian_date_time.second))]);
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
	var state = dict ({'sol_number': SolNumber (0), 'sol_number_ref': 'sol_number_ref' + Math.random ()});
	var actions = dict ({'sol_number_to_martian_date_time': (function __lambda__ (event) {
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
			return action_sol_number_to_martian_date_time (state, event);
		});
	})});
	app (state, actions, view, document.getElementById ('app'));
};

//# sourceMappingURL=main.map