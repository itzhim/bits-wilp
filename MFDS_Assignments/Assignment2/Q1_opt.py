import numpy as np
import sys
import copy
import math
import time
from numpy.random import RandomState
np.set_printoptions(suppress=True)
random_state = RandomState(1240)

def crout(A):
    crout_start = time.time()
    n = A.shape[0]
    
    U = np.zeros((n, n), dtype=np.double)
    L = np.zeros((n, n), dtype=np.double)
    
    for k in range(n):
        
        L[k, k] = A[k, k] - L[k, :] @ U[:, k]
        
        U[k, k:] = (A[k, k:] - L[k, :k] @ U[:k, k:]) / L[k, k]
        L[(k+1):, k] = (A[(k+1):, k] - L[(k+1):, :] @ U[:, k]) / U[k, k]
    
    crout_end = time.time()
    print(f"Time taken for Crout's decomposition: {crout_end - crout_start}")

    return L, U

def forward_substitution(L, b):
    fs_start = time.time()
    # Get number of rows
    n = L.shape[0]
    
    # Allocating space for the solution vector
    y = np.zeros_like(b, dtype=np.double);
    
    # Here we perform the forward-substitution.  
    # Initializing  with the first row.
    y[0] = b[0] / L[0, 0]
    
    # Looping over rows in reverse (from the bottom  up),
    # starting with the second to last row, because  the 
    # last row solve was completed in the last step.
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]
        
    fs_end = time.time()
    print(f"Time taken for forward substitution: {fs_end - fs_start}")

    return y

def back_substitution(U, y):
    bs_start = time.time()
    # Number of rows
    n = U.shape[0]
    
    # Allocating space for the solution vector
    x = np.zeros_like(y, dtype=np.double);

    # Here we perform the back-substitution.  
    # Initializing with the last row.
    x[-1] = y[-1] / U[-1, -1]
    
    # Looping over rows in reverse (from the bottom up), 
    # starting with the second to last row, because the 
    # last row solve was completed in the last step.
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
    
    bs_end = time.time()
    print(f"Time taken for backward substitution: {bs_end - bs_start}")

    return x

def forward_elimination(matrix, n):
    fe_start = time.time() 
    # Loop over rows
    for i in range(n):
            
        # Find the pivot index by looking down the ith 
        # column from the ith row to find the maximum 
        # (in magnitude) entry.
        p = np.abs(matrix[i:, i]).argmax()
            
        # We have to reindex the pivot index to be the 
        # appropriate entry in the entire matrix, not 
        # just from the ith row down.
        p += i 
    
        # Swapping rows to make the maximal entry the 
        # pivot (if needed).
        if p != i:
            matrix[[p, i]] = matrix[[i, p]]
           
        
        # Eliminate all entries below the pivot
        factor = matrix[i+1:, i] / matrix[i, i]
        matrix[i+1:] -= factor[:, np.newaxis] * matrix[i]

    fe_end = time.time()
    print(f"Time taken for forward elimination: {fe_end - fe_start}")

    return matrix

def call_crout(system, n):
    print("\nStart of Crout's Decomposition Method")
    sol = np.zeros(n)
    A = system[:, :n]
    b = system[:, -1:]

    l, u = crout(A)

    y = forward_substitution(l, b)
    
    return back_substitution(u, y)

def call_ge(system):
    print("\nStart of Gaussian Elimination Method")
    temp_mat = system
    b = system[:, -1:]

    # Get the number of rows
    n = temp_mat.shape[0]

    temp_mat = forward_elimination(temp_mat, n)

    x = back_substitution(temp_mat[:, :n], b)
        
    return x

def print_solution_crout(z, size):
    # Displaying solution
    print('\nThe solution obtained from Crout Method is: ')
    for i in range(n):
        print('X{} = {}' .format(i, z[i]), end = '\n')

def print_solution_ge(z, size):
	# Displaying solution
	print('\nThe solution obtained from Gaussian Elimination is: ')
	for i in range(n):
		print('X{} = {}' .format(i, z[i]), end = '\n')

# Reading the size of linear system
#n = int(input('Enter the size of linear system: '))

# Ask user if he/she wants to print solution
#print_sol = input('Would you like to display the solution? y for yes, n for no. \n')

for n in range(100, 2100, 100):
	print(f"\nFor n = {n}")
	# Making NumPy array of n x n+1 size
	arr = random_state.uniform(low=1, high=20, size=(n,n+1))

	sol_crout = call_crout(arr, n)
	sol_ge = call_ge(arr)

"""if print_sol == "y":
    print_solution_crout(sol_crout, n)
    print_solution_ge(sol_ge, n)"""
