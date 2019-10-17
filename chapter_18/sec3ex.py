class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def print_time(t):
        print('{%.2d}:{%.2d}:{%.2d}' % (t.hour, t.minute, t.second))

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second


    # tuple implementation
    def __lt__(self, other):
        return (self.hour, self.minute, self.second) < (other.hour, other.minute, other.second)



t1 = Time(5,54,11)
t2 = Time(5,54,11)
print(t1 > t2)
