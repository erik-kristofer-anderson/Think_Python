# write a function called print_time that
# takes a time object and prints it in the format
# hh:mm:ss

class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

def print_time(t):
    print('{%.2d}:{%.2d}:{%.2d}' % (t.hour, t.minute, t.second))

# write a boolean function called is_after that takes two
# Time objects and returns tru if t1 follows t2 chronologically
# and False otherwise
# (challenge: don't use an if statement)
# [not sure how to do that]

def is_after(t1, t2):
    if t1.hour > t2.hour:
        return True
    elif t1.hour == t2.hour:
        if t1.minute > t2.minute:
            return True
        elif t1.minute == t2.minute:
            if t1.second > t2.second:
                return True
            else:
                return False
        else:
            return False
    else:
        return False





# time = Time()
# time.hour = 11
# time.minute = 59
# time.second = 30
#
# print_time(time)



# testing is_after(t1, t2)
t1 = Time()
t1.hour =7
t1.minute = 57
t1.second = 30

t2 = Time()
t2.hour = 10
t2.minute = 58
t2.second = 29

print(is_after(t1, t2))
# worked correctly for all the cases I tested
