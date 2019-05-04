import math
from imain import *


def terrestrial_time_to_offset_t_j2000(terrestrial_time):
    """地球時を基にしてJ2000元期からの經過日數を求める"""
    offset_t_j2000 = terrestrial_time.terrestrial_time - 2451545.0
    return offset_t_j2000


def offset_t_j2000_to_mars_mean_anomaly(offset_t_j2000):
    """Mを求める。"""
    mars_mean_anomaly = 19.3871 + 0.52402073 * offset_t_j2000
    return mars_mean_anomaly


def offset_t_j2000_to_angle_of_fictitious_mean_sun(offset_t_j2000):
    """α_FMSを求める。"""
    angle_of_fictitious_mean_sun = 270.3871 + 0.524038496 * offset_t_j2000
    return angle_of_fictitious_mean_sun


def offset_t_j2000_to_perturbers(offset_t_j2000):
    """PBS=攝動角を求める。"""
    amp = [0.0071, 0.0057, 0.0039, 0.0037, 0.0021, 0.0020, 0.0018]
    tau = [2.2353, 2.7543, 1.1177, 15.7866, 2.1354, 2.4694, 32.8493]
    phi = [49.409, 168.173, 191.837, 21.736, 15.704, 95.528, 49.095]
    perturbers = 0
    for i in range(0, len(amp)):
        angle = (360 / 365.25) * offset_t_j2000 / tau[i] + phi[i]
        perturbers += amp[i] * math.cos(math.radians(angle))
    return perturbers


def offset_t_j2000_to_equation_of_center(offset_t_j2000):
    """ν-Mを求める。"""
    m_m_a = offset_t_j2000_to_mars_mean_anomaly(offset_t_j2000)
    angle_m = math.radians(m_m_a)
    pbs = offset_t_j2000_to_perturbers(offset_t_j2000)
    equation_of_center = (10.691 + (3.0 * 10 ** -7) * offset_t_j2000) * math.sin(angle_m) \
                       + 0.623 * math.sin(2 * angle_m) \
                       + 0.050 * math.sin(3 * angle_m) \
                       + 0.005 * math.sin(4 * angle_m) \
                       + 0.0005 * math.sin(5 * angle_m) + pbs
    return equation_of_center


def offset_t_j2000_to_areocentric_solar_longitude(offset_t_j2000):
    """Ls=火星中心太陽黃經を求める。"""
    areocentric_solar_longitude = (offset_t_j2000_to_angle_of_fictitious_mean_sun(offset_t_j2000) \
        + offset_t_j2000_to_equation_of_center(offset_t_j2000)) % 360
    return areocentric_solar_longitude


def gregorian_date_time_to_areocentric_solar_longitude(gregorian_date_time):
    """グレゴリオ暦からLsを計算する"""
    areocentric_solar_longitude = offset_t_j2000_to_areocentric_solar_longitude(
        terrestrial_time_to_offset_t_j2000(
            gregorian_date_time_to_terrestrial_time(gregorian_date_time)))
    return areocentric_solar_longitude



 # 以下テスト函數

def tt2ls(terrestrial_time):

    j2000 = terrestrial_time_to_offset_t_j2000(terrestrial_time)
    ls = offset_t_j2000_to_areocentric_solar_longitude(j2000)
    return ls
    
    
def g2ls(y,m,d,h,minute,sec,tz):
    """test""" 
    
    gdt = GregorianDateTime(y,m,d,h,minute,sec,tz)
    tt = gregorian_date_time_to_terrestrial_time(gdt)
    ls = tt2ls(tt)
    return ls
