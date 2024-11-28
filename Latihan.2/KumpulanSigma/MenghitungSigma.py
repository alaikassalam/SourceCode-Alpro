n = int(input('masukkan nilai : '))
a = 0
for i in range(1,n+1):
    if i%2==0:
        a += 2*i
    else:
        a += 2+i
y = a + 4
print(y)
