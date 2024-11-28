print('## pola piramid ##')
t = int(input('input tinggi piramid :'))
for i in range(t):
    print(' ' * (t - i),end='')
    print('* ' * (i+1))
print('## pola piramid terbalik ##')
w = int(input('input tinggi piramid terbalik :'))
for i in range(w):
    print(' ' * (i+1),end='')
    print('* ' * (w-i))

