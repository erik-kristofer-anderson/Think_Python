# 6:52 am, 1 mile at 8:15 minutes per mile, then 3 miles at 7:12 per mile. what time get home for breakfast?


# time spent running is (in seconds)
# 1 * (8 * 60 + 15) + 3 * (7 * 60 + 12)

# time of day (in seconds) is
# 6 * 60 * 60 + 52 * 60

# time in seconds from start of day to getting home
time_home_sec = 1 * (8 * 60 + 15) + 3 * (7 * 60 + 12) + 6 * 60 * 60 + 52 * 60

# time in minutes from start of day to time getting home, in minutes, rounded down
time_home_minutes = time_home_sec // 60

# how many seconds it is past the minute
sec_past_minute = time_home_sec % 60

# time from start of day to time hour in hours, rounded down
time_home_hours = time_home_minutes // 60

# number of minutes it is past the hour
minutes_past_hour = time_home_minutes % 60
print(time_home_hours, 'hours')
print(minutes_past_hour, 'minutes')
print(sec_past_minute, 'seconds')
