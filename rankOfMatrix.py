def rank_of_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    rank = 0
    
    for i in range(min(rows, cols)):
        
        if matrix[i][i] != 0:
            rank += 1
            for j in range(rows):
                if j != i:
                    ratio = matrix[j][i] / matrix[i][i]
                    for k in range(cols):
                        matrix[j][k] -= ratio * matrix[i][k]
    
    return rank

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("Rank of the matrix:", rank_of_matrix(matrix))
