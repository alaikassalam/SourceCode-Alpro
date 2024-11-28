angka = int(input('masukkan angka : '))

ratusanRibu = angka // 100000
puluhanRibu = (angka % 100000) // 10000
ribuan = ((angka % 100000) % 10000) // 1000
ratusan = (((angka % 100000) % 10000) % 1000) //100
puluhan = ((((angka % 100000) % 10000) % 1000) % 100) //10
satuan = angka % 10 

print(f'1 : {ratusanRibu} x 100000')
print(f'2 : {puluhanRibu} x 10000')
print(f'3 : {ribuan} x 1000')
print(f'4 : {ratusan} x 100')
print(f'5 : {puluhan} x 10')
print(f'6 : {satuan} x 1')