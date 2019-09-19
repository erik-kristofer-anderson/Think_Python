# write a pure version of increment that creates and
# returns a new Time object rather than modifying
# the parameter

class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

def print_time(t):
    print('{%.2d}:{%.2d}:{%.2d}' % (t.hour, t.minute, t.second))

import copy
def increment(time_in, seconds):
    time = copy.deepcopy(time_in)
    time.second += seconds

    if time.second >= 60:
        time.minute += 1 * time.second // 60
        time.second -= 60 * (time.second // 60)


    if False: #time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    return time


time = Time()
time.hour = 7
time.minute = 11
time.second = 5

print_time(time)
new_time = increment(time, 120)
print_time(new_time)
print_time(time)
