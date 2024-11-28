n = int(input('input nilai n : '))
a = 0
h = 0
for i in range(1,n+1):
    if i%2==1 :
        a = 2+i
        h = h+a
    else :
        a = 2*i
        h = h+a
y = 4+h 
print(y)

