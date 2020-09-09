"""importing math module"""

import math
print("Age Counter \n")

"""current date"""

day_e = 3
month_e = 8
year_e = 2020
print("Current Date is",day_e,"/",month_e,"/",year_e)
print("Enter DOB of birth")

"""input of DOB"""

day_s = int(input("Day: "))
month_s = int(input("Month: "))
year_s = int(input("year: "))
year_t = year_e - year_s

days_t = math.ceil((year_e - year_s) * 365 + (month_e - month_s) * 30.4 + (day_e - day_s))

rem = days_t % 365
if rem <= 364:
    month_rem = int( rem / 30.4 )
    rem_m = int(rem % 30.4)
    if rem_m <= 29:
       rem_d = rem_m
    else:
        month_rem = 0
else:
    year_rem = 0
hrs_t = days_t * 24
hrs_t = int(hrs_t)
wk_t = int(days_t / 7)
month_t = int(days_t / 30.4)
year_t = int(days_t / 365)

"""getting accurate time for originals"""

if hrs_t > 1:
    hrt = "hrs"
elif hrs_t <= 1:
    hrt = "hr"
else:
    hrs_t = hrs_t
if days_t > 1:
    dt = "days"
elif days_t <= 1:
    dt = "day"
else:
    days_t = days_t
if wk_t > 1:
    wkt = "wks"
elif wk_t <= 1:
    wkt = "wk"
else:
    wk_t = wk_t
if month_t > 1:
    mt = "mnths"
elif month_t <= 1:
    mt = "month"
else:
    month_t = month_t
    
"""getting remenders"""

if rem_d > 1:
    d = "days"
elif rem_d <= 1:
    d = "day"
else:
    rem_d = rem_d
if month_rem > 1:
    m = "months"
elif month_rem <= 1:
    m = "month"
else:
    month_rem = month_rem
if year_t > 1:
    y = "years"
elif year_t <= 1:
    y = "year"
else:
    year_t = year_t
print()

"""output"""

print(f"Total hours you spend in the world: {hrs_t} {hrt}\nTotal number of days you spend in the world: {days_t} {dt}\nTotal number of weeks you spend in the world {wk_t} {wkt} {rem_d} {d}\nTotal number of months you spend in the world: {month_t} {mt} {rem_d} {d}\nYou're {year_t} {y} old.\nYou lived {year_t} {y} {month_rem} {m} {rem_d} {d}")


