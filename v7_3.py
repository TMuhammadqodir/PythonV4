try:
    file=open('car_model.txt','r')
    temp=file.read()
except FileNotFoundError: print('Bunday fayl mavjud emas')
else:
    def func(fil:file):
        for i in fil:
            i=i.split(',')
            if int(i[5])<2005:
                print('Kimdan:Auto Test Corp')
                print(f'Kimdan:{i[1]} {i[2]}')
                print(f'Joriy davlat:{i[-1]}')
                print(f'''Hurmatli {i[1]} {i[2]}! {i[4]} tomonidan 
ishlab chiqarilgan {i[5]} da ishlab chiqarilgan {i[-2]}
rangli avtoulovingiz Texnik Holatini tekshirtirish
maqsadida mahalliy Auto Test Corp ofisiga murojaat
qilishingizni so\'raymiz!
''')

    temp=temp.split('\n')[1:-1]
    func(temp)
    file.close()