try:
    file=open('people_count.txt','r')
    temp=file.read()
except:
    print('Bunday fayl mavjud emas')
else:
    temp=temp.split('\n')[:-1]
    for i in temp:
        i=i.split(',')
        if i[2]=='Male':
            print(i[0],i[1],i[-1])
