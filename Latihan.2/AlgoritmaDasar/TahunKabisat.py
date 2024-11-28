year = int(input('Input tahun: '))
 
if (year % 400) == 0:
  print(year,'adalah tahun kabisat')
elif (year % 100) == 0:
  print(year,'bukan tahun kabisat')
elif (year % 4) == 0:
  print(year,'adalah tahun kabisat')
else:
  print(year,'bukan tahun kabisat')