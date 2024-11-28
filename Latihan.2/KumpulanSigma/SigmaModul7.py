x=[10,10,5,10,10]
print(f'x = {x}')
temp=0
fx=0
for i in range(1,len(x)+1):
    temp+=x[i-1]
xbar=temp/len(x)
for j in range(1,len(x)+1):
    fx+=x[j-1]-xbar
print(f'xbar = {xbar}')
print(f'fx = {fx}')
