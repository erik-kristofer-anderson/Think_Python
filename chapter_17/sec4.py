from objects import *

start = Time()
start.hour = 5
start.minute = 3
start.second = 22

start.print_time()

finish = Time()
finish.hour = 5
finish.minute = 57
finish.second = 59

print(finish.is_after(start))
