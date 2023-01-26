try:
    file=open('booking_data.txt')
    temp=file.read()
except FileNotFoundError: print('Bunday file mavjud emas')
else:
    temp=temp.split('\n')[:-1]
    n=int(input('>>> '))
    for i in temp:
        i=i.split(',')
        if (n-50)<float(i[-1][1:])<(n+100):
            print(*i)
    file.close()
