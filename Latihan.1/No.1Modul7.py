string = input('masukkan string : ')
karakter = input('masukkan karakter : ')
temp = 0 # untuk menyimpan nilai karakter 

for i in range(len(string)):
    if string[i] == karakter:
        temp += 1 # jika kondisi terpenuhi ditambah 1 
print(f"Jumlah karakter '{karakter}' dalam string '{string}': {temp}")