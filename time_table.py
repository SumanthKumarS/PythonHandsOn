import Dates as dt
y = int(input("Enter year as 4 digits (e.g: 2002):\n"))
mon = int(input("Enter month number:\n"))
year_o = dt.is_leap(y)
if(year_o == True):
    print("Year: Leap Year")
else:
    print("Year: Not Leap Year")
print("Month Name: ",dt.month_name(mon))
print("Days in month: ",dt.day_month(mon,y))


