try:
    file=open('product_material.txt','r')
    temp=file.read()
except FileNotFoundError:
    print('Bunday file mavjud emas')
else:
    temp=temp.split('\n')[:-1]
    lis,dic=list(),dict()
    material=input('material nomini kiriting: ')
    for i in temp:
        i=i.split(',')
        if i[2]==material and i[-1]=='true': lis.append(float(i[3][1:]))
    lis.sort()
    lis=list(map(lambda a: '$'+str(a),lis))
    print(lis)

        