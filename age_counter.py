print("Age counter")
print()
day_e = 18
month_e = 6
year_e = 2020
print("Current date is",day_e,end="")
print(" /",month_e,end="")
print(" /",end="")
print("",year_e)
print("Enter date of birth")
day_s = int(input("Day="))
month_s = int(input("Month="))
year_s = int(input("Year="))
year_l = int((year_e - year_s) / 4)
days_t = (year_e - year_s) * 365 + (month_e - month_s) * 30 + (day_e - day_s)
days_t = days_t + year_l
hrs_t = days_t * 24
hrs_t = int(hrs_t)
seconds_t = int(hrs_t * 60 * 60)
minutes_t = in(hrs_t * 60)
wk_t = int(days_t / 7)
month_t = int(days_t / 30.8)
year_t = int(days_t / 365)
print()
print("Your date of birth is",day_s,"/",month_s,"/",year_s)
print("Total seconds you spend in the world =",seconds_t,"s")
print("Total seconds you spend in the world =",minutes_t,"mins")
print("Total hours you spend in the world =",hrs_t,end="")
print("hrs")
print("Total number of days you spend in the world =",days_t,end="")
print("days")
print("Total number of weeks you spend in the world =",wk_t,end="")
print("wks")
print("Total number of months you spend in the world =",month_t,end="")
print("mnths")
print("You're",year_t,"years old")
print("You spend",year_t,end="")
print("yrs in the world")
print()