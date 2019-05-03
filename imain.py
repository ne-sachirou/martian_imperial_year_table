# 以下テスト用函數。


def g2tt(y, m, d, h, min, sec, tz):
    """test"""
    gdt = GregorianDateTime(y, m, d, h, min, sec, tz)
    tt = gregorian_date_time_to_terrestrial_time(gdt)
    print(tt.__dict__)


def g2dt(Gyear):
    """
    Gyear = float(input('年:'))
    Gmonth = float(input('月:'))
    Gday = float(input('日:'))
    Ghour = float(input('時:'))
    Gminute = float(input('分:'))
    Gsecond = float(input('秒:'))
    Gtzone = float(input('時差:'))
    gdt = GregorianDateTime(Gyear, Gmonth, Gday, Ghour, Gminute, Gsecond, Gtzone)
    """
    gdt = GregorianDateTime(Gyear, 0, 0, 0, 0, 0, 0)
    dt = year_number_to_delta_t(julian_day_to_year_number(gregorian_date_time_to_julian_day(gdt)))
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
