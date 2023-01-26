try:
    with open('car_model.txt','r') as file:
        temp=file.read()
        s1,s2=0,0
        temp=temp.split('\n')[1:-1]
        for i in temp:
            i=i.split(',')
            if s1<str(temp).count(i[4]):
                s1=str(temp).count(i[4])
                temp2=i[4]
        print(f'eng ko\'p mashina {s1} ta {temp2} brendiga tegishli')
        temp2=list(filter(lambda a: a.split(',')[4]==temp2,temp))
        s3=str(temp2).count(temp2[0].split(',')[-1])
        for i in temp2:
            i=i.split(',')
            if s2<str(temp2).count(i[-1]):
                s2=str(temp2).count(i[-1])
                temp3=i[-1]
            if s3>str(temp2).count(i[-1]):
                s3=str(temp2).count(i[-1])
                temp4=i[-1]
        print(f'eng ko\'pi {temp3} davlatida {s2} ta')
        print(f'eng kami {temp4} davlatida {s3} ta')

except: print('not found file')