matrix_a, matrix_b = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
 #Create a new result_matrix of the same dimensions, initialized with zeros.
rows = len(matrix_a)
cols = len(matrix_a[0])

result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

#Perform element-wise addition of matrix_a and matrix_b, storing the results in result_matrix.
for i in range(rows):
    for j in range(cols):
        result_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]

print(result_matrix)