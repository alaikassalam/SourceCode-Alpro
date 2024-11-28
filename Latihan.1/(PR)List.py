
stop = False
while not(stop):
    print('Menu :')
    print('1.Nilai Total dan Rata-Rata')
    print('2.Nilai Maksimal & minimal')
    print('3.Nilai Index dari Threshold')

    inp = input('input pilihan anda : ')
    data = [90,56,34,78,86,90,87,88,75,65,86,57,89,67,80]
    
    if inp =='1':
        print('data = [90,56,34,78,86,90,87,88,75,65,86,57,89,67,80]')
        total = 0
        for nilai in data:
            total = total + nilai
        ratarata = total/len(data)
        print('rata-rata : ',ratarata)

    elif inp =='2':
        print('data = [90,56,34,78,86,90,87,88,75,65,86,57,89,67,80]')
        maksimum=34
        minimum = 90
        for i in range(len(data)):
            if data[i]>maksimum:
                maksimum=data[i]
            elif data[i]<minimum:
                minimum=data[i]  
        print('Nilai maksimal : ',maksimum)
        print('Nilai minimal : ',minimum) 

    elif inp =='3':
        print('data = [90,56,34,78,86,90,87,88,75,65,86,57,89,67,80]')
        Threshold = int(input('input nilai threshold : '))
        index = [] 
        for i in range(len(data)):
            if data [i] > Threshold:
                index.append(i)
        print('index diatas nilai threshold : ',index)

    else:
        print()
        print('>>> input anda ga valid !!!!!!!!!!!!!')
        print()
    
    inp = input('Apakah anda ingin mengoprasikannya lagi (y/t) : ')
    if inp =='t':
        stop = True
