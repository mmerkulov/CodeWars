# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and
# returns it in cm per second, rounded down to the integer (= floored).
#
# For example:
# 1.08 --> 30
#
# Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

def cockroach_speed(s):
    return int((s / 3.6) * 100)


# 1 км = 1000 м
# 1 час = 60 мин
# км/ч = м/с
# 30 km/h = 8.3 m/s

# s - расстояние, v - скорость, t - время
# s = v * t
# v = 30 km/h = 8.3 m/s
print(30 * 1000 / (1 * 3600))

x = 1.08
print(cockroach_speed(x))

w = 'world'
print(w[::-1])
