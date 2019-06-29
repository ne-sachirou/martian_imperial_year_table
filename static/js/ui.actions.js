// Transcrypt'ed from Python, 2019-06-29 15:02:04
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as t from './typing.js';
import {TerrestrialTime} from './imperial_calendar.TerrestrialTime.js';
import {MarsSolDate} from './imperial_calendar.MarsSolDate.js';
import {JulianDay} from './imperial_calendar.JulianDay.js';
import {ImperialSolNumber} from './imperial_calendar.ImperialSolNumber.js';
import {ImperialDateTime} from './imperial_calendar.ImperialDateTime.js';
import {GregorianDateTime} from './imperial_calendar.GregorianDateTime.js';
var __name__ = 'ui.actions';
export var Api =  __class__ ('Api', [object], {
	__module__: __name__,
	get get_datetimes () {return __get__ (this, async function (self, params) {
		var response = await fetch ('/api/datetimes?params={}'.format (encodeURIComponent (params)), dict ({'method': 'GET'}));
		if (!(response.ok)) {
			var __except0__ = Exception ('{}: {}'.format (response.status, response.text ()));
			__except0__.__cause__ = null;
			throw __except0__;
		}
		return await response.json ();
	});}
});
export var change_grdt_timezone = function (state, event) {
	var ref = state ['grdt_ref'];
	var grdt_timezone = document.getElementById (ref + 'timezone').value;
	var grdt = state ['grdt'].copy ();
	grdt.timezone = grdt_timezone;
	return dict ({'grdt_timezone': grdt_timezone, 'grdt': grdt});
};
export var change_imdt_timezone = function (state, event) {
	var ref = state ['imdt_ref'];
	var imdt_timezone = document.getElementById (ref + 'timezone').value;
	var imdt = state ['imdt'].copy ();
	imdt.timezone = imdt_timezone;
	return dict ({'imdt_timezone': imdt_timezone, 'imdt': imdt});
};
export var draw_datetimes = function (state, datetimes) {
	var grdt = datetimes ['grdt'];
	var grdt = GregorianDateTime (grdt ['year'], grdt ['month'], grdt ['day'], grdt ['hour'], grdt ['minute'], grdt ['second'], state ['grdt_timezone']);
	var juld = JulianDay (datetimes ['juld'] ['julian_day']);
	var tert = TerrestrialTime (datetimes ['tert'] ['terrestrial_time']);
	var mrsd = MarsSolDate (datetimes ['mrsd'] ['mars_sol_date']);
	var imsn = ImperialSolNumber (datetimes ['imsn'] ['imperial_sol_number']);
	var imdt = datetimes ['imdt'];
	var imdt = ImperialDateTime (imdt ['year'], imdt ['month'], imdt ['day'], imdt ['hour'], imdt ['minute'], imdt ['second'], state ['imdt_timezone']);
	return dict ({'grdt': grdt, 'juld': juld, 'delta_t': datetimes ['delta_t'], 'tert': tert, 'mrls': datetimes ['mrls'], 'mrsd': mrsd, 'imsn': imsn, 'imdt': imdt});
};
export var sync_by_grdt = async function (state, actions, event) {
	if (event) {
		event.stopPropagation ();
		event.preventDefault ();
	}
	var ref = state ['grdt_ref'];
	var params = JSON.stringify (dict ({'grdt_timezone': state ['grdt_timezone'], 'imdt_timezone': state ['imdt_timezone'], 'grdt': dict ({'year': int (document.getElementById (ref + 'year').value), 'month': int (document.getElementById (ref + 'month').value), 'day': int (document.getElementById (ref + 'day').value), 'hour': int (document.getElementById (ref + 'hour').value), 'minute': int (document.getElementById (ref + 'minute').value), 'second': int (document.getElementById (ref + 'second').value)})}));
	var datetimes = await Api ().get_datetimes (params);
	actions ['draw_datetimes'] (datetimes);
};
export var sync_by_juld = async function (state, event) {
	event.stopPropagation ();
	event.preventDefault ();
	var ref = state ['juld_ref'];
	var params = JSON.stringify (dict ({'grdt_timezone': state ['grdt_timezone'], 'imdt_timezone': state ['imdt_timezone'], 'juld': dict ({'julian_day': float (document.getElementById (ref).value)})}));
	var datetimes = await Api ().get_datetimes (params);
	actions ['draw_datetimes'] (datetimes);
};
export var sync_by_tert = async function (state, event) {
	event.stopPropagation ();
	event.preventDefault ();
	var ref = state ['tert_ref'];
	var params = JSON.stringify (dict ({'grdt_timezone': state ['grdt_timezone'], 'imdt_timezone': state ['imdt_timezone'], 'tert': dict ({'terrestrial_time': float (document.getElementById (ref).value)})}));
	var datetimes = await Api ().get_datetimes (params);
	actions ['draw_datetimes'] (datetimes);
};
export var sync_by_mrsd = async function (state, event) {
	event.stopPropagation ();
	event.preventDefault ();
	var ref = state ['mrsd_ref'];
	var params = JSON.stringify (dict ({'grdt_timezone': state ['grdt_timezone'], 'imdt_timezone': state ['imdt_timezone'], 'mrsd': dict ({'mars_sol_date': float (document.getElementById (ref).value)})}));
	var datetimes = await Api ().get_datetimes (params);
	actions ['draw_datetimes'] (datetimes);
};
export var sync_by_imsn = async function (state, event) {
	event.stopPropagation ();
	event.preventDefault ();
	var ref = state ['imsn_ref'];
	var params = JSON.stringify (dict ({'grdt_timezone': state ['grdt_timezone'], 'imdt_timezone': state ['imdt_timezone'], 'imsn': dict ({'imperial_sol_number': float (document.getElementById (ref).value)})}));
	var datetimes = await Api ().get_datetimes (params);
	actions ['draw_datetimes'] (datetimes);
};
export var sync_by_imdt = async function (state, event) {
	event.stopPropagation ();
	event.preventDefault ();
	var ref = state ['imdt_ref'];
	var params = JSON.stringify (dict ({'grdt_timezone': state ['grdt_timezone'], 'imdt_timezone': state ['imdt_timezone'], 'imdt': dict ({'year': int (document.getElementById (ref + 'year').value), 'month': int (document.getElementById (ref + 'month').value), 'day': int (document.getElementById (ref + 'day').value), 'hour': int (document.getElementById (ref + 'hour').value), 'minute': int (document.getElementById (ref + 'minute').value), 'second': int (document.getElementById (ref + 'second').value)})}));
	var datetimes = await Api ().get_datetimes (params);
	actions ['draw_datetimes'] (datetimes);
};
export var actions = function () {
	return dict ({'change_grdt_timezone': (function __lambda__ (event) {
		return (function __lambda__ (state) {
			return change_grdt_timezone (state, event);
		});
	}), 'change_imdt_timezone': (function __lambda__ (event) {
		return (function __lambda__ (state) {
			return change_imdt_timezone (state, event);
		});
	}), 'draw_datetimes': (function __lambda__ (datetimes) {
		return (function __lambda__ (state) {
			return draw_datetimes (state, datetimes);
		});
	}), 'sync_by_grdt': (function __lambda__ (event) {
		return (function __lambda__ (state, actions) {
			return sync_by_grdt (state, actions, event);
		});
	}), 'sync_by_juld': (function __lambda__ (event) {
		return (function __lambda__ (state) {
			return sync_by_juld (state, event);
		});
	}), 'sync_by_tert': (function __lambda__ (event) {
		return (function __lambda__ (state) {
			return sync_by_tert (state, event);
		});
	}), 'sync_by_mrsd': (function __lambda__ (event) {
		return (function __lambda__ (state) {
			return sync_by_mrsd (state, event);
		});
	}), 'sync_by_imsn': (function __lambda__ (event) {
		return (function __lambda__ (state) {
			return sync_by_imsn (state, event);
		});
	}), 'sync_by_imdt': (function __lambda__ (event) {
		return (function __lambda__ (state) {
			return sync_by_imdt (state, event);
		});
	})});
};

//# sourceMappingURL=ui.actions.map