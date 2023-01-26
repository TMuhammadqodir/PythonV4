try:
    file=open('languages.txt','r')
    temp=file.read()
except:
    print('not found file')
else:
    temp=temp.split('\n')[:-1]
    for i in temp:
        i=i.split(',')
        if int(i[1])>1e6:
            print(*i)