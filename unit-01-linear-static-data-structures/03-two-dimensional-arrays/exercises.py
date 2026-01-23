from two_dimensional_array import Matrix

def exercise_1_create_and_fill():
    """
    Exercise 1: Basic Initialization
    
    Objective:
    Create a 4x4 Matrix initialized with 0. Manually set the four 
    corners to value 1 and print the result.
    
    Logic:
    Instantiate a Matrix object with dimensions 4x4. Use the 
    `matrix[i, j]` syntax to update positions (0,0), (0,3), 
    (3,0), and (3,3).
    """
    # TODO: Implement logic
    pass

def exercise_2_fill_diagonal_pattern():
    """
    Exercise 2: Fill Main Diagonal
    
    Objective:
    Create a 5x5 Matrix and fill the MAIN DIAGONAL (where i == j) 
    with the value 9.
    
    Logic:
    Use a single `for` loop from 0 to 4. In each iteration `i`, 
    update the element at position `(i, i)`. This is more efficient 
    than nested loops for diagonal operations.
    """
    # TODO: Implement logic
    pass

def exercise_3_sum_rows_and_cols(matrix: Matrix):
    """
    Exercise 3: Summation
    
    Objective:
    Calculate and print the sum of each separate row and each 
    separate column in a given matrix.
    
    Logic:
    Use nested loops. For row sums, fix the row index `i` and sum 
    all `j`. For column sums, fix the column index `j` and sum all `i`.
    """
    # TODO: Implement logic
    pass

def exercise_4_secondary_diagonal(matrix: Matrix):
    """
    Exercise 4: Secondary Diagonal
    
    Objective:
    Print the elements of the SECONDARY diagonal of a square matrix.
    
    Logic:
    Iterate through rows `i`. The corresponding column `j` for the 
    secondary diagonal is always `n - 1 - i`, where `n` is the 
    number of rows/cols.
    """
    # TODO: Implement logic
    pass

def exercise_5_check_identity_matrix(matrix: Matrix):
    """
    Exercise 5: Identity Matrix Validation
    
    Objective:
    Verify if the given matrix is an Identity Matrix.
    
    Logic:
    1. Check if it's square (rows == cols).
    2. Traverse all elements: if `i == j`, the value must be 1; 
       if `i != j`, the value must be 0. Return False if any 
       condition fails.
    """
    # TODO: Implement logic
    pass

def exercise_6_transpose_matrix(matrix: Matrix):
    """
    Exercise 6: Matrix Transposition
    
    Objective:
    Create and return a NEW Matrix that is the transpose of the input.
    
    Logic:
    Create a new Matrix with swapped dimensions (MxN). Iterate 
    through the original matrix and assign `new_matrix[j, i] = original[i, j]`.
    """
    # TODO: Implement logic
    pass

def exercise_7_check_symmetric(matrix: Matrix):
    """
    Exercise 7: Symmetric Matrix Check
    
    Objective:
    Check if a matrix is Symmetric (Matrix equals its Transpose).
    
    Logic:
    First, ensure the matrix is square. Then, iterate through the 
    upper triangle (`j > i`) and compare `matrix[i, j]` with 
    `matrix[j, i]`. If they differ, it's not symmetric.
    """
    # TODO: Implement logic
    pass

def exercise_8_identify_triangular_type(matrix: Matrix):
    """
    Exercise 8: Triangular Matrix Identification
    
    Objective:
    Determine if the matrix is 'Upper Triangular', 'Lower Triangular', 
    or 'Neither'.
    
    Logic:
    - Upper: All elements where `i > j` must be 0.
    - Lower: All elements where `i < j` must be 0.
    Traverse the matrix and flag if any non-zero element violates these rules.
    """
    # TODO: Implement logic
    pass

def exercise_9_rotate_90_degrees(matrix: Matrix):
    """
    Exercise 9: Rotate Matrix 90 Degrees Clockwise
    
    Objective:
    Rotate the matrix elements 90 degrees to the right.
    
    Logic:
    A common 2-step approach: 
    1. Transpose the matrix (swap `i, j` with `j, i`).
    2. Reverse each row. 
    Alternatively, map positions directly: `new[j, n-1-i] = old[i, j]`.
    """
    # TODO: Implement logic
    pass

def exercise_10_spiral_traversal(matrix: Matrix):
    """
    Exercise 10: Spiral Order Traversal
    
    Objective:
    Print elements in spiral order starting from top-left (0,0) 
    going clockwise (Right -> Down -> Left -> Up).
    
    Logic:
    Maintain four boundaries: `top`, `bottom`, `left`, `right`. 
    Iterate while boundaries don't overlap, moving along the 
    edges and shrinking the boundaries after each direction is completed.
    """
    # TODO: Implement logic
    pass