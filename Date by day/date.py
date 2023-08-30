year = int(input('Year: '))
day = int(input('Day: '))
months = [31,28,31,30,31,30,31,31,30,31,30,31] if year%4 != 0 else [31,29,31,30,31,30,31,31,30,31,30,31]

if (year < 0) or (day < 0) or (day > 366) or (day == 366 and year%4 != 0): print('Invalid input')
else:
    for month in range(0,12):
        day -= months[month]
        if day <= 0:
            day += months[month]
            break

    print(str(day) + '/' + str(month + 1) + '/' + str(year))