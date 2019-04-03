import math

from scipy.special._ufuncs import radian

# 싼타페 DM의 윤거전 = 1628 mm = 1.628 meter
# 윤거전 : 전륜 바퀴 2개에 대해, 각각 바퀴의 중심 위치간의 거리


Tire_width = 1.628     # 싼타페 윤거전 https://auto.naver.com/car/lineup.nhn?yearsId=68095

whole_x = 0         # initial_x_coordinate
whole_y = 0         # initial_y_coordinate
whole_angle = 0    # initial_heading
delta_angle = 0     # value initialization
lower_var = 18      # km/h to meter/0.2sec
# lower_var = 18/5  # km/h to meter/1sec
print(whole_x, whole_y, whole_angle, delta_angle)

# -------------------------------------------- 1회 데이터 인입시
# -------------------------------------------- Data update First
FL = 30.2 / lower_var  # 30.2 km 라면, (30.2 * 1000 / (3600) ) / 5 ==> 30.2 / 18
FR = 30.3 / lower_var  # 30.2 km 라면, (30.3 * 1000 / (3600) ) / 5 ==> 30.3 / 18
delta_angle = 90 - math.degrees(math.atan2(Tire_width, FR - FL))
distance = (FL+FR) / 2
whole_angle = whole_angle + delta_angle
whole_x = whole_x + distance * math.cos(math.radians(whole_angle))
whole_y = whole_y + distance * math.sin(math.radians(whole_angle))
print(whole_x, whole_y, whole_angle, delta_angle)

# -------------------------------------------- 2회 데이터 인입시
# -------------------------------------------- Data update Second
FL = 30.7 / lower_var  # 30.7 km 라면, (30.7 * 1000 / (3600) ) / 5 ==> 30.7 / 18
FR = 30.5 / lower_var  # 30.5 km 라면, (30.5 * 1000 / (3600) ) / 5 ==> 30.5 / 18
delta_angle = 90 - math.degrees(math.atan2(Tire_width, FR - FL))
distance = (FL+FR) / 2
whole_angle = whole_angle + delta_angle
whole_x = whole_x + distance * math.cos(math.radians(whole_angle))
whole_y = whole_y + distance * math.sin(math.radians(whole_angle))
print(whole_x, whole_y, whole_angle, delta_angle)

# -------------------------------------------- 3회 데이터 인입시
# -------------------------------------------- Data update Third
FL = 30.1 / lower_var  # 30.1 km 라면, (30.1 * 1000 / (3600) ) / 5 ==> 30.1 / 18
FR = 30.5 / lower_var  # 30.5 km 라면, (30.5 * 1000 / (3600) ) / 5 ==> 30.5 / 18
delta_angle = 90 - math.degrees(math.atan2(Tire_width, FR - FL))
distance = (FL+FR) / 2
whole_angle = whole_angle + delta_angle
whole_x = whole_x + distance * math.cos(math.radians(whole_angle))
whole_y = whole_y + distance * math.sin(math.radians(whole_angle))
print(whole_x, whole_y, whole_angle, delta_angle)


def dr_one_step(whole_x, whole_y, whole_angle, Tire_width, FL, FR, freq):
    # freq should be 1000 = 1s, 200 = 0.2s
    lower_var = 18 / (freq/200)  # km/h to meter/0.2sec, 1sec...
    FL_meter = FL / lower_var
    FR_meter = FR / lower_var

    delta_angle = 90 - math.degrees(math.atan2(Tire_width, FR_meter - FL_meter))
    distance = (FL_meter + FR_meter) / 2
    whole_angle = whole_angle + delta_angle
    whole_x = whole_x + distance * math.cos(math.radians(whole_angle))
    whole_y = whole_y + distance * math.sin(math.radians(whole_angle))
    print(whole_x, whole_y, whole_angle, delta_angle)
    return whole_x, whole_y, whole_angle


whole_x, whole_y, whole_angle=dr_one_step(0,0,0,1.628, 30.2, 30.3, 200)
whole_x, whole_y, whole_angle=dr_one_step(whole_x, whole_y, whole_angle,1.628, 30.7, 30.5, 200)

dr_one_step(whole_x, whole_y, whole_angle,1.628, 30.7, 30.5, 200)

