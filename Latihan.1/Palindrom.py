stop = False
while not(stop):
    kata = input('masukkan kata : ')
    benar = 0 
    temp = 0

    for i in range(len(kata)-1,-1,-1):
        if kata[temp] == kata[i]:
            print(f'{kata[temp]} sama dengan {kata[i]}')
            benar += 1
        else:
            print(f'{kata[temp]} tidak sama dengan {kata[i]}')
        temp += 1
    if benar == len(kata):
        print('palindrome')
    else:
        print('bukan palindrome')

    inp = input('mau ngulang y/t ? ')
    if inp =='t':
        stop = True


# s = input('masukkan kata : ')
# s1 = reversed(s)
# if list(s) == list(s1):
#     print('palindrome')
# else:
#     print('not palindrome')