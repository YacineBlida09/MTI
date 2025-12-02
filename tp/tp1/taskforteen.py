matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(matrix)

#Access and print the element at row 0, column 1 (should be 2).
print(matrix[0][1])

#Access and print the element at row 2, column 2 (should be 9).
print(matrix[2][2])

#Iterate through matrix and print each element row by row.
for row in matrix:
    for col in row:
        print(col, end = '|')
    print("\n------")
