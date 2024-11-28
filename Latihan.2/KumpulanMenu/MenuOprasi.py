
stop = False

while not(stop):

    print('Menu')
    print('Tekan 1. Untuk operasi perhitungan luas lingkaran (input adalah jari-jari)')
    print('Tekan 2. Untuk operasi perhitungan luas persegi panjang (input adalah panjang dan lebar)')
    print('Tekan 3. Untuk operasi perhitungan luas segitiga (input adalah alas dan tinggi )')
    pilih = input('masukkan pilihan anda : ')
    
    if pilih == '1':
        jari = int(input('masukkan jari-jari : '))
        luas = 22/7*jari**2
        print('Luas lingkaran : ',luas)

    elif pilih == '2':
        panjang = int(input('masukkan panjang : '))
        lebar = int(input('masukkan lebar : '))
        luas = panjang * lebar
        print('Luas persegi panjang : ',luas)

    elif pilih == '3':
        alas = int(input('masukkan alas : '))
        tinggi = int(input('masukkan tinggi : '))
        luas = 1/2 * alas * tinggi 
        print('Luas segitiga : ',luas)

    inp = input('Apakah anda ingin mengoprasikannya lagi : ')
    if inp == 'y':
        stop = False
    else :
        stop = True

                