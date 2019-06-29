// Transcrypt'ed from Python, 2019-06-29 12:32:33
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {app, h} from './node_modules.hyperapp.src.index.js';
import {__all__, grdt_to_juld, imdt_to_imsn, imsn_to_imdt, imsn_to_mrsd, juld_to_grdt, juld_to_tert, mrsd_to_imsn, mrsd_to_tert, tert_to_juld, tert_to_mrls, tert_to_mrsd} from './imperial_calendar.transform.js';
import {GregorianDateTime, ImperialDateTime, ImperialMonth, ImperialSolNumber, ImperialYear, JulianDay, MarsSolDate, TerrestrialTime} from './imperial_calendar.js';
var __name__ = '__main__';
export var new_ref = function (prefix) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'prefix': var prefix = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var ref = '{}.{}{}'.format (prefix, Date.now ().toString (36), Math.random ().toString (36).substr (1));
	return ref;
};
export var action_sync_by_grdt = function (state, event) {
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
	var ref = state ['grdt_ref'];
	var grdt = GregorianDateTime (int (document.getElementById (ref + 'year').value), int (document.getElementById (ref + 'month').value), int (document.getElementById (ref + 'day').value), int (document.getElementById (ref + 'hour').value), int (document.getElementById (ref + 'minute').value), int (document.getElementById (ref + 'second').value), GregorianDateTime.parse_timezone_str (document.getElementById (ref + 'timezone').value));
	var juld = grdt_to_juld (grdt);
	var tert = juld_to_tert (juld);
	var mrsd = tert_to_mrsd (tert);
	var imsn = mrsd_to_imsn (mrsd);
	var imdt = imsn_to_imdt (imsn, 0.0);
	return dict ({'grdt': grdt, 'juld': juld, 'tert': tert, 'mrsd': mrsd, 'imsn': imsn, 'imdt': imdt});
};
export var action_sync_by_juld = function (state, event) {
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
	var ref = state ['juld_ref'];
	var juld = JulianDay (float (document.getElementById (ref).value));
	var grdt = juld_to_grdt (juld, 0.0);
	var tert = juld_to_tert (juld);
	var mrsd = tert_to_mrsd (tert);
	var imsn = mrsd_to_imsn (mrsd);
	var imdt = imsn_to_imdt (imsn, 0.0);
	return dict ({'grdt': grdt, 'juld': juld, 'tert': tert, 'mrsd': mrsd, 'imsn': imsn, 'imdt': imdt});
};
export var action_sync_by_tert = function (state, event) {
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
	var ref = state ['tert_ref'];
	var tert = TerrestrialTime (float (document.getElementById (ref).value));
	var juld = tert_to_juld (tert);
	var grdt = juld_to_grdt (juld, 0.0);
	var mrsd = tert_to_mrsd (tert);
	var imsn = mrsd_to_imsn (mrsd);
	var imdt = imsn_to_imdt (imsn, 0.0);
	return dict ({'grdt': grdt, 'juld': juld, 'tert': tert, 'mrsd': mrsd, 'imsn': imsn, 'imdt': imdt});
};
export var action_sync_by_mrsd = function (state, event) {
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
	var ref = state ['mrsd_ref'];
	var mrsd = MarsSolDate (float (document.getElementById (ref).value));
	var tert = mrsd_to_tert (mrsd);
	var juld = tert_to_juld (tert);
	var grdt = juld_to_grdt (juld, 0.0);
	var imsn = mrsd_to_imsn (mrsd);
	var imdt = imsn_to_imdt (imsn, 0.0);
	return dict ({'grdt': grdt, 'juld': juld, 'tert': tert, 'mrsd': mrsd, 'imsn': imsn, 'imdt': imdt});
};
export var action_sync_by_imsn = function (state, event) {
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
	var ref = state ['imsn_ref'];
	var imsn = ImperialSolNumber (float (document.getElementById (ref).value));
	var mrsd = imsn_to_mrsd (imsn);
	var tert = mrsd_to_tert (mrsd);
	var juld = tert_to_juld (tert);
	var grdt = juld_to_grdt (juld, 0.0);
	var imdt = imsn_to_imdt (imsn, 0.0);
	return dict ({'grdt': grdt, 'juld': juld, 'tert': tert, 'mrsd': mrsd, 'imsn': imsn, 'imdt': imdt});
};
export var action_sync_by_imdt = function (state, event) {
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
	var ref = state ['imdt_ref'];
	var imdt = ImperialDateTime (int (document.getElementById (ref + 'year').value), int (document.getElementById (ref + 'month').value), int (document.getElementById (ref + 'day').value), int (document.getElementById (ref + 'hour').value), int (document.getElementById (ref + 'minute').value), int (document.getElementById (ref + 'second').value), ImperialDateTime.parse_timezone_str (document.getElementById (ref + 'timezone').value));
	var imsn = imdt_to_imsn (imdt);
	var mrsd = imsn_to_mrsd (imsn);
	var tert = mrsd_to_tert (mrsd);
	var juld = tert_to_juld (tert);
	var grdt = juld_to_grdt (juld, 0.0);
	return dict ({'grdt': grdt, 'juld': juld, 'tert': tert, 'mrsd': mrsd, 'imsn': imsn, 'imdt': imdt});
};
export var view_grdt = function (state, actions) {
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
	var grdt = state ['grdt'];
	var ref = state ['grdt_ref'];
	return h ('div', dict ({'class': 'field is-grouped is-grouped-multiline'}), [h ('label', dict ({'class': 'label', 'for': ref + 'year'}), 'Gregorian Date Time'), h ('input', dict ({'id': ref + 'year', 'class': 'input', 'style': dict ({'width': '6em'}), 'type': 'number', 'value': grdt.year}), ''), '-', h ('input', dict ({'id': ref + 'month', 'class': 'input', 'max': 12, 'min': 1, 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': grdt.month}), ''), '-', h ('input', dict ({'id': ref + 'day', 'class': 'input', 'max': 31, 'min': 1, 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': grdt.day}), ''), 'T', h ('input', dict ({'id': ref + 'hour', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': grdt.hour}), ''), ':', h ('input', dict ({'id': ref + 'minute', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': grdt.minute}), ''), ':', h ('input', dict ({'id': ref + 'second', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': grdt.second}), ''), h ('input', dict ({'id': ref + 'timezone', 'class': 'input', 'style': dict ({'width': '6em'}), 'type': 'text', 'value': grdt.timezone_str}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
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
		return actions ['sync_by_grdt'] (event);
	})}), 'Sync')]);
};
export var view_juld = function (state, actions) {
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
	var juld = state ['juld'];
	var ref = state ['juld_ref'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('label', dict ({'class': 'label', 'for': ref}), 'Julian Day'), h ('input', dict ({'id': ref, 'class': 'input', 'step': 1e-05, 'type': 'number', 'value': juld.julian_day}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
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
		return actions ['sync_by_juld'] (event);
	})}), 'Sync')]);
};
export var view_delta_t = function (state, actions) {
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
	var juld = state ['juld'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('div', dict ({'class': 'label'}), '⊿t'), str (juld.delta_t)]);
};
export var view_tert = function (state, actions) {
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
	var tert = state ['tert'];
	var ref = state ['tert_ref'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('label', dict ({'class': 'label', 'for': ref}), 'Terrestrual Time'), h ('input', dict ({'id': ref, 'class': 'input', 'step': 1e-05, 'type': 'number', 'value': tert.terrestrial_time}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
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
		return actions ['sync_by_tert'] (event);
	})}), 'Sync')]);
};
export var view_mrls = function (state, actions) {
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
	var tert = state ['tert'];
	var mrls = tert_to_mrls (tert);
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('label', dict ({'class': 'label'}), 'Areocentric Solar Longitude (Mars Ls)'), str (mrls)]);
};
export var view_mrsd = function (state, actions) {
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
	var mrsd = state ['mrsd'];
	var ref = state ['mrsd_ref'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('label', dict ({'class': 'label', 'for': ref}), 'Mars Sol Date'), h ('input', dict ({'id': ref, 'class': 'input', 'step': 1e-05, 'type': 'number', 'value': mrsd.mars_sol_date}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
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
		return actions ['sync_by_mrsd'] (event);
	})}), 'Sync')]);
};
export var view_imperial_imsn = function (state, actions) {
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
	var imsn = state ['imsn'];
	var ref = state ['imsn_ref'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('label', dict ({'class': 'label', 'for': ref}), 'Imperial Sol Number'), h ('input', dict ({'id': ref, 'class': 'input', 'step': 1e-05, 'type': 'number', 'value': imsn.imperial_sol_number}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
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
		return actions ['sync_by_imsn'] (event);
	})}), 'Sync')]);
};
export var view_imdt = function (state, actions) {
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
	var imdt = state ['imdt'];
	var ref = state ['imdt_ref'];
	return h ('div', dict ({'class': 'field is-grouped is-grouped-multiline'}), [h ('label', dict ({'class': 'label', 'for': ref + 'year'}), 'Imperial Date Time'), h ('input', dict ({'id': ref + 'year', 'class': 'input', 'style': dict ({'width': '6em'}), 'type': 'number', 'value': imdt.year}), ''), '-', h ('input', dict ({'id': ref + 'month', 'class': 'input', 'max': 24, 'min': 1, 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': imdt.month}), ''), '-', h ('input', dict ({'id': ref + 'day', 'class': 'input', 'max': 28, 'min': 1, 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': imdt.day}), ''), 'T', h ('input', dict ({'id': ref + 'hour', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': imdt.hour}), ''), ':', h ('input', dict ({'id': ref + 'minute', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': imdt.minute}), ''), ':', h ('input', dict ({'id': ref + 'second', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': imdt.second}), ''), h ('input', dict ({'id': ref + 'timezone', 'class': 'input', 'style': dict ({'width': '6em'}), 'type': 'text', 'value': imdt.timezone_str}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
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
		return actions ['sync_by_imdt'] (event);
	})}), 'Sync')]);
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
	return h ('div', dict ({}), [view_grdt, view_juld, view_delta_t, view_tert, view_mrls, view_mrsd, view_imperial_imsn, view_imdt]);
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
	var grdt = GregorianDateTime (0, 1, 1, 0, 0, 0, 0.0);
	var juld = grdt_to_juld (grdt);
	var tert = juld_to_tert (juld);
	var mrsd = tert_to_mrsd (tert);
	var imsn = mrsd_to_imsn (mrsd);
	var imdt = imsn_to_imdt (imsn, 0.0);
	var state = dict ({'grdt': grdt, 'grdt_ref': new_ref ('grdt'), 'juld': juld, 'juld_ref': new_ref ('juld'), 'tert': tert, 'tert_ref': new_ref ('tert'), 'mrsd': mrsd, 'mrsd_ref': new_ref ('mrsd'), 'imsn': imsn, 'imsn_ref': new_ref ('imsn'), 'imdt': imdt, 'imdt_ref': new_ref ('imdt')});
	var actions = dict ({'sync_by_grdt': (function __lambda__ (event) {
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
			return action_sync_by_grdt (state, event);
		});
	}), 'sync_by_juld': (function __lambda__ (event) {
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
			return action_sync_by_juld (state, event);
		});
	}), 'sync_by_tert': (function __lambda__ (event) {
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
			return action_sync_by_tert (state, event);
		});
	}), 'sync_by_mrsd': (function __lambda__ (event) {
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
			return action_sync_by_mrsd (state, event);
		});
	}), 'sync_by_imsn': (function __lambda__ (event) {
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
			return action_sync_by_imsn (state, event);
		});
	}), 'sync_by_imdt': (function __lambda__ (event) {
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
			return action_sync_by_imdt (state, event);
		});
	})});
	app (state, actions, view, document.getElementById ('app'));
};

//# sourceMappingURL=main.map