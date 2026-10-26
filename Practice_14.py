day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if year < 1 or year > 10000:
    print("Invalid date")
elif month < 1 or month > 12:
    print("Invalid date")
else:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days = 29
        else:
            days = 28
    elif month in [4, 6, 9, 11]:
        days = 30
    else:
        days = 31

    if day >= 1 and day <= days:
        print("Valid date")
    else:
        print("Invalid date")