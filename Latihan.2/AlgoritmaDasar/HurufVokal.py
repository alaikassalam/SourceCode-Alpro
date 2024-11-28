# # 1
# vokal = 0
# for i in x:
#   if(i=='a' or i=='i' or i=='u' or i=='e' or i=='o' or
#      i=='A' or i=='I' or i=='U' or i=='E' or i=='O'):
#     vokal = vokal + 1
 
# # Tampilkan total huruf vokal jika ditemukan
# if vokal > 0 :
#   print('Jumlah huruf vokal =', vokal)
# else:
#   print('Huruf vokal tidak ditemukan')

# 2
kata = input('masukkan kata : ')
urut = 1
vokal = 'aiueoAIUEO'
for i in kata:
    if i in vokal:
        print(f'huruf ke-',urut,':','merupakan huruf vokal',i)
    else:
        print(f'huruf ke-',urut,':','merupakan huruf konsonan',i)
    urut += 1