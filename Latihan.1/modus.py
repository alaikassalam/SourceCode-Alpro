def buat(l1):
  hasil = []
  for i in range(jumlah):
    inp = int(input('input angka : '))
    hasil.append(inp)
  return hasil

jumlah = int(input('input jumlah list :'))
data = buat(jumlah)
print(data)

for i in range(len(data)):
    for j in range(0,len(data)-i-1):
        if data[j]>data[j+1]:
            temp=data[j]
            data[j]=data[j+1]
            data[j+1] = temp

print(data)   
print(data.count(4))

