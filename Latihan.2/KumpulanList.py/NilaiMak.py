data = [90,56,34,78,86,90,87,88,75,65,86,57,89,67,80]
maksimum=34
minimum = 90

for i in range(len(data)):
    if data[i]>maksimum:
        maksimum=data[i]
    elif data[i]<minimum:
        minimum=data[i]  
print(maksimum)
print(minimum) 

print('data = [90,56,34,78,86,90,87,88,75,65,86,57,89,67,80]')
maksimal = max(data)
minimal = min(data)
print('nilai maksimal : ',maksimal)
print('nilai minimal : ',minimal)