def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter a year: "))
print(is_leap_year(year))

if is_leap_year(year):
    print(f"{year} is a LEAP YEAR")
else:
    print(f"{year} is not a LEAP YEAR")

