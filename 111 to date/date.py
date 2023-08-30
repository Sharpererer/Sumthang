day = int(input('Enter days: '))
year = 1


while day - 365 > 0 or day - 366 > 0:
    if year == 1:
        day -= 364
    elif year % 100 == 0:
        day -= 366 if year % 400 == 0 else 365
    else:
        day -= 366 if year % 4 == 0 else 365
    year += 1

months = [31,29,31,30,31,30,31,31,30,31,30,31] if year % 4 == 0 else [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(0,12):
    day -= months[i]
    if day < 1:
        day += months[i]
        break

month = i + 1

print(day,month,year)