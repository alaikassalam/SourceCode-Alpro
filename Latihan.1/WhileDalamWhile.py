a = False
while not(a):

    stop = False 
    while not(stop):
        inp = input('mau lanjut y/t : ')
        if inp =='y':
            stop = False
        elif inp =='t':
            stop = True
        else :
            print('inputan anda ga valid')
            stop = True
    m = input('apakah anda mau mengulang y/t : ')
    if m =='y':
        a = False
    else:
        a = True

