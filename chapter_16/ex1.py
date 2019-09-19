# write a function called mult_time that takes a Time object
# and a number and returns a new Time object
# that contains the product of the original time and the number

# should it multiply the hour and mins separately,
# or just multiply the seconds only (after converting
# to int number of seconds)?
# acutally, I think it would have the same result either way
# mult 2 mins by 3 gives 6 mins. converting 2 mins to secs
# gives 120 sec, times 3 gives 360 sec, which is 6 mins.
# yes. it doesn't matter. so it will be easiest to
# use the time_to_int function

# calls of print_time from sec4ex1 execute (#why?)
from sec4ex1 import time_to_int, int_to_time, Time, print_time


def mult_time(time, x):
    return int_to_time(x * time_to_int(time))



time = Time()
time.hour = 4
time.minute = 30
time.second = 15

print('hi')
print_time(time)
new_time = mult_time(time, 2)
print_time(new_time)
print_time(time)


# next write a function that takes a time object
# and a distance number and returns a Time
# object that represents the average pace (time per mile)
print('next part')


def pace(time, d):
    return mult_time(time, 1/d)

dist = 3

time = Time()
time.hour = 0
time.minute = 35
time.second = 22

pace_var = pace(time, dist)
print_time(pace_var)
