DEGREE = "\u00B0"
def dms(number):
    degrees, minutes, seconds = 0, 0 ,0
    split = str(number).split(".")

    if len(split) > 0:
        degrees = int(number)
    if len(split) > 1:
        minutes = (number - int(degrees)) * 60
        seconds = (minutes - int(minutes)) * 60

    return f"{degrees}{DEGREE}{'%02d' % minutes}'{'%02d' % seconds}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
