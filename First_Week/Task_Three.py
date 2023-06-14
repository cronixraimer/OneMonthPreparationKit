import math
import os
import random
import re
import sys

s = input()



hours, minutes, seconds = map(int, s[:-2].split(':'))

if s[-2:] == "AM" and hours == 12:
    hours -= 12

if s[-2:] == "PM" and hours != 12:
    hours += 12
formatted_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

print(formatted_time)
