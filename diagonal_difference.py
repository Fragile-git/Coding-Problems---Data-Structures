"""
Diagonal Difference: 

You are given a square matrix of integers. Your task is to find the 
absolute difference between the sums of its diagonals.
Consider a square matrix, arr, of size n x n, where n is the number of rows 
(and columns) in the matrix. 

The primary diagonal is the set of elements where the row index is equal to the column index (i.e., arr[i][i]). 
The secondary diagonal is the set of elements where the row index plus the column index is equal to n - 1 (i.e., arr[i][n - 1 - i]).

Your goal is to calculate the absolute difference between the sums of the primary diagonal and the secondary diagonal. 
Specifically, find: |sum(primary diagonal) - sum(secondary diagonal)| 

For example, given the matrix:

1 2 3
4 5 6 
9 8 9
The primary diagonal sums to 1 + 5 + 9 = 15, 
and the secondary diagonal 
sums to 3 + 5 + 9 = 17. Therefore, the absolute difference is 15 - 17 = 2
"""

size = int(input('Enter the size of the square matrix: '))
print('Enter the elements of the square matrix: ')
matrix = [] # declare a list it can become a 1st dimensional 2nd dimension 

for i in range(size):
    # inputs becomes a list an iterated to become an int
    row = [int(x) for x in input().split()] 
    matrix.append(row)

print(matrix)

primary_d = sum(matrix[i][i] for i in range(size)) # row index is equal to the column index
secondary_d = sum(matrix[i][size -1 - i] for i in range(size)) 
# size -1 (with respect top indexing) - i decreasing as you go down the diagonal


print(f'Absolute diagonal difference: {abs(primary_d-secondary_d)}') #absolute value 



