day = int(input('Enter day: '))
month = int(input('Enter month: '))
year = int(input('Enter year: '))

error = 0

def rank(val):
    s = str(val)
    if s[-1] == '1': s += 'st'
    elif s[-1] == '2': s += 'nd'
    elif s[-1] == '3': s += 'rd'
    else: s += 'th'
    return s

if day > 31 or day < 1:
    print('Invalid "day" input')
    error += 1
if month > 12 or month < 1:
    print('Invalid "month" input')
    error += 1
if year < 0:
    print('Invalid "year" input')
    error += 1

if error > 0:
    pass
else:
    if (month == 2 and day > 29) or (month == 2 and day == 29 and year%4 != 0) or (month in [1,3,5,7,8,10,12] and day > 31) or (month in [2,4,6,9,11] and day > 30):
        print('Day exceeds a specific month')

    else:

        add_1 = 0
        for months in range(1,month):
            if months in [1,3,5,7,8,10,12]: add_1 += 31
            elif months in [4,6,9,11]: add_1 += 30
            elif months == 2: add_1 += 29 if year % 4 == 0 else 28
        add_1 += day

    years = ((year - 1)//4)*1461 + 
        
print(str(day) + '/' + str(month) + '/' + str(year), end=' ')
print('(Leap year)' if year%4 == 0 else '(Normal year)')
print('The ' + rank(add_1) + ' day of the year.')
print('The ' + rank(years) + ' day counting from 1/1/1.')