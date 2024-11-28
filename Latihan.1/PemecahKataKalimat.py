

kalimat = input('Masukkan kalimat: ')
jumlah = 0

for karakter in kalimat:
    jumlah += 1

print("Jumlah karakter:", jumlah)


# kata
kalimat = input('Masukkan kalimat: ')
jumlah = len(kalimat.split()) #  Memecah kalimat menjadi kata-kata menggunakan metode split(),

print("Jumlah kata:", jumlah)

