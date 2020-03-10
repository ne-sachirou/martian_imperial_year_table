"""App."""
from datetime import timedelta
from flasgger import swag_from, Swagger
from flask import Flask, jsonify, request
from flask import render_template
from imperial_calendar import (
    GregorianDateTime,
    ImperialDateTime,
    ImperialSolNumber,
    JulianDay,
    MarsSolDate,
    TerrestrialTime,
)
from imperial_calendar.transform import (
    grdt_to_juld,
    imdt_to_imsn,
    imsn_to_imdt,
    imsn_to_mrsd,
    juld_to_grdt,
    juld_to_tert,
    mrsd_to_imsn,
    mrsd_to_tert,
    tert_to_juld,
    tert_to_mrls,
    tert_to_mrsd,
)
import json
import markdown
import typing as t


class Config(object):
    """Common config."""

    pass


class DevelopmentConfig(Config):
    """Development config."""

    SEND_FILE_MAX_AGE_DEFAULT = 0


class ProductionConfig(Config):
    """Production config."""

    SEND_FILE_MAX_AGE_DEFAULT = timedelta(minutes=5)


class TestingConfig(Config):
    """Testing config."""

    SEND_FILE_MAX_AGE_DEFAULT = 0
    TESTING = True


app = Flask(__name__)
if app.env == "development":
    app.config.from_object(DevelopmentConfig)
elif app.env == "production":
    app.config.from_object(ProductionConfig)
elif app.env == "testing":
    app.config.from_object(TestingConfig)
else:
    raise Exception(f"Unknown FLASK_ENV: {app.env}")
Swagger(app)


@app.route("/ops/heartbeat")
def heartbeat() -> str:
    """Komachi heartbeat."""
    return "heartbeat:ok"


@app.route("/")
def index() -> str:
    """Index."""
    return render_template("index.html")


@app.route("/description")
def description() -> str:
    """Describe Martian Imperial Calendar."""
    with open("templates/description.md") as f:
        return markdown.markdown(f.read(), extensions=[], output_format="html5")


@app.route("/api/datetimes", methods=["GET"])
@swag_from("web.yml", validation=False)
def datetimes() -> str:
    """Get datetimes."""
    params = json.loads(t.cast(str, request.args.get("params")))
    if "grdt" in params:
        grdt = params["grdt"]
        grdt = GregorianDateTime(
            grdt["year"],
            grdt["month"],
            grdt["day"],
            grdt["hour"],
            grdt["minute"],
            grdt["second"],
            params["grdt_timezone"],
        )
        juld = grdt_to_juld(grdt.to_utc_naive())
        tert = juld_to_tert(juld)
        mrsd = tert_to_mrsd(tert)
        imsn = mrsd_to_imsn(mrsd)
        imdt = ImperialDateTime.from_standard_naive(
            imsn_to_imdt(imsn), params["imdt_timezone"]
        )
    elif "juld" in params:
        juld = params["juld"]
        juld = JulianDay(juld["day"], juld["second"])
        grdt = GregorianDateTime.from_utc_naive(
            juld_to_grdt(juld), params["grdt_timezone"]
        )
        tert = juld_to_tert(juld)
        mrsd = tert_to_mrsd(tert)
        imsn = mrsd_to_imsn(mrsd)
        imdt = ImperialDateTime.from_standard_naive(
            imsn_to_imdt(imsn), params["imdt_timezone"]
        )
    elif "tert" in params:
        tert = TerrestrialTime(params["tert"]["terrestrial_time"])
        juld = tert_to_juld(tert)
        grdt = GregorianDateTime.from_utc_naive(
            juld_to_grdt(juld), params["grdt_timezone"]
        )
        mrsd = tert_to_mrsd(tert)
        imsn = mrsd_to_imsn(mrsd)
        imdt = ImperialDateTime.from_standard_naive(
            imsn_to_imdt(imsn), params["imdt_timezone"]
        )
    elif "mrsd" in params:
        mrsd = MarsSolDate(params["mrsd"]["mars_sol_date"])
        tert = mrsd_to_tert(mrsd)
        juld = tert_to_juld(tert)
        grdt = GregorianDateTime.from_utc_naive(
            juld_to_grdt(juld), params["grdt_timezone"]
        )
        imsn = mrsd_to_imsn(mrsd)
        imdt = ImperialDateTime.from_standard_naive(
            imsn_to_imdt(imsn), params["imdt_timezone"]
        )
    elif "imsn" in params:
        imsn = params["imsn"]
        imsn = ImperialSolNumber(imsn["day"], imsn["second"])
        mrsd = imsn_to_mrsd(imsn)
        tert = mrsd_to_tert(mrsd)
        juld = tert_to_juld(tert)
        grdt = GregorianDateTime.from_utc_naive(
            juld_to_grdt(juld), params["grdt_timezone"]
        )
        imdt = ImperialDateTime.from_standard_naive(
            imsn_to_imdt(imsn), params["imdt_timezone"]
        )
    elif "imdt" in params:
        imdt = params["imdt"]
        imdt = ImperialDateTime(
            imdt["year"],
            imdt["month"],
            imdt["day"],
            imdt["hour"],
            imdt["minute"],
            imdt["second"],
            params["imdt_timezone"],
        )
        imsn = imdt_to_imsn(imdt.to_standard_naive())
        mrsd = imsn_to_mrsd(imsn)
        tert = mrsd_to_tert(mrsd)
        juld = tert_to_juld(tert)
        grdt = GregorianDateTime.from_utc_naive(
            juld_to_grdt(juld), params["grdt_timezone"]
        )
    else:
        raise Exception(f"Unknown pattern of params: {params}")
    return jsonify(
        {
            "grdt": grdt.__dict__,
            "juld": juld.__dict__,
            "delta_t": juld.delta_t,
            "tert": tert.__dict__,
            "mrls": tert_to_mrls(tert),
            "mrsd": mrsd.__dict__,
            "imsn": imsn.__dict__,
            "imdt": imdt.__dict__,
        }
    )
