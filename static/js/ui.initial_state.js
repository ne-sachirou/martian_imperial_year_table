// Transcrypt'ed from Python, 2019-06-29 15:02:04
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {TerrestrialTime} from './imperial_calendar.TerrestrialTime.js';
import {MarsSolDate} from './imperial_calendar.MarsSolDate.js';
import {JulianDay} from './imperial_calendar.JulianDay.js';
import {ImperialSolNumber} from './imperial_calendar.ImperialSolNumber.js';
import {ImperialDateTime} from './imperial_calendar.ImperialDateTime.js';
import {GregorianDateTime} from './imperial_calendar.GregorianDateTime.js';
var __name__ = 'ui.initial_state';
export var new_ref = function (prefix) {
	var ref = '{}.{}{}'.format (prefix, Date.now ().toString (36), Math.random ().toString (36).substr (1));
	return ref;
};
export var initial_state = function () {
	var grdt_timezone = '+00:00';
	var grdt = GregorianDateTime (1970, 1, 1, 0, 0, 0, grdt_timezone);
	var grdt_ref = new_ref ('grdt');
	var juld = JulianDay (0.0);
	var juld_ref = new_ref ('juld');
	var tert = TerrestrialTime (0.0);
	var tert_ref = new_ref ('tert');
	var mrsd = MarsSolDate (0.0);
	var mrsd_ref = new_ref ('mrsd');
	var imsn = ImperialSolNumber (0.0);
	var imsn_ref = new_ref ('imsn');
	var imdt_timezone = '+00:00';
	var imdt = ImperialDateTime (0, 0, 0, 0, 0, 0, imdt_timezone);
	var imdt_ref = new_ref ('imdt');
	return dict ({'grdt': grdt, 'grdt_ref': grdt_ref, 'grdt_timezone': grdt_timezone, 'juld': juld, 'juld_ref': juld_ref, 'delta_t': 0.0, 'tert': tert, 'tert_ref': tert_ref, 'mrls': 0.0, 'mrsd': mrsd, 'mrsd_ref': mrsd_ref, 'imsn': imsn, 'imsn_ref': imsn_ref, 'imdt': imdt, 'imdt_ref': imdt_ref, 'imdt_timezone': imdt_timezone});
};

//# sourceMappingURL=ui.initial_state.map