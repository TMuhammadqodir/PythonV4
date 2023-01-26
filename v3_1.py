try:
    file=open('product_material.txt','r')
    temp=file.read()
except FileNotFoundError:
    print('Bunday file mavjud emas')
else:
    temp=temp.split('\n')[:-1]
    for i in temp:
        i=i.split(',')
        if 500<float(i[3][1:])<1000:
            print(i[0],i[2])