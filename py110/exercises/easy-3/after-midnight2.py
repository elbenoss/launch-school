def before_midnight(time):
    time_split = time.split(":")
    first = int(time_split[0]) * 60
    second = int(time_split[1])
    return (1440 - (first + second)) % 1440

def after_midnight(time):
    time_split = time.split(":")
    first = int(time_split[0]) * 60
    second = int(time_split[1])
    return (first + second) % 1440

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
