"""Draw a imdt calendar image."""
from contextlib import contextmanager
from functools import partial
from imperial_calendar import GregorianDateTime, ImperialDateTime
from imperial_calendar.internal.ImperialMonth import ImperialMonth
from imperial_calendar.internal.ImperialYear import ImperialYear
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
    tert_to_mrsd,
)
import typing as t
import xml.etree.ElementTree as ET


def days_of_month(imdt: ImperialDateTime) -> int:
    """Get days of the imdt month."""
    days = ImperialMonth(imdt.month).days()
    if imdt.month == 24 and ImperialYear(imdt.year).is_leap_year():
        days += 1
    return days


def next_grdt_day_of(grdt: GregorianDateTime) -> GregorianDateTime:
    """Create a new grdt on the next day."""
    grdt = grdt.copy()
    days: int = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][grdt.month - 1]
    # NOTE: Don't consider about Julian Calendar, before Gregorian Calendar begins.
    if grdt.month == 2 and (
        grdt.year % 4 == 0 and (grdt.year % 100 != 0 or grdt.year % 400 == 0)
    ):
        days = 29
    if grdt.day == days:
        if grdt.month == 12:
            grdt.year += 1  # NOTE: Don't consider about B.C. 1, A.D. 1.
            grdt.month = 1
        else:
            grdt.month += 1
        grdt.day = 1
    else:
        grdt.day += 1
    return grdt


def grdt_to_imdt(
    grdt: GregorianDateTime, imdt_timezone: t.Optional[str]
) -> ImperialDateTime:
    """Transform grdt to imdt."""
    imdt_timezone = imdt_timezone or "+00:00"
    juld = grdt_to_juld(grdt.to_utc_naive())
    tert = juld_to_tert(juld)
    mrsd = tert_to_mrsd(tert)
    imsn = mrsd_to_imsn(mrsd)
    return ImperialDateTime.from_standard_naive(imsn_to_imdt(imsn), imdt_timezone)


def imdt_to_grdt(imdt: ImperialDateTime, grdt_timezone: str) -> GregorianDateTime:
    """Transform imdt to grdt."""
    imsn = imdt_to_imsn(imdt.to_standard_naive())
    mrsd = imsn_to_mrsd(imsn)
    tert = mrsd_to_tert(mrsd)
    juld = tert_to_juld(tert)
    return GregorianDateTime.from_utc_naive(juld_to_grdt(juld), grdt_timezone)


@contextmanager
def e(
    tag: str, attrib: t.Dict[str, str] = {}, text: str = "", parent: ET.Element = None
) -> t.Generator[t.Callable[[str, t.Dict[str, str], str], t.Any], None, t.Any]:
    """Create a XML element and pass a new context for sub elements."""
    if parent is not None:
        element = ET.SubElement(parent, tag, attrib)
    else:
        element = ET.Element(tag, attrib)
    if text != "":
        element.text = text
    yield partial(e, parent=element)


def text_y(y: t.Union[float, str], font_size: t.Union[float, str]) -> float:
    """
    Caliculate the y value of the SVG text element.

    y: mm
    font_size: pt
    """
    return float(y) + float(font_size) * 0.353


class CalendarImage(object):
    """Draw a imdt calendar image."""

    BLACK: str = "#3b3b3b"
    BLUE: str = "#40a1cc"
    FONT_FAMILY_BOLD: str = """"筑紫B丸ゴシック ボールド", "UD デジタル 教科書体 NK-B", sans-serif"""
    FONT_FAMILY_REGULAR: str = """"筑紫B丸ゴシック ボールド", "UD デジタル 教科書体 NK-R", sans-serif"""
    FONT_SIZE_ANNOTATION: float = 8.0
    FONT_SIZE_BOLD_LARGE: float = 32.0
    FONT_SIZE_LARGE: float = 20.0
    FONT_SIZE_SMALL: float = 10.0
    GRAY_BLUE: str = "#a5c7d6"
    GRAY_RED: str = "#ffb7a1"
    GRAY: str = "#999999"
    grdt_timezone: str
    HEIGHT_DAYS_GAP: float = 4.5
    HEIGHT_GRDT_BELT: float = 5.5
    HEIGHT_TOP_SPACE: float = 15.0
    imdt: ImperialDateTime
    RED: str = "#e07553"
    SIZE_DAY_SQUARE: float = 22.5
    STROKE_WIDTH_BOLD: str = "0.4mm"
    STROKE_WIDTH_THIN: str = "0.15mm"
    WHITE: str = "white"
    WIDTH_LEFT_SPACE: float = 45.0

    def __init__(self, imdt: ImperialDateTime, grdt_timezone: str):
        """Init."""
        self.grdt_timezone = grdt_timezone
        self.imdt = imdt.copy()
        self.imdt.day = 1
        self.imdt.hour = 0
        self.imdt.minute = 0
        self.imdt.second = 0

    def draw_as_svg(self) -> str:
        """Draw a imdt calendar image as SVG string."""
        svg = ET.Element(
            "svg",
            {
                "height": "148mm",
                "style": f"""
                background-color: {CalendarImage.WHITE};
                """,
                "width": "210mm",
                "xmlns": "http://www.w3.org/2000/svg",
            },
        )
        with e("title", {}, f"帝國火星曆{self.imdt.year}年{self.imdt.month}月", parent=svg):
            pass
        with e(
            "g",
            {
                "style": f"""
                font-family: {CalendarImage.FONT_FAMILY_REGULAR};
                """
            },
            parent=svg,
        ) as _e:
            self.__draw_title(_e)
            self.__draw_joubi(_e)
            self.__draw_static_frame(_e)
            self.__draw_imdt_days(_e)
            self.__draw_imdt_syukuzitu(_e)
            self.__draw_grdt_days(_e)
        return ET.tostring(svg).decode("utf-8")

    def __draw_grdt_day(self, _e, grdt: GregorianDateTime) -> None:
        imdt = grdt_to_imdt(grdt, self.imdt.timezone)
        line_x = (
            (((imdt.hour * 60) + imdt.minute) * 60 + imdt.second)
            / (24 * 60 * 60)
            * CalendarImage.SIZE_DAY_SQUARE
        )
        if imdt.month == self.imdt.month:
            x1 = (
                CalendarImage.WIDTH_LEFT_SPACE
                + line_x
                + CalendarImage.SIZE_DAY_SQUARE * ((imdt.day - 1) % 7)
            )
            x2 = (
                CalendarImage.WIDTH_LEFT_SPACE
                + line_x
                + CalendarImage.SIZE_DAY_SQUARE * ((imdt.day - 1) % 7)
            )
            y1 = (
                CalendarImage.HEIGHT_TOP_SPACE
                + CalendarImage.SIZE_DAY_SQUARE
                + (
                    CalendarImage.HEIGHT_GRDT_BELT
                    + CalendarImage.HEIGHT_DAYS_GAP
                    + CalendarImage.SIZE_DAY_SQUARE
                )
                * ((imdt.day - 1) // 7)
            )
            y2 = (
                CalendarImage.HEIGHT_TOP_SPACE
                + CalendarImage.SIZE_DAY_SQUARE
                + CalendarImage.HEIGHT_GRDT_BELT
                + (
                    CalendarImage.HEIGHT_GRDT_BELT
                    + CalendarImage.HEIGHT_DAYS_GAP
                    + CalendarImage.SIZE_DAY_SQUARE
                )
                * ((imdt.day - 1) // 7)
            )
            with _e(
                "line",
                {
                    "stroke": CalendarImage.BLACK,
                    "stroke-width": CalendarImage.STROKE_WIDTH_THIN,
                    "x1": f"{x1}mm",
                    "x2": f"{x2}mm",
                    "y1": f"{y1}mm",
                    "y2": f"{y2}mm",
                },
            ):
                pass
        next_grdt_day = next_grdt_day_of(grdt)
        next_grdt_day_imdt = grdt_to_imdt(next_grdt_day, self.imdt.timezone)
        next_line_x = (
            (
                ((next_grdt_day_imdt.hour * 60) + next_grdt_day_imdt.minute) * 60
                + next_grdt_day_imdt.second
            )
            / (24 * 60 * 60)
            * CalendarImage.SIZE_DAY_SQUARE
        )
        is_drawable_on_beginning_of_month = (
            next_line_x
            > 0.353 * CalendarImage.FONT_SIZE_SMALL * (len("10/10") * 0.6) + 1.5
        )
        if grdt.is_holiday or grdt.weekday == 7:
            color = CalendarImage.GRAY_RED
        elif grdt.weekday == 6:
            color = CalendarImage.GRAY_BLUE
        else:
            color = CalendarImage.GRAY
        if imdt.month == self.imdt.month:
            text = (
                f"{grdt.month}/{grdt.day}"
                if grdt.day == 1
                or (imdt.day == 1 and not is_drawable_on_beginning_of_month)
                else str(grdt.day)
            )
            is_drawable_on_weekend = (
                CalendarImage.SIZE_DAY_SQUARE - line_x
            ) > 0.353 * CalendarImage.FONT_SIZE_SMALL * (len(text) * 0.6) + 1.5
            if imdt.day == days_of_month(self.imdt) and not is_drawable_on_weekend:
                pass
            elif imdt.day % 7 == 0 and not is_drawable_on_weekend:
                self.__draw_text(
                    _e,
                    {
                        "fill": color,
                        "font-size": CalendarImage.FONT_SIZE_SMALL,
                        "x": f"{CalendarImage.WIDTH_LEFT_SPACE + 1}mm",
                        "y": CalendarImage.HEIGHT_TOP_SPACE
                        + CalendarImage.SIZE_DAY_SQUARE
                        + 0.5
                        + (
                            CalendarImage.HEIGHT_GRDT_BELT
                            + CalendarImage.HEIGHT_DAYS_GAP
                            + CalendarImage.SIZE_DAY_SQUARE
                        )
                        * (imdt.day // 7),
                    },
                    text,
                )
            else:
                x = (
                    CalendarImage.WIDTH_LEFT_SPACE
                    + line_x
                    + 1
                    + CalendarImage.SIZE_DAY_SQUARE * ((imdt.day - 1) % 7)
                )
                self.__draw_text(
                    _e,
                    {
                        "fill": color,
                        "font-size": CalendarImage.FONT_SIZE_SMALL,
                        "x": f"{x}mm",
                        "y": CalendarImage.HEIGHT_TOP_SPACE
                        + CalendarImage.SIZE_DAY_SQUARE
                        + 0.5
                        + (
                            CalendarImage.HEIGHT_GRDT_BELT
                            + CalendarImage.HEIGHT_DAYS_GAP
                            + CalendarImage.SIZE_DAY_SQUARE
                        )
                        * ((imdt.day - 1) // 7),
                    },
                    text,
                )
        else:
            if is_drawable_on_beginning_of_month:
                self.__draw_text(
                    _e,
                    {
                        "fill": color,
                        "font-size": CalendarImage.FONT_SIZE_SMALL,
                        "x": f"{CalendarImage.WIDTH_LEFT_SPACE + 1}mm",
                        "y": CalendarImage.HEIGHT_TOP_SPACE
                        + CalendarImage.SIZE_DAY_SQUARE
                        + 0.5,
                    },
                    f"{grdt.month}/{grdt.day}",
                )

    def __draw_grdt_days(self, _e) -> None:
        drawing_grdt_day = imdt_to_grdt(self.imdt, self.grdt_timezone)
        drawing_grdt_day.hour = 0
        drawing_grdt_day.minute = 0
        drawing_grdt_day.second = 0
        while (
            grdt_to_imdt(drawing_grdt_day, self.imdt.timezone)
            < self.__next_imdt_month()
        ):
            self.__draw_grdt_day(_e, drawing_grdt_day)
            drawing_grdt_day = next_grdt_day_of(drawing_grdt_day)

    def __draw_imdt_days(self, _e) -> None:
        for day in range(1, days_of_month(self.imdt) + 1):
            if day % 7 == 0:
                color = CalendarImage.BLUE
            elif day % 7 == 1:
                color = CalendarImage.RED
            else:
                color = CalendarImage.BLACK
            self.__draw_text(
                _e,
                {
                    "fill": color,
                    "font-size": CalendarImage.FONT_SIZE_SMALL,
                    "x": f"{CalendarImage.WIDTH_LEFT_SPACE + 1 + CalendarImage.SIZE_DAY_SQUARE * ((day - 1) % 7)}mm",
                    "y": CalendarImage.HEIGHT_TOP_SPACE
                    + 1
                    + (
                        CalendarImage.SIZE_DAY_SQUARE
                        + CalendarImage.HEIGHT_GRDT_BELT
                        + CalendarImage.HEIGHT_DAYS_GAP
                    )
                    * ((day - 1) // 7),
                },
                str(day),
            )

    def __draw_imdt_syukuzitu(self, _e) -> None:
        pass

    def __draw_joubi(self, _e) -> None:
        for i, (joubi, color) in enumerate(
            [
                ("日", CalendarImage.RED),
                ("月", CalendarImage.BLACK),
                ("火", CalendarImage.BLACK),
                ("水", CalendarImage.BLACK),
                ("木", CalendarImage.BLACK),
                ("金", CalendarImage.BLACK),
                ("土", CalendarImage.BLUE),
            ]
        ):
            x = (
                CalendarImage.WIDTH_LEFT_SPACE
                + (CalendarImage.SIZE_DAY_SQUARE / 2)
                - 2.0
                + CalendarImage.SIZE_DAY_SQUARE * i
            )
            self.__draw_text(
                _e,
                {
                    "fill": color,
                    "font-size": CalendarImage.FONT_SIZE_SMALL,
                    "x": f"{x}mm",
                    "y": CalendarImage.HEIGHT_TOP_SPACE - 5,
                },
                joubi,
            )

    def __draw_static_frame(self, _e) -> None:
        days = days_of_month(self.imdt)
        for i in range(4):
            days_of_week = 6 if i == 3 and days == 27 else 7
            y = (
                CalendarImage.HEIGHT_TOP_SPACE
                + (
                    CalendarImage.SIZE_DAY_SQUARE
                    + CalendarImage.HEIGHT_GRDT_BELT
                    + CalendarImage.HEIGHT_DAYS_GAP
                )
                * i
            )
            with _e(
                "rect",
                {
                    "fill": CalendarImage.WHITE,
                    "height": f"{CalendarImage.SIZE_DAY_SQUARE + CalendarImage.HEIGHT_GRDT_BELT}mm",
                    "stroke-width": CalendarImage.STROKE_WIDTH_BOLD,
                    "stroke": CalendarImage.BLACK,
                    "width": f"{CalendarImage.SIZE_DAY_SQUARE * days_of_week}mm",
                    "x": f"{CalendarImage.WIDTH_LEFT_SPACE}mm",
                    "y": f"{y}mm",
                },
            ):
                pass
            y1 = (
                CalendarImage.HEIGHT_TOP_SPACE
                + CalendarImage.SIZE_DAY_SQUARE
                + (
                    CalendarImage.SIZE_DAY_SQUARE
                    + CalendarImage.HEIGHT_GRDT_BELT
                    + CalendarImage.HEIGHT_DAYS_GAP
                )
                * i
            )
            y2 = (
                CalendarImage.HEIGHT_TOP_SPACE
                + CalendarImage.SIZE_DAY_SQUARE
                + (
                    CalendarImage.SIZE_DAY_SQUARE
                    + CalendarImage.HEIGHT_GRDT_BELT
                    + CalendarImage.HEIGHT_DAYS_GAP
                )
                * i
            )
            with _e(
                "line",
                {
                    "stroke-width": CalendarImage.STROKE_WIDTH_THIN,
                    "stroke": CalendarImage.BLACK,
                    "x1": f"{CalendarImage.WIDTH_LEFT_SPACE}mm",
                    "x2": f"{CalendarImage.WIDTH_LEFT_SPACE + CalendarImage.SIZE_DAY_SQUARE * days_of_week}mm",
                    "y1": f"{y1}mm",
                    "y2": f"{y2}mm",
                },
            ):
                pass
            for j in range(days_of_week):
                y1 = (
                    CalendarImage.HEIGHT_TOP_SPACE
                    + (
                        CalendarImage.SIZE_DAY_SQUARE
                        + CalendarImage.HEIGHT_GRDT_BELT
                        + CalendarImage.HEIGHT_DAYS_GAP
                    )
                    * i
                )
                y2 = (
                    CalendarImage.HEIGHT_TOP_SPACE
                    + CalendarImage.SIZE_DAY_SQUARE
                    + (
                        CalendarImage.SIZE_DAY_SQUARE
                        + CalendarImage.HEIGHT_GRDT_BELT
                        + CalendarImage.HEIGHT_DAYS_GAP
                    )
                    * i
                )
                with _e(
                    "line",
                    {
                        "stroke-width": CalendarImage.STROKE_WIDTH_BOLD,
                        "stroke": CalendarImage.BLACK,
                        "x1": f"{CalendarImage.WIDTH_LEFT_SPACE + CalendarImage.SIZE_DAY_SQUARE * (j + 1)}mm",
                        "x2": f"{CalendarImage.WIDTH_LEFT_SPACE + CalendarImage.SIZE_DAY_SQUARE * (j + 1)}mm",
                        "y1": f"{y1}mm",
                        "y2": f"{y2}mm",
                    },
                ):
                    pass

    def __draw_text(
        self, _e, attrib: t.Dict[str, t.Union[str, float]], text: str
    ) -> None:
        attrib["y"] = "{}mm".format(text_y(attrib["y"], attrib["font-size"]))
        attrib["font-size"] = "{}pt".format(attrib["font-size"])
        with _e("text", attrib, text):
            pass

    def __draw_title(self, _e) -> None:
        self.__draw_text(
            _e,
            {
                "fill": CalendarImage.BLACK,
                "font-size": CalendarImage.FONT_SIZE_LARGE,
                "x": "5mm",
                "y": 9.5,
            },
            "帝國火星暦",
        )
        self.__draw_text(
            _e,
            {
                "fill": CalendarImage.BLACK,
                "font-size": CalendarImage.FONT_SIZE_LARGE,
                "x": "11mm",
                "y": 18.0,
            },
            f"{self.imdt.year}年",
        )
        x = 10 + (
            CalendarImage.FONT_SIZE_BOLD_LARGE * 0.7 * 0.353
            if self.imdt.month in range(10)
            else 0
        )
        self.__draw_text(
            _e,
            {
                "fill": CalendarImage.BLACK,
                "font-family": CalendarImage.FONT_FAMILY_BOLD,
                "font-size": CalendarImage.FONT_SIZE_BOLD_LARGE,
                "x": f"{x}mm",
                "y": 28.0,
            },
            f"{self.imdt.month}月",
        )
        self.__draw_text(
            _e,
            {
                "fill": CalendarImage.BLACK,
                "font-size": CalendarImage.FONT_SIZE_LARGE,
                "x": "9.5mm",
                "y": 42.0,
            },
            f"({self.imdt.japanese_month_name}月)",
        )
        self.__draw_text(
            _e,
            {
                "fill": CalendarImage.GRAY,
                "font-size": CalendarImage.FONT_SIZE_ANNOTATION,
                "x": f"{CalendarImage.WIDTH_LEFT_SPACE - 5.5}mm",
                "y": 52.0,
            },
            "～",
        )
        with _e(
            "svg",
            {
                "height": "8mm",
                "style": """
                background-color: transparent;
                """,
                "width": f"{CalendarImage.WIDTH_LEFT_SPACE - 8}mm",
                "x": "2mm",
                "y": "52mm",
            },
        ) as _e:
            weekdays = ["月", "火", "水", "木", "金", "土", "日"]
            grdt_start = imdt_to_grdt(self.imdt, self.grdt_timezone)
            grdt_start_weekday = weekdays[grdt_start.weekday - 1]
            grdt_end = imdt_to_grdt(self.__next_imdt_month(), self.grdt_timezone)
            grdt_end_weekday = weekdays[grdt_end.weekday - 1]
            self.__draw_text(
                _e,
                {
                    "fill": CalendarImage.GRAY,
                    "font-size": CalendarImage.FONT_SIZE_ANNOTATION,
                    "text-anchor": "end",
                    "x": "100%",
                    "y": 0.0,
                },
                "{}/{}/{}({}){:02}:{:02}:{:02}".format(
                    grdt_start.year,
                    grdt_start.month,
                    grdt_start.day,
                    grdt_start_weekday,
                    grdt_start.hour,
                    grdt_start.minute,
                    grdt_start.second,
                ),
            )
            text = ""
            if grdt_start.year != grdt_end.year:
                text += f"{grdt_end.year}/"
            text += "{}/{}({}){:02}:{:02}:{:02}".format(
                grdt_end.month,
                grdt_end.day,
                grdt_end_weekday,
                grdt_end.hour,
                grdt_end.minute,
                grdt_end.second,
            )
            self.__draw_text(
                _e,
                {
                    "fill": CalendarImage.GRAY,
                    "font-size": CalendarImage.FONT_SIZE_ANNOTATION,
                    "text-anchor": "end",
                    "x": "100%",
                    "y": 4.0,
                },
                text,
            )

    def __next_imdt_month(self) -> ImperialDateTime:
        return self.imdt.copy().next_month()
