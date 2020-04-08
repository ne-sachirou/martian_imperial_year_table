"""Client of Web API."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.JulianDay import JulianDay
from imperial_calendar.MarsSolDate import MarsSolDate
from imperial_calendar.TerrestrialTime import TerrestrialTime
import typing as t

JSON: t.Any = 0  # __:skip
encodeURIComponent: t.Any = 0  # __:skip
fetch: t.Any = 0  # __:skip


class Api(object):
    """Client of Web API."""

    async def get_datetimes(self, params: dict) -> dict:
        """Get datetimes."""
        response = await fetch(
            "/api/datetimes?params={}".format(
                encodeURIComponent(JSON.stringify(params))
            )
        )
        if not response.ok:
            raise Exception(f"{response.status}: {response.text()}")
        json = await response.json()
        grdt = GregorianDateTime(
            json["grdt"]["year"],
            json["grdt"]["month"],
            json["grdt"]["day"],
            json["grdt"]["hour"],
            json["grdt"]["minute"],
            json["grdt"]["second"],
            params["grdt_timezone"],
        )
        juld = JulianDay(json["juld"]["day"], json["juld"]["second"])
        tert = TerrestrialTime(json["tert"]["terrestrial_time"])
        mrsd = MarsSolDate(json["mrsd"]["mars_sol_date"])
        imsn = ImperialSolNumber(json["imsn"]["day"], json["imsn"]["second"])
        imdt = ImperialDateTime(
            json["imdt"]["year"],
            json["imdt"]["month"],
            json["imdt"]["day"],
            json["imdt"]["hour"],
            json["imdt"]["minute"],
            json["imdt"]["second"],
            params["imdt_timezone"],
        )
        return {
            "grdt": grdt,
            "juld": juld,
            "delta_t": json["delta_t"],
            "tert": tert,
            "mrls": json["mrls"],
            "mrsd": mrsd,
            "imsn": imsn,
            "imdt": imdt,
        }

    async def get_description(self) -> dict:
        """Get description."""
        response = await fetch("/api/description")
        if not response.ok:
            raise Exception(f"{response.status}: {response.text()}")
        return await response.json()
