import numpy as np
import sys
import copy
import math
import time
from numpy.random import RandomState
np.set_printoptions(suppress=True)
random_state = RandomState(1240)

def swap_rows(row_1, row_2):
	row_1 = row_1 - row_2
	row_2 = row_1 + row_2
	row_1 = row_2 - row_1
	return row_1, row_2

def back_substitution(y, size, arr):
    bs_start = time.time_ns()
    # Back Substitution
    y[size-1] = arr[size-1][size]/arr[size-1][size-1]

    for i in range(size-2,-1,-1):
        y[i] = arr[i][size]
        
        for j in range(i+1,size):
            y[i] = y[i] - arr[i][j]*y[j]
        
        y[i] = y[i]/arr[i][i]

    bs_end = time.time_ns()
    print(f"Time taken for backward substitution: {bs_end - bs_start}")
    return y

def forward_substitution(y, size, arr):
    fs_start = time.time_ns()
    # Back Substitution
    y[0] = arr[0][size]/arr[0][0]

    for i in range(1, size, 1):
        y[i] = arr[i][size]
        
        for j in range(0,i):
            y[i] = y[i] - arr[i][j]*y[j]
        
        y[i] = y[i]/arr[i][i]

    fs_end = time.time_ns()
    print(f"Time taken for forward substitution: {fs_end - fs_start}")
    return y

def crout(A):
    crout_start = time.time_ns()
    n = A.shape[0]
    
    U = np.zeros((n, n), dtype=np.double)
    L = np.zeros((n, n), dtype=np.double)
    
    for k in range(n):
        
        L[k, k] = A[k, k] - L[k, :] @ U[:, k]
        
        U[k, k:] = (A[k, k:] - L[k, :k] @ U[:k, k:]) / L[k, k]
        L[(k+1):, k] = (A[(k+1):, k] - L[(k+1):, :] @ U[:, k]) / U[k, k]
    
    crout_end = time.time_ns()
    print(f"Time taken for Crout's decomposition: {crout_end - crout_start}")

    return L, U

def partially_pivot(matrix):
	# Partially pivoting the input matrix

	# If a row except first row has larger value in first column
	# then swap that row with first row
	column_1 = matrix[:,0]
	max_index = np.argmax(column_1)
	if max_index != 0:
		matrix[0], matrix[max_index] = matrix[0], matrix[max_index]

	return matrix

def forward_elimination(matrix, size, pivot = False):
	fe_start = time.time_ns()
	for i in range(size):	
		for j in range(i+1, size):
			ratio = matrix[j][i]/matrix[i][i]

			for k in range(size+1):
				matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

		if pivot:
			# Below logic executes pivoting of intermediate rows (for partial pivoting)
			if i+1 != size:
				col = np.argmax(abs(matrix[i+1:, i+1]))
				matrix[i+1], matrix[col+i+1] = matrix[i+1], matrix[col+i+1]

	fe_end = time.time_ns()
	print(f"Time taken for forward elimination: {fe_end - fe_start}")
	return matrix

def print_solution_ge(z, size):
	# Displaying solution
	print('\nThe solution obtained from Gaussian Elimination is: ')
	for i in range(n):
		print('X{} = {}' .format(i, z[i]), end = '\n')

def print_solution_crout(z, size):
	# Displaying solution
	print('\nThe solution obtained from Crout Method is: ')
	for i in range(n):
		print('X{} = {}' .format(i, z[i]), end = '\n')

def ge_with_pivot(aug_mat, size):
	# Applying Gauss Elimination (With Partial Pivoting)
	sol = np.zeros(n)
	pivot_mat = partially_pivot(aug_mat) # Pivot first row

	fe_mat_piv = forward_elimination(pivot_mat, size, True)
	
	ge_mat = back_substitution(sol, size, fe_mat_piv)
	
	return ge_mat

def call_crout(system, n):
	sol = np.zeros(n)
	A = system[:, :n]
	b = system[:, -1:]

	l, u = crout(A)

	forward_sol = np.zeros(n)
	l_b = np.column_stack((l, b))

	forward_subs = forward_substitution(forward_sol, n, l_b)
	u_y = np.column_stack((u, forward_subs))

	sol_crout = back_substitution(sol, n, u_y)

	return sol_crout

print("Welcome to the comparison of Gaussian Elimination and Crout's Method!")

# Reading the size of linear system
n = int(input('Enter the size of linear system: '))

# Ask user if he/she wants to print solution
print_sol = input('Would you like to display the solution? y for yes, n for no. \n')

# Making NumPy array of n x n+1 size
arr = random_state.uniform(low=1, high=20, size=(n,n+1))

sol_ge = ge_with_pivot(arr, n)
sol_crout = call_crout(arr, n)

if print_sol == "y":
	print_solution_crout(sol_crout, n)
	print_solution_ge(sol_ge, n)
