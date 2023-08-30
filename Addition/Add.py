out = open('output.txt','w')
with open('input.txt','r') as file:

    for val in file:
        list = []

        if int(val) <= 2: out.write(0)

        else:
            nums = [i for i in range(2,int(val)//2)]
            addfix = -1

            while addfix < int(val)//2:
                addloose = 0

                while addloose < int(val)//2:
                    addfix +=1
                    addloose += nums[addfix]
                if addloose == int(val):
                    list.append([i for i in range(addfix,addloose+1)])
            s = ''
            for items in list:
                s += items[0]
                for item in items[1:-1]:
                    s += '+' + str(item)
                s += '\n'
out.write(s)