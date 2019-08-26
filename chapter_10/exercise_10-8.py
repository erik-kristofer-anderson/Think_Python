"""
if there are 23 students in you class, what are the
chances that two of you have the same birthday
"""
# approach: randomly sample collections of 23 birthdays,
# with the days selected randomly, and track the
# fraction of birthday matches
# pretend 365 days every year


import random

def has_duplicates(t):
    ts = sorted(t)
    for i in range(len(ts)-1):
        if ts[i] == ts[i+1]:
            return True
    return False



def chances():
    counter = 0
    i = 0
    while i < 100000:
        t = []
        for j in range(23):
            day = random.randint(1, 365)
            t.append(day)
        if has_duplicates(t):
            counter += 1


        i += 1

    return counter / i * 100

print(chances())

# result:
# between 50 and 51 for 10,000 combinations of 23 days
