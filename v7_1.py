try:
    file=open('car_model.txt','r')
    temp=file.read()
except FileNotFoundError: print("not found file")
else:
    def func(fil: file):
        male=len(list(filter(lambda a: a.split(',')[3]=='Male',fil)))
        female=len(list(filter(lambda a: a.split(',')[3]=='Female',fil)))
        total=male+female
        print('erkaklar {} ta\nayollar {} ta\numumiy {} ta'.format(male,female,total))
        maleprosent=male*100/total
        femaleprosent=female*100/total
        print(f'erkaklar {maleprosent}%')
        print(f'ayollar {femaleprosent}%')
        if maleprosent>femaleprosent:
            print(f'erkaklar ayollardan {100-female*100/male}% ga ko\'p')
        else:
            print(f'ayollar erkaklardan {100-male*100/female}% ga ko\'p')

    temp=temp.split('\n')[1:-1]
    func(temp)
    file.close()