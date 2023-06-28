import math
import os
import random
import re
import sys

s = input() #input from user



hours, minutes, seconds = map(int, s[:-2].split(':')) # spliting the user input by : into
#hours, minutes and seconds converting it map and where also spliting by -2

if s[-2:] == "AM" and hours == 12: #if check is our last 2 input AM  and hour equal to 12
    hours -= 12 # dicreasing it by 12 where our time from midnight till noon

if s[-2:] == "PM" and hours != 12: #if check is our last input 12 PM and is not 12
    hours += 12 #increasing our time input by 12 where will be converted to more then 12PM
    #like 13, 14 and so on
formatted_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

print(formatted_time)
