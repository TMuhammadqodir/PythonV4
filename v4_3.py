try:
    with open('cinema.txt','r') as file:
        temp=file.readlines()
        for i in temp:
            i=i.split(',')
            if int(i[-1][:-4])>17 and 'Horror' in i[2].split('|') and len(i[2].split('|'))==1:
                print(*i)

except FileNotFoundError: print('BUnday file mavjud emas')