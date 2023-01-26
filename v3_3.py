try:
    file=open('product_material.txt','r')
    temp=file.read()
except FileNotFoundError:
    print('Bunday file mavjud emas')
else:
    temp=temp.split('\n')[:-1]
    for i in temp:
        i=i.split(',')
        if i[-1]=='false' and float(i[3][1:])<1e3:
            print(i[2])