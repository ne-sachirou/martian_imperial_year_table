// Transcrypt'ed from Python, 2019-06-29 15:01:11
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {h} from './node_modules.hyperapp.src.index.js';
export {h};
var __name__ = 'ui.view';
export var view_grdt = function (state, actions) {
	var grdt = state ['grdt'];
	var ref = state ['grdt_ref'];
	return h ('div', dict ({'class': 'field is-grouped is-grouped-multiline'}), [h ('label', dict ({'class': 'label', 'for': ref + 'year'}), 'Gregorian Date Time'), h ('input', dict ({'id': ref + 'year', 'class': 'input', 'style': dict ({'width': '6em'}), 'type': 'number', 'value': grdt.year}), ''), '-', h ('input', dict ({'id': ref + 'month', 'class': 'input', 'max': 12, 'min': 1, 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': grdt.month}), ''), '-', h ('input', dict ({'id': ref + 'day', 'class': 'input', 'max': 31, 'min': 1, 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': grdt.day}), ''), 'T', h ('input', dict ({'id': ref + 'hour', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': grdt.hour}), ''), ':', h ('input', dict ({'id': ref + 'minute', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': grdt.minute}), ''), ':', h ('input', dict ({'id': ref + 'second', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': grdt.second}), ''), h ('input', dict ({'id': ref + 'timezone', 'class': 'input', 'oninput': (function __lambda__ (event) {
		return actions ['change_grdt_timezone'] (event);
	}), 'style': dict ({'width': '6em'}), 'type': 'text', 'value': grdt.timezone}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
		return actions ['sync_by_grdt'] (event);
	})}), 'Sync')]);
};
export var view_juld = function (state, actions) {
	var juld = state ['juld'];
	var ref = state ['juld_ref'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('label', dict ({'class': 'label', 'for': ref}), 'Julian Day'), h ('input', dict ({'id': ref, 'class': 'input', 'step': 1e-05, 'type': 'number', 'value': juld.julian_day}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
		return actions ['sync_by_juld'] (event);
	})}), 'Sync')]);
};
export var view_delta_t = function (state, actions) {
	var delta_t = state ['delta_t'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('div', dict ({'class': 'label'}), '⊿t'), str (delta_t)]);
};
export var view_tert = function (state, actions) {
	var tert = state ['tert'];
	var ref = state ['tert_ref'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('label', dict ({'class': 'label', 'for': ref}), 'Terrestrual Time'), h ('input', dict ({'id': ref, 'class': 'input', 'step': 1e-05, 'type': 'number', 'value': tert.terrestrial_time}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
		return actions ['sync_by_tert'] (event);
	})}), 'Sync')]);
};
export var view_mrls = function (state, actions) {
	var mrls = state ['mrls'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('label', dict ({'class': 'label'}), 'Areocentric Solar Longitude (Mars Ls)'), str (mrls)]);
};
export var view_mrsd = function (state, actions) {
	var mrsd = state ['mrsd'];
	var ref = state ['mrsd_ref'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('label', dict ({'class': 'label', 'for': ref}), 'Mars Sol Date'), h ('input', dict ({'id': ref, 'class': 'input', 'step': 1e-05, 'type': 'number', 'value': mrsd.mars_sol_date}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
		return actions ['sync_by_mrsd'] (event);
	})}), 'Sync')]);
};
export var view_imsn = function (state, actions) {
	var imsn = state ['imsn'];
	var ref = state ['imsn_ref'];
	return h ('div', dict ({'class': 'field is-grouped'}), [h ('label', dict ({'class': 'label', 'for': ref}), 'Imperial Sol Number'), h ('input', dict ({'id': ref, 'class': 'input', 'step': 1e-05, 'type': 'number', 'value': imsn.imperial_sol_number}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
		return actions ['sync_by_imsn'] (event);
	})}), 'Sync')]);
};
export var view_imdt = function (state, actions) {
	var imdt = state ['imdt'];
	var ref = state ['imdt_ref'];
	return h ('div', dict ({'class': 'field is-grouped is-grouped-multiline'}), [h ('label', dict ({'class': 'label', 'for': ref + 'year'}), 'Imperial Date Time'), h ('input', dict ({'id': ref + 'year', 'class': 'input', 'style': dict ({'width': '6em'}), 'type': 'number', 'value': imdt.year}), ''), '-', h ('input', dict ({'id': ref + 'month', 'class': 'input', 'max': 24, 'min': 1, 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': imdt.month}), ''), '-', h ('input', dict ({'id': ref + 'day', 'class': 'input', 'max': 28, 'min': 1, 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': imdt.day}), ''), 'T', h ('input', dict ({'id': ref + 'hour', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': imdt.hour}), ''), ':', h ('input', dict ({'id': ref + 'minute', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': imdt.minute}), ''), ':', h ('input', dict ({'id': ref + 'second', 'class': 'input', 'style': dict ({'width': '3.5em'}), 'type': 'number', 'value': imdt.second}), ''), h ('input', dict ({'id': ref + 'timezone', 'class': 'input', 'oninput': (function __lambda__ (event) {
		return actions ['change_imdt_timezone'] (event);
	}), 'style': dict ({'width': '6em'}), 'type': 'text', 'value': imdt.timezone}), ''), h ('button', dict ({'class': 'button is-dark', 'onclick': (function __lambda__ (event) {
		return actions ['sync_by_imdt'] (event);
	})}), 'Sync')]);
};
export var view = function (state, actions) {
	return h ('div', dict ({}), [view_grdt, view_juld, view_delta_t, view_tert, view_mrls, view_mrsd, view_imsn, view_imdt]);
};
export var __all__ = ['view'];

//# sourceMappingURL=ui.view.map