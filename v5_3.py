try:
    with open('booking_data.txt','r') as file:
        temp=file.read()
        temp=temp.split('\n')[:-1]
        for i in temp:
            i=i.split(',')
            if i[3]=='US' and int(i[4][:-3])<=20:
                print(*i)
except: print('Bunday file mavjud emas')