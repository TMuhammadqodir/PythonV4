try:
    with open('cinema.txt','r') as file:
        temp=file.readlines()
        vaqt=int(input('1...24 >>> '))
        for i in temp:
            i=i.split(',')
            if int(i[-1][:-4])>vaqt:
                print(*i[-1])
except FileNotFoundError: print('Bunday file mavjud emas')
