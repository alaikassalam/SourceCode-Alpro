string = input('masukkan string : ')
karakter = input('masukkan karakter : ')
jumlah = 0 
index = [] # untuk menyimpan index karakter dalam string 

for i in range(len(string)):
    if string[i] == karakter:
        index.append(i)
        jumlah += 1
print(f"Indeks karakter '{karakter}' pada string: {index}")
print(f"Jumlah karakter '{karakter}' pada string: {jumlah}")
