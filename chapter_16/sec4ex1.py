# as an exercise, rewrite increment using time_to_int
# and int_to_time

# start with the functions from this section

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


# here is the original function increment
#
# def increment(time, seconds):
#     time.second += seconds
#
#     if time.second >= 60:
#         time.minute += 1 * time.second // 60
#         time.second -= 60 * (time.second // 60)
#
#
#     if False: #time.minute >= 60:
#         time.minute -= 60
#         time.hour += 1

# will also need to define the class Time and the
# function print time
class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

def print_time(t):
    print('{%.2d}:{%.2d}:{%.2d}' % (t.hour, t.minute, t.second))

def increment(time, seconds):
    seconds = time_to_int(time) + seconds
    return int_to_time(seconds)

# test it


time = Time()
time.hour = 7
time.minute = 11
time.second = 5



print_time(time)
time = increment(time, 120)
print_time(time)

# I'll be interested to see whether allen, in his solution
# used a function that outputs time, or a function
# that modifies the time object?
