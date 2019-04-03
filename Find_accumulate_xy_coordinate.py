import math

from scipy.special._ufuncs import radian

# 싼타페 DM의 윤거전 = 1628 mm = 1.628 meter
# 윤거전 : 전륜 바퀴 2개에 대해, 각각 바퀴의 중심 위치간의 거리
# 100km 고속주행시 양 바퀴의 속도가 약 0.1km 차이일때
# 왼쪽 바퀴는 100.1 km / h, 오른쪽바퀴는 100.2km 라고하면
# 100.1 * 1000 / 3600 ==> meter/sec
# 100.2 * 1000 / 3600 ==> meter/sec
# FL-FR = 5.56 - 5.578

print(math.degrees(math.atan2(1.628, 0)))
print(90 - math.degrees(math.atan2(1.628, -0.018)))

Tire_width = 1.628     # 김보근싼타페

whole_x = 0         # initial_x_coordinate
whole_y = 0         # initial_y_coordinate
whole_angle = 0    # initial_heading
delta_angle = 0     # value initialization
lower_var = 18      # km/h to meter/0.2sec
# lower_var = 18/5  # km/h to meter/1sec
print(whole_x, whole_y, whole_angle, delta_angle)

# --------------------------------------------
FL = 30.2 / lower_var  # 30.2 km 라면, (30.2 * 1000 / (3600) ) / 5 ==> 30.2 / 18
FR = 30.3 / lower_var  # 30.2 km 라면, (30.3 * 1000 / (3600) ) / 5 ==> 30.3 / 18
delta_angle = 90 - math.degrees(math.atan2(Tire_width, FR - FL))
distance = (FL+FR) / 2
whole_angle = whole_angle + delta_angle
whole_x = whole_x + distance * math.cos(math.radians(whole_angle))
whole_y = whole_y + distance * math.sin(math.radians(whole_angle))
print(whole_x, whole_y, whole_angle, delta_angle)

# --------------------------------------------
FL = 30.7 / lower_var  # 30.2 km 라면, (30.2 * 1000 / (3600) ) / 5 ==> 30.2 / 18
FR = 30.5 / lower_var  # 30.2 km 라면, (30.3 * 1000 / (3600) ) / 5 ==> 30.3 / 18
delta_angle = 90 - math.degrees(math.atan2(Tire_width, FR - FL))
distance = (FL+FR) / 2
whole_angle = whole_angle + delta_angle
whole_x = whole_x + distance * math.cos(math.radians(whole_angle))
whole_y = whole_y + distance * math.sin(math.radians(whole_angle))
print(whole_x, whole_y, whole_angle, delta_angle)

# --------------------------------------------
FL = 30.1 / lower_var  # 30.2 km 라면, (30.2 * 1000 / (3600) ) / 5 ==> 30.2 / 18
FR = 30.5 / lower_var  # 30.2 km 라면, (30.3 * 1000 / (3600) ) / 5 ==> 30.3 / 18
delta_angle = 90 - math.degrees(math.atan2(Tire_width, FR - FL))
distance = (FL+FR) / 2
whole_angle = whole_angle + delta_angle
whole_x = whole_x + distance * math.cos(math.radians(whole_angle))
whole_y = whole_y + distance * math.sin(math.radians(whole_angle))
print(whole_x, whole_y, whole_angle, delta_angle)


