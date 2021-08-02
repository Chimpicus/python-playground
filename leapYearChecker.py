def isLeap(year):
    if year%100 == 0:
        if year%400 == 0:
            print(year, "is a leap year")

        else:
            print(year, 'is not a leap year')
            

isLeap(1700)
isLeap(2000)