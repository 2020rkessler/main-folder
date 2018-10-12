A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
f = 1
for i in range(0, 3):
    f *= 10
    for j in range(0, 3):
       A[i][j] *= f
print(A)
