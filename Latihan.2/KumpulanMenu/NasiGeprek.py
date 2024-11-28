
stop = False
while not(stop):
    print('Menu Ayam Geprek Mufid')
    print('paket ayam geprek :')
    print('1. Ayam Geprek B.ajah : RP.10000')
    print('2. Ayam Geprek M.ajah : RP.12000')
    print('3. Ayam Geprek S.ajah : RP.14000')

    pilih = input('input pilihan anda : ')
    harga = 0
    kembalian = 0
    if pilih =='1':
        harga = 10000
        jumlahpesenan = int(input('masukkan jumlah pesenan : '))
        hargasemua = harga * jumlahpesenan
        print('total harga :Rp.', hargasemua)
        
        inp = int(input('input uang anda :Rp.'))
        if inp ==hargasemua:
            kembalian = inp - hargasemua
            print('uang anda pas :Rp.', kembalian)
                    
        elif inp >hargasemua:
            kembalian = inp - hargasemua
            print('uang kembalian anda :Rp.', kembalian)
                    
        else:
            kembalian = inp - hargasemua
            print('uang anda kurang :Rp.', kembalian)
            print('=================================================')
    

            
    elif pilih =='2':
        print('anda memilih Ayam Geprek M.ajah')
        harga = 12000
        jumlahpesenan = int(input('masukkan jumlah pesanan : '))
        hargasemua = harga * jumlahpesenan
        print('total harga :Rp.', hargasemua)
        
        inp = int(input('input uang anda : '))
        if inp ==12000:
            kembalian = inp - hargasemua
            print('uang anda pas :Rp.', kembalian)
        elif inp >12000:
            kembalian = inp  - hargasemua
            print('uang kembalian anda :Rp.', kembalian)
        else: 
            kembalian = inp - hargasemua
            print('uang anda kurang :Rp.', kembalian)
            print('=================================================')

    elif pilih =='3':
        print('anda memilih Ayam Geprek S.ajah')
        harga = 14000
        jumlahpesenan = int(input('masukkan jumlah pesanan : '))
        hargasemua = harga * jumlahpesenan
        print('harga total : ', hargasemua)
        
        inp = int(input('input uang anda : '))
        if inp ==14000:
            kembalian = inp - hargasemua
            print('uang anda pas :Rp.', kembalian)
        elif inp >14000:
            kembalian = inp  - hargasemua
            print('uang kembalian anda :Rp.', kembalian)
        else: 
            kembalian = inp - hargasemua
            print('uang anda kurang :Rp.', kembalian)
            print('=================================================')


            
    inp = input('Apakah anda ingin mengoprasikannya lagi (y/t) : ')
    if inp == 'y':
        stop = False
    elif inp=='t':
        stop = True
    else:
        stop = True

    