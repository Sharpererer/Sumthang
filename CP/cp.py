
list = []
add = 2
num = int(input('Enter number here: '))
while add**2 <= num:
    list += [add**2]
    add += 1
print(list)