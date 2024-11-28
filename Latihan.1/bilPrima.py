bil = int(input('masukkan bilangan : '))

a = 0 

for i in range(1,bil+1):
    if bil % i ==0:
        a += 1

if a == 2:
    print(bil,'adalah bilangan prima')
else:
    print(bil,'bukan bilangan prima, memiliki faktor pembagi',a)





