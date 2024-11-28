n = int(input('masukkan nilai : '))

for i in range(n+1):
    spasi = ''
    for j in range(n+1):
        if i==j:
            spasi += 'x' + ' '
        elif i+j==n:
            spasi += 'x' + ' '
        else:
            spasi += str(j)+ ' '
    print(spasi)