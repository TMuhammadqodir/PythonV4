try:
    with open('cinema.txt','r') as file:
        temp=file.readlines()
        for i in temp:
            i=i.split(',')
            if int(i[3])>2000 and ('Comedy' in i[2].split('|') or 'Drama' in i[2].split('|') or 'Romance' in i[2].split('|')):
                print(i[1],i[4])
except FileNotFoundError: print('Bunday file mavjud emas')