print('## segitiga ##')
# menggunakan 1 for
a = int(input('Input tinggi segitiga: '))
for i in range(a+1):
  print(' *' * i)
# menggunakan 2 for 
b = int(input('input tinggi segitiga :'))
for i in range(b):
    for j in range(i+1):
        print(' *',end='')
    print()
print()
print('## segitiga terbalik ##')
# menggunakan 1 for 
c = int(input('input tinggi segitiga terbalik :'))
for i in range(c):
    print(' *' * (c - i))
# menggunkan 2 for 
d = int(input('input tinggi segitiga terbalik :'))
for i in range(d):
    for j in range(d - i):
        print(' *',end='')
    print()