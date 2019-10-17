"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

# this will need to be changed
class Time: #done
    """Represents the time of day.

    attribute: second
    """
    def __init__(self, hour=0, minute=0, second=0): #done
        """Initializes a time object.

        hour: int
        minute: int
        second: int or float
        """
        minutes = hour * 60 + minute
        seconds = minutes * 60 + second
        self.second = seconds


    def __str__(self): #done
        """Returns a string representation of the time."""
        minutes, second = divmod(self.second, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def print_time(self): #done (didn't need change)
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self): # done
        """Computes the number of seconds since midnight."""
        return self.second

    def is_after(self, other): #done
        """Returns True if t1 is after t2; false otherwise."""
        return self.second > other.second

    def __add__(self, other): #okay
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other): #okay
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other): #done
        """Adds two time objects."""
        seconds = self.second + other.second
        return int_to_time(seconds)

    def increment(self, seconds): # okay
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self): # not used
        """Checks whether a Time object satisfies the invariants."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True


def int_to_time(seconds): #done
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time(second = seconds)
    return time


def main():
    # Time() ie init, must take (x, y, z) (and self)
    start = Time(9, 45, 00)
    # print time must take a time object (with just the attribute second, and print formatted time)
    start.print_time()

    # increment  must take a number of seconds (and self), and return a time object
    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    # end.is_after(start) must take self, and a time object, and return a boolean
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()


# okay. looks like it all works!
# here's the output
"""
09:45:00
10:07:17
Is end after start?
True
Using __str__
09:45:00 10:07:17
11:20:00
10:07:17
10:07:17
Example of polymorphism
23:01:00
"""
