satu = int(input('Masukkan bilangan pertama = '))
dua = int(input('Masukkan bilangan pertama = '))
num = 1
terbesar = 0


for i in range(1,satu):
  if satu % i == 0 and dua % i == 0:
    if terbesar < i :
      terbesar = i
      print(f'Pembagi yang sama - {num} = {i}')
      num+=1
print(f'Pembagi yang sama besar adalah = {terbesar}')