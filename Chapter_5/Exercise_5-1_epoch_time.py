'''
this is a solution to exercise 5.1 in Think Python 2e
the aim is to convert epoch time
to days, hours, minutes, and seconds
'''




import time
seconds = time.time()

# convert to minutes and find the remainder in seconds
minutes = seconds // 60
seconds = seconds % 60

# convert to hours and find the remainder in seconds
hours = minutes // 60
minutes = minutes % 60

# convert to days and find the remainder in hours
days = hours // 24
hours = hours % 24

print(f'The time of day is {hours} hours, {minutes} minutes, and {seconds} seconds')
print(f'And it hase been {days} days since the start of the epoch')
