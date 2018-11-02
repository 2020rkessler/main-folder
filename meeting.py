import random

matrix = [[random.randint(0,100) for col in range(5)] for row in range(5)]
print(matrix)
def col_sum(matrix,num):
    sum = 0
    for row in range (len(matrix)):
        for col in range (len(matrix)):
            if col == num:
                sum = sum + matrix[row][col]
    print(sum)

# call the function

col_sum(matrix, 3)
