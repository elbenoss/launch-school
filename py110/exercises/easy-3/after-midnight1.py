def time_of_day(integer):
    hours = integer / 60
    first = (hours % 24)
    second = (first - int(first)) * 60
    return f'{"%02.f" % first.__floor__()}:{"%02.f" % second}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
