# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:49:43 2019

@author: user2
"""
kilometers = 10

miles = kilometers / 1.61

print(miles)


minutes = 42

seconds = 42

total_seconds = 42 + 42 * 60

# average pace in time per mile (in minutes and seconds)
avg_pace = total_seconds / miles
print(avg_pace)

avg_pace_min = avg_pace // 60
avg_pace_seconds = avg_pace % 60
print(avg_pace_min)
print(avg_pace_seconds)

#average speed in miles per hour
print('miles', miles, 'total_seconds', total_seconds)
hours = total_seconds / 60 / 60

speed = miles / hours

print('speed', speed)