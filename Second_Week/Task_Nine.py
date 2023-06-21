import re
month = []

def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 29    #first mistake was 28 instead of 29
    elif year % 100 == 0:
        month[2] = 28    # second mistake was 29 instead of 28
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28

def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31

def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while(True):
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1  #Third mistake was 1000 it has to be 10000 to reach million
        if x % 4 == 0 or x % 7 == 0:  #Fourt mistake was and instead of or
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 =  y1 + 1
                m1 = 1 #Last misteake was m1 = m1 + 1 instead of m1 = 1 if I would use m1 = m1 the date will greter and it will index issue and if I leave m1 = m1 + 1 it would count as 14 month in a year
                
    return result;

for i in range(1, 15):
    month.append(31)

line = input()
date = re.split('-| ', line)
d1 = int(date[0])
m1 = int(date[1])
y1 = int(date[2])
d2 = int(date[3])
m2 = int(date[4])
y2 = int(date[5])

result = findPrimeDates(d1, m1, y1, d2, m2, y2)
print(result)
