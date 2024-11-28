
# # akses element matrix
# matrix = [
#     [5, 0],
#     [2, 6],
# ]

# for x in range(0, len(matrix)):
#     for y in range(0, len(matrix[0])):
#         print (matrix[x][y], end=' ')
#     print()

# # penjumlahan matrix
# mat1 = [
#     [5, 0],
#     [2, 6],
# ]
# mat2 = [
# [1, 0],
# [4, 2],
# ]
# for x in range(0, len(mat1)):
#     for y in range(0, len(mat1[0])):
#         print (mat1[x][y] + mat2[x][y], end=' ')
#     print()

# # perkalian matrix
# mat1 = [
#     [5, 0],
#     [2, 6],
# ]

# mat2 = [
#     [1, 0],
#     [4, 2],
# ]

# mat3 = []

# for x in range(0, len(mat1)):
#     row = []
#     for y in range(0, len(mat1[0])):
#         total = 0
#         for z in range(0, len(mat1)):
#             total = total + (mat1[x][z] * mat2[z][y])
#         row.append(total)
#     mat3.append(row)


# for x in range(0, len(mat3)):
#     for y in range(0, len(mat3[0])):
#         print (mat3[x][y], end=' ')
#     print ()

#Nama : Mozaik Al Qharomi

def Mult(a,b):
    #perkalian matriks C = A.B
    A = a
    B = b
    
    n = 2
    W = X = Y = Z = 0
    k = 0

    for i in range(n):
        for j in range(n):
            if i == 0:
                W = W + A[i][j]*B[j][i]
            else:
                Z = Z + A[i][j]*B[j][i]
            
            if k == 0:
                X = X + A[i][j]*B[i][j+1]
                Y = Y + A[i+1][j]*B[i][j]
                k=k+1
            
            if i==j & i > 0:
                X = X + A[i-1][j]*B[i][j]
                Y = Y + A[i][j]*B[i][j-1]
    Matrix2D = ([W, X], [Y, Z])
    return Matrix2D

def add(a,b):
    A = a
    B = b
    
    Add_Matriks = ([0,0], [0,0])
    
    for i in range(len(A)):
        for j in range(len(A)):
            Add_Matriks[i][j] = A[i][j] + B[i][j]
    
    return Add_Matriks


  
