try:
    file=open('booking_data.txt','r')
    temp=file.read()
except FileNotFoundError: print('Bunday file mavjud emas')
else:
    temp=temp.split('\n')[:-1]
    yonalishi=input('yonalishni kiriting: ')
    for i in temp:
        i=i.split(',')
        if i[3]==yonalishi and int(i[2][:-3])>12 and 21<int(i[4][:-3]):
            print(i)
    file.close()
