# write a correct version of implement that doesn't
# use loops

class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

def print_time(t):
    print('{%.2d}:{%.2d}:{%.2d}' % (t.hour, t.minute, t.second))


def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.minute += 1 * time.second // 60
        time.second -= 60 * (time.second // 60)


    if False: #time.minute >= 60:
        time.minute -= 60
        time.hour += 1


time = Time()
time.hour = 7
time.minute = 11
time.second = 5

print_time(time)
increment(time, 120)
print_time(time)
