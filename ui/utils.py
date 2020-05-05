from imperial_calendar.GregorianDateTime import GregorianDateTime

Date: t.Any = 0  # __:skip


def current_grdt() -> GregorianDateTime:
    now = __new__(Date)  # noqa
    offset = now.getTimezoneOffset()
    if offset <= 0:
        sign = "+"
    else:
        sign = "-"
    grdt_timezone = "{0}{1}:{2}".format(
        sign,
        "0{}".format(abs(offset) // 60).substr(-2),
        "0{}".format(abs(offset) % 60).substr(-2),
    )
    return GregorianDateTime(
        now.getFullYear(),
        now.getMonth() + 1,
        now.getDate(),
        now.getHours(),
        now.getMinutes(),
        now.getSeconds(),
        grdt_timezone,
    )
