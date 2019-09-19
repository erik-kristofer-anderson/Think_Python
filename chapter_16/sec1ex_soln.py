# his solution uses tuples in a clever way


def is_after(t1, t2):
    """Returns True is t1 is after t2; false otherwise."""
    return (t1.hour, t1.minute, t1.second) > t2.hour, t2.minute, t2.second)
    #takes advantage of how tuples are compared for equality
