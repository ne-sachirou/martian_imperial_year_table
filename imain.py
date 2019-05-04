import math


class GregorianDateTime(object):
    """グレゴリオ暦の日時"""

    intercept = 1721088.5

    def __init__(self, year, month, day, hour, minute, second, timezone):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.timezone = timezone

    def __eq__(self, other):
        if not isinstance(other, GregorianDateTime):
            return False
        return self.__dict__ == other.__dict__


class JulianDay(object):
    """ユリウス通日"""

    def __init__(self, julian_day):
        self.julian_day = julian_day

    def __eq__(self, other):
        if not isinstance(other, JulianDay):
            return False
        return math.isclose(self.julian_day, other.julian_day, abs_tol=0.00001)


class TerrestrialTime(object):
    """地球時(テレストリアルタイム)"""

    def __init__(self, terrestrial_time):
        self.terrestrial_time = terrestrial_time

    def __eq__(self, other):
        if not isinstance(other, TerrestrialTime):
            return False
        return math.isclose(self.terrestrial_time, other.terrestrial_time, abs_tol=0.00001)


def gregorian_date_time_to_julian_day(gregorian_date_time):
    """グレゴリオ暦の日時をユリウス通日に變換する"""

    if gregorian_date_time.month in [1, 2]:
        tweaked_year = gregorian_date_time.year - 1
        tweaked_month = gregorian_date_time.month + 12
    else:
        tweaked_year = gregorian_date_time.year
        tweaked_month = gregorian_date_time.month

    return JulianDay(
        math.floor(tweaked_year * 365.25) +
        math.floor(tweaked_year / 400) -
        math.floor(tweaked_year / 100) +
        math.floor((tweaked_month - 2) * 30.59) +
        gregorian_date_time.day +
        gregorian_date_time.hour / 24 +
        gregorian_date_time.minute / (24 * 60) +
        gregorian_date_time.second / (24 * 60 * 60) -
        gregorian_date_time.timezone / 24 +
        gregorian_date_time.intercept)


def julian_day_to_gregorian_date_time(julian_day, timezone):
    """ユリウス通日をグレゴリオ暦の日時に變換する"""
#參考ページ http://astronomy.webcrow.jp/time/julianday-gregoriancalendar.html
    A = math.floor(julian_day.julian_day + timezone / 24 + 68569.5)
    B = julian_day.julian_day + timezone / 24 + 0.5
    a = math.floor(A / 36524.25)
    b = A - math.floor(36524.25 * a + 0.75)
    c = math.floor((b + 1) / 365.25025)
    d = b - math.floor(365.25 * c) + 31
    e = math.floor(d / 30.59)
    f = math.floor(e / 11)
    u = 100 * (a - 49) + c + f
    v = e - 12 * f + 2
    w = d - math.floor(30.59 * e) + (B % 1)
    x = (w % 1) * 24
    y = (x % 1) * 60
    z = (y % 1) * 60
    gregorian_date_time = GregorianDateTime(
        u, v , math.floor(w), math.floor(x), math.floor(y), math.floor(z), timezone)
    return gregorian_date_time


def julian_day_to_julian_year(julian_day):
    """ユリウス通日をユリウス年表示に變換する"""

    julian_day_to_julian_year_intercept = 1721117.5
    tweaked_julian_day = julian_day.julian_day - julian_day_to_julian_year_intercept
 # ユリウス暦0年3月1日正子を0とする通算日數を計算。
    quadrennium = divmod(tweaked_julian_day, (365 * 4 + 1))
    if quadrennium[1] < 365:
        quadrennial_year = 0
    elif quadrennium[1] < 365 * 2:
        quadrennial_year = 1
    elif quadrennium[1] < 365 * 3:
        quadrennial_year = 2
    else:
        quadrennial_year = 3
    julian_year = quadrennium[0] * 4 + quadrennial_year
    annual_day = quadrennium[1] - quadrennial_year * 365
    if annual_day >= 306:  # 306は3月から12月の日數。過ぎると翌年。
        julian_year += 1
        annual_day -= 306
    else:
        if julian_year % 4 == 0:
            annual_day += 31 + 29
        else:
            annual_day += 31 + 28
    if julian_year % 4 == 0:
        julian_year += annual_day / 366
    else:
        julian_year += annual_day / 365
    return julian_year


def julian_day_to_gregorian_year(julian_day):
    """ユリウス通日をグレゴリオ年表示に變換する"""
    
    gregorian_date_time = julian_day_to_gregorian_date_time(julian_day, 0)
    january_1st = GregorianDateTime(gregorian_date_time.year, 1, 1, 0, 0, 0, 0)
    next_january_1st = GregorianDateTime(gregorian_date_time.year + 1, 1, 1, 0, 0, 0, 0)
    julian_day_of_january_1st = gregorian_date_time_to_julian_day(january_1st) 
    julian_day_of_next_january_1st = gregorian_date_time_to_julian_day(next_january_1st)
 # 年内日數の小數表示
    annual_day = (julian_day.julian_day - julian_day_of_january_1st.julian_day) \
    / (julian_day_of_next_january_1st.julian_day - julian_day_of_january_1st.julian_day)
    gregorian_year = gregorian_date_time.year + annual_day
    return gregorian_year


def julian_day_to_year_number(julian_day):
    """ユリウス通日から變數year_numberを算出する"""
    
    calendar_reform = 2299160.5
    if julian_day.julian_day < calendar_reform:
        year_number = julian_day_to_julian_year(julian_day)
    else:
        year_number = julian_day_to_gregorian_year(julian_day)
    return year_number


def year_number_to_delta_t(year_number):
    """year_numberからΔTを算出する"""

    if year_number < -500:
        delta_u = (year_number - 1820) / 100
        delta_t = -20 + 32 * delta_u ** 2
    elif year_number < 500:
        delta_u = year_number / 100
        delta_t = 10583.6 \
                - 1014.41 * delta_u \
                + 33.78311 * delta_u ** 2 \
                - 5.952053 * delta_u ** 3 \
                - 0.1798452 * delta_u ** 4 \
                + 0.022174192 * delta_u ** 5 \
                + 0.0090316521 * delta_u ** 6
    elif year_number < 1600:
        delta_u = (year_number - 1000) / 100
        delta_t = 1574.2 \
                - 556.01 * delta_u \
                + 71.23472 * delta_u ** 2 \
                + 0.319781 * delta_u ** 3 \
                - 0.8503463 * delta_u ** 4 \
                - 0.005050998 * delta_u ** 5 \
                + 0.0083572073 * delta_u ** 6
    elif year_number < 1700:
        delta_u = year_number - 1600
        delta_t = 120 \
                - 0.9808 * delta_u \
                - 0.01532 * delta_u ** 2 \
                + delta_u ** 3 / 7129
    elif year_number < 1800:
        delta_u = year_number - 1700
        delta_t = 8.83 \
                + 0.1603 * delta_u \
                - 0.0059285 * delta_u ** 2 \
                + 0.00013336 * delta_u ** 3 \
                - delta_u ** 4 / 1174000
    elif year_number < 1860:
        delta_u = year_number - 1800
        delta_t = 13.72 \
                - 0.332447 * delta_u \
                + 0.0068612 * delta_u ** 2 \
                + 0.0041116 * delta_u ** 3 \
                - 0.00037436 * delta_u ** 4 \
                + 0.0000121272 * delta_u ** 5 \
                - 0.0000001699 * delta_u ** 6 \
                + 0.000000000875 * delta_u ** 7
    elif year_number < 1900:
        delta_u = year_number - 1860
        delta_t = 7.62 \
                + 0.5737 * delta_u \
                - 0.251754 * delta_u ** 2 \
                + 0.01680668 * delta_u ** 3 \
                - 0.0004473624 * delta_u ** 4 \
                + delta_u ** 5 / 233174
    elif year_number < 1920:
        delta_u = year_number - 1900
        delta_t = -2.79 \
                + 1.494119 * delta_u \
                - 0.0598939 * delta_u ** 2 \
                + 0.0061966 * delta_u ** 3 \
                - 0.000197 * delta_u ** 4
    elif year_number < 1941:
        delta_u = year_number - 1920
        delta_t = 21.20 \
                + 0.84493 * delta_u \
                - 0.076100 * delta_u ** 2 \
                + 0.0020936 * delta_u ** 3 
    elif year_number < 1961:
        delta_u = year_number - 1950
        delta_t = 29.07 \
                + 0.407 * delta_u \
                - delta_u ** 2 / 233 \
                + delta_u ** 3 / 2547
    elif year_number < 1986:
        delta_u = year_number - 1975
        delta_t = 45.45 \
                + 1.067 * delta_u \
                - delta_u ** 2 / 260 \
                - delta_u ** 3 / 718
    elif year_number < 2005:
        delta_u = year_number - 2000
        delta_t = 63.86 \
                + 0.3345 * delta_u \
                - 0.060734 * delta_u ** 2 \
                + 0.0017275 * delta_u ** 3 \
                + 0.000651814 * delta_u ** 4 \
                + 0.00002373599 * delta_u ** 5
    elif year_number < 2050:
        delta_u = year_number - 2000
        delta_t = 63.795 \
                + 0.1287 * delta_u \
                + 0.0091 * delta_u ** 2
 # 2005-2050の近似式は自作。參考文獻に準拠した式をコメントアウトして置く。
 # 參考文獻: https://eclipse.gsfc.nasa.gov/SEhelp/deltatpoly2004.html
 #   elif year_number < 2050:
 #       delta_u = year_number - 2000
 #       delta_t = 62.92 \
 #               + 0.32217 * delta_u \
 #               + 0.005589 * delta_u ** 2
    elif year_number < 2150:
        delta_t = -20 \
        + 32 * ((year_number - 1820)/100) ** 2 \
        - 0.5628 * (2150 - year_number)
    else:
        delta_u = (year_number - 1820) / 100
        delta_t = -20 + 32 * delta_u ** 2
    return delta_t


def julian_day_to_delta_t(julian_day):
    """ユリウス通日からΔTを算出する"""
    
    delta_t = year_number_to_delta_t(
        julian_day_to_year_number(julian_day))
    return delta_t


def julian_day_to_terrestrial_time(julian_day):
    """ユリウス通日を地球時に變換する"""

    delta_t = julian_day_to_delta_t(julian_day)
    terrestrial_time = TerrestrialTime(julian_day.julian_day + delta_t / (24 * 60 * 60))
    return terrestrial_time


def gregorian_date_time_to_terrestrial_time(gregorian_date_time):
    """グレゴリオ暦の日時を地球時に變換する"""
    
    julian_day = gregorian_date_time_to_julian_day(gregorian_date_time)
    terrestrial_time = julian_day_to_terrestrial_time(julian_day)
    return terrestrial_time


def terrestrial_time_to_julian_day(terrestrial_time):
    """地球時をユリウス通日に變換する"""

    delta_t = julian_day_to_delta_t(JulianDay(terrestrial_time.terrestrial_time))
    julian_day_prime = JulianDay(terrestrial_time.terrestrial_time - delta_t / (24 * 60 *60))
    terrestrial_time_prime = julian_day_to_terrestrial_time(julian_day_prime)
    julian_day = JulianDay(julian_day_prime.julian_day \
               + terrestrial_time.terrestrial_time - terrestrial_time_prime.terrestrial_time)
    return julian_day


def terrestrial_time_to_msd(terrestrial_time):
    """地球時からMSDを算出する"""
    msd = (terrestrial_time.terrestrial_time - 2451545 - 4.5) / 1.027491252 + 44796 - 0.00096
    return msd


def gregorian_date_time_to_msd(gregorian_date_time):
    """グレゴリオ暦の日時からMSDを算出する"""
    msd = terrestrial_time_to_msd(gregorian_date_time_to_terrestrial_time(gregorian_date_time))
    return msd


def gregorian_date_time_to_imperial_sol_number(gregorian_date_time):
    """グレゴリオ暦の日時から帝國火星日を算出する"""
    isn = gregorian_date_time_to_msd(gregorian_date_time) - 0.375 + 901193
    return isn


def imperial_sol_number_to_msd(imperial_sol_number):
    """帝國火星日からMSDを算出する"""
    msd = imperial_sol_number + 0.375 - 901193
    return msd


def msd_to_terrestrial_time(msd):
    """MSDから地球時を算出する"""
    terrestrial_time = 1.027491252 * (msd - 44796 + 0.00096) + 2451545 + 4.5
    return TerrestrialTime(terrestrial_time)

def imperial_sol_number_to_gregorian_date_time(imperial_sol_number,timezone):
    """帝國火星日をグレゴリオ暦の日時に變換する"""
    gregorian_date_time = julian_day_to_gregorian_date_time(
    	terrestrial_time_to_julian_day(
    		msd_to_terrestrial_time(
    			imperial_sol_number_to_msd(
    				imperial_sol_number))),timezone)
    return gregorian_date_time


# 以下テスト用函數。


def g2tt(y,m,d,h,minute,sec,tz):
    """test""" 
    
    gdt = GregorianDateTime(y,m,d,h,minute,sec,tz)
    tt = gregorian_date_time_to_terrestrial_time(gdt)
    print(tt.__dict__)


def g2dt(y,m,d,h,minute,sec,tz):
    """test"""
    
    gdt = GregorianDateTime(y,m,d,h,minute,sec,tz)
    dt = year_number_to_delta_t(
    	julian_day_to_year_number(
    		gregorian_date_time_to_julian_day(gdt)))
    print(dt)


def g2jd():
    """test"""

    Gyear = float(input('年:'))
    Gmonth = float(input('月:'))
    Gday = float(input('日:'))
    Ghour = float(input('時:'))
    Gminute = float(input('分:'))
    Gsecond = float(input('秒:'))
    Gtzone = float(input('時差:'))
    gdt = GregorianDateTime(Gyear, Gmonth, Gday, Ghour, Gminute, Gsecond, Gtzone)
    jd = gregorian_date_time_to_julian_day(gdt)
    print('ユリウス通日は:' + str(jd.julian_day))
    

def jd2g():
    """test2"""
    Jday = float(input('ユリウス通日:'))
    Jtzone = float(input('時差:'))
    jd = JulianDay(Jday)
    gdt = julian_day_to_gregorian_date_time(jd, Jtzone)
    print('グレゴリオ暦は:' + \
        str(gdt.year) + '年' + \
        str(gdt.month) + '月' + \
        str(gdt.day) + '日' + \
        str(gdt.hour) + '時' + \
        str(gdt.minute) + '分' + \
        str(gdt.second) + '秒, 時差' + \
        str(gdt.timezone) + '時間')


def decimal2time(days):
    """小數表示を時分秒に"""
    decimal = days % 1
    hour = math.floor(decimal * 24)
    minute = math.floor((decimal * 1440) % 60)
    second = math.floor((decimal * 86400) % 60)
    print(str(hour) + ':' + str(minute) + ':' + str(second))
