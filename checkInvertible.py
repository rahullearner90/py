import numpy as np
#pip install numpy

def enter_matrix(matrix_name):
    try:
        rows = int(input(f"Enter the number of rows for {matrix_name}: "))
        cols = int(input(f"Enter the number of columns for {matrix_name}: "))
        
        if rows < 1 or cols < 1:
            raise ValueError("Rows and columns must be positive integers.")
        
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                element = float(input(f"Enter the element at position ({i+1}, {j+1}): "))
                row.append(element)
            matrix.append(row)
        
        return matrix
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

def print_matrix(matrix):
    for row in matrix:
        print(row)

def is_invertible(matrix):
    try:
        inverse = np.linalg.inv(matrix)
        return True
    except np.linalg.LinAlgError:
        return False

def find_inverse(matrix):
    return np.linalg.inv(matrix)

# Example usage:
matrix_a = enter_matrix("Matrix A")

if matrix_a is not None:
    print("\nMatrix A:")
    print_matrix(matrix_a)
    
    if is_invertible(matrix_a):
        inverse_matrix = find_inverse(matrix_a)
        print("\nThe matrix is invertible.")
        print("\nInverse of Matrix A:")
        print_matrix(inverse_matrix)
    else:
        print("\nThe matrix is not invertible.") #2,2,1,-1,2,2
        
