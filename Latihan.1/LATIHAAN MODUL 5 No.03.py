angka = int(input('masukkan angka : '))
n = 1
temp1 = 100000

while n<=6:
    temp2 = angka // temp1
    temp2 = temp2 % 10
    spasi = str(n)+' ' + ':' + ' ' +str(temp2)+ ' ' + 'x' + ' ' + str(temp1)
    print(spasi)
    n+=1
    temp1 = temp1 // 10