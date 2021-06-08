import numpy as np
import sys
import copy
import math
from numpy.random import RandomState
np.set_printoptions(suppress=True)
random_state = RandomState(1240)

# Round numbers according to significant digits
def my_round(d, x):
	return d - int(math.floor(math.log10(abs(x)))) - 1

print("Welcome to the Gaussian Elimination method for linear systems!")

# Reading the size of linear system
n = int(input('Enter the size of linear system: '))

# Reading precision required by user
d = int(input('Enter the precision value d: '))

# Making NumPy array of n x n+1 size
b = random_state.uniform(low=1, high=20, size=(n,n+1))

# Storing NumPy array according to user's precision
#a = np.array([[0.0004, 1.4020, 1.4060],[0.4003, -1.5020, 2.5010]])
#a = 10 * np.random.rand(n, n+1)

a = 10 * random_state.rand(n, n+1)
for i in range(n):
	for j in range(n+1):
		a[i][j] = np.around(a[i][j], decimals = my_round(d, a[i][j]))
print(a)

c = copy.deepcopy(a)
e = copy.deepcopy(a)

#print("\nRandomly generated augmented matrix is:")
#print(b)

print("\nAugmented matrix with precision set by the user:")
print(a)

def swap_rows(row_1, row_2):
	row_1 = row_1 - row_2
	row_2 = row_1 + row_2
	row_1 = row_2 - row_1
	return row_1, row_2

def partially_pivot(matrix):
	# Partially pivoting the input matrix

	# If a row except first row has larger value in first column
	# then swap that row with first row
	column_1 = matrix[:,0]
	max_index = np.argmax(column_1)
	if max_index != 0:
		matrix[0], matrix[max_index] = swap_rows(matrix[0], matrix[max_index])

	print("\nThe pivoted matrix is:\n"+str(matrix)+"\n")
	
	""" Below logic is to sort all rows based on first column
	for i in range(n):     
		for j in range(i+1, n):
			if arr1[j][0] > arr1[i][0]:
				arr1[i] = arr1[i] - arr1[j]
				arr1[j] = arr1[i] + arr1[j]
				arr1[i] = arr1[j] - arr1[i]"""
				
	return matrix

def forward_elimination(matrix, size, pivot = False):
	for i in range(size):	
		for j in range(i+1, size):
			ratio = matrix[j][i]/matrix[i][i]
			ratio = round(ratio, my_round(d,ratio))

			for k in range(size+1):
				matrix[j][k] = matrix[j][k] - round(ratio* matrix[i][k], my_round(d,ratio* matrix[i][k]))

		if pivot:
			# Below logic executes pivoting of intermediate rows (for partial pivoting)
			if i+1 != size:
				col = np.argmax(abs(matrix[i+1:, i+1]))
				matrix[i+1], matrix[col+i+1] = swap_rows(matrix[i+1], matrix[col+i+1])

	for k in range(size):
		for l in range(k, size+1):
			matrix[k][l] = np.around(matrix[k][l], decimals = my_round(d, matrix[k][l]))

	return matrix

def back_substitution(y, size, arr):
	# Back Substitution
	y[size-1] = arr[size-1][size]/arr[size-1][size-1]

	for i in range(size-2,-1,-1):
		y[i] = arr[i][size]
		
		for j in range(i+1,size):
			y[i] = y[i] - round(arr[i][j]*y[j], my_round(d, arr[i][j]*y[j]))
		
		y[i] = y[i]/arr[i][i]
	
	for i in range(size):
		y[i] = round(y[i], my_round(d, y[i]))

	return y

def print_solution(z, size, precision):
	# Displaying solution
	print('\nThe solution obtained from Gaussian Elimination is: ')
	for i in range(n):
		print('X{} = {}' .format(i, z[i]), end = '\n')

def ge_with_pivot(aug_mat, size, precision):
	# Applying Gauss Elimination (With Partial Pivoting)
	sol = np.zeros(n)
	pivot_mat = partially_pivot(aug_mat) # Pivot first row

	fe_mat_piv = forward_elimination(pivot_mat, size, True)
	
	ge_mat = back_substitution(sol, size, fe_mat_piv)
	
	return ge_mat
	
def ge_without_pivot(aug_mat, size, precision):
	# Applying Gauss Elimination (Without Partial Pivoting)
	
	# Check validity of input to avoid divide by zero
	for i in range(size):
		if aug_mat[i][i] == 0.0:
			sys.exit('Divide by zero detected!') 
	sol = np.zeros(n)
	fe_mat_non_piv = forward_elimination(aug_mat, size)
		
	ge_mat = back_substitution(sol, size, fe_mat_non_piv)
	
	return ge_mat
		
sol_piv = ge_with_pivot(c, n, d)
sol_non_piv = ge_without_pivot(e, n, d)

print_solution(sol_piv, n, d)
print_solution(sol_non_piv, n, d)
