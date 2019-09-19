# use the datetime module to write a program that gest the
# current date and prints the day of the week

import datetime
# part 1

now = datetime.datetime.now()

#print(now.weekday()) # on 2019-09-18

### the solution did this useing now.strftime (return a string representation of the date)

# part 2
# write a program that takes a birthday as input and
# prints the user's age and then umber of days, hours
# minutes, and seconds until their next birthday

bday = datetime.datetime.fromisoformat('1986-09-19')

current_datetime = datetime.datetime.now()
bday = bday
#print((current_datetime - bday))
#print((current_datetime - bday)/365.25, 'actually this is in years' )
bday = bday.replace(year = 2019)
#print(bday)

if current_datetime > bday:
    bday = bday.replace(year = 2020)

#print(bday- current_datetime)

# the above is kind of messy, but I'm calling it good enough

# part 3
# try to think about design
# we start with two dates. on some date, the difference
# from the earlier birthday to the current time will
# be twice the difference from the later birthday to the
# current time.
# we could write the ratio of the ages as
# (some_datetime - bday1) / (some_datetime - bday2)
# which we think of as a function of some_datetime.
# then we iterate some_datetime until we get an answer
# I'm thinking binary search maybe
# oh wait... when the time delta from the first birthday
# to the second birthday is equal to the time delta from
# the second birthday to the some_datetime, the condition
# will be met. so that's actually pretty easy
print('part 3')
bday1 = datetime.datetime.fromisoformat('1985-07-13')
bday2 = datetime.datetime.fromisoformat('2005-09-19')
if bday1 > bday2:
    bday1, bday2 = bday2, bday1


time_delta = bday2 - bday1
some_datetime = bday2 + time_delta
print(some_datetime)


# part 4: I'm going to make an executive decision and say that
# it would be more effective to look up the answer for
# this one in the interest of moving through the book
