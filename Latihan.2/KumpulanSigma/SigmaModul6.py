n = int(input('masukkan nilai n : '))
m = int(input('masukkan nilai m : '))
y = 0 

for i in range(0,m):
    for j in range(0,n):
        y += i*4 + j*2
print('nilai y : ', y)