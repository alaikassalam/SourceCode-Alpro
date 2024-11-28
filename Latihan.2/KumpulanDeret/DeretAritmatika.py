a = int(input('masukkan suku awal : '))
b = int(input('masukkan pembeda : '))
n = int(input('masukan banyaknya bilangan : '))

c = ''
total = 0

for i in range(n):
    hitung = a + i * b
    c = c + str(hitung) + ' '
    total = total + hitung 

print('deret aritmatika',c)
print('total : ',total)