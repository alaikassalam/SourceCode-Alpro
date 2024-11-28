kata = input('masukkan kata : ')
genap = []
ganjil = []

for i in range(len(kata)):
    if i%2==0:
        genap.append(kata[i])
    else:
        ganjil.append(kata[i])
print('index genap : ',genap)
print('index ganjil : ',ganjil)
        