day = int(input('Enter day: '))
month = int(input('Enter month: '))
year = int(input('Enter year: '))
add = 0

months = [31,28,31,30,31,30,31,31,30,31,30,31] 
if year % 4 == 0 and not year % 400 == 0:
    months[1] = 29

for i in range(0,12):
    if i + 1 < month: 
        add += months[i]
    else : break
print(add + day)