def isLeapYear(year: int):
    if( ( year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0):
        return True
    else:
        return False

def daysMonth(mon: int, year: int):
    daysMon = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if(mon == 2 and isLeapYear(year)):
        return daysMon[j] + 1
    else:    
        return daysMon[j]

startyear = 1901
endYear = 2000
startDay = 2 # 1 Jan 1901 was Tuesday
count = 0
for i in range(startyear, endYear+1):
    for j in range(1,13):
        mon = j + 1
        if(mon == 13):
            mon = 1    
        startDay = ( startDay + daysMonth(j, i) ) % 7
        
        if(startDay == 0):
            print(i, mon, startDay) 
            count += 1

print(count)