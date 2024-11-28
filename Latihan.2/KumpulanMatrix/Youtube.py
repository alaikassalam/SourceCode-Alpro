

# # penjumlahan 2 Matrix
# x = [
#     [1,2,3],
#     [2,3,4],
#     [3,4,5]
# ]

# y = [
#     [1,2,3],
#     [2,3,4],
#     [3,4,5]
# ]

# result = [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j] + y[i][j]
# for r in result:
#     print(r)

# # masukkan matrix ke matrix kosong 
# y = [
#     [1,2,3],
#     [2,3,4],
#     [3,4,5]
# ]

# result = [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]
# for i in range(len(y)):
#     for j in range(len(y[0])):
#         result[i][j] = y[i][j]
# for r in result:
#     print(r)

# multiply two matrix 
x = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

y = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
for r in result:
    print(r)
    
