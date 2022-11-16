import calendar
def is_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def month_name(no):
    res = calendar.month_name[no]
    return res
def day_month(m,y):
    leap = 0
    if y%400 == 0:
        leap = 1
    elif y%100 == 0:
        leap = 1
    elif y%4 == 0:
        leap = 1
    if m == 2:
        return 28 + leap
    lst = [1,3,5,7,8,10,12]
    if m in lst:
        return 31
    return 30
