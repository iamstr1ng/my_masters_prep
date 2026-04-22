#checks leap year
#rules : Should be cleanly divisible by 4
#rules : if divisible by 100, and also divisible by 400 then leap year
def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:  #and takes precedence and then or
        return True
    else:
        return False