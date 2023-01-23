def is_leap(year):
    # First step : if year is divisble by 4 pass to second step else pass to Fifth step 
    if year % 4 != 0:
        return False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
    return False
        
print(is_leap(1992))