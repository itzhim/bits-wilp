import numpy as np
import sys
import copy
import math
from numpy.random import RandomState
np.set_printoptions(suppress=True)
random_state = RandomState(1240)

diag_dom_condition = False

# Generate diagonally dominant matrix
while diag_dom_condition != True:
	a = 10 * random_state.rand(3, 4)
	a = np.around(a, decimals=4)
	diag_dom_condition = (np.abs(a[0][0])>np.abs(a[0][1])+np.abs(a[0][2])) and \
	(np.abs(a[1][1])>np.abs(a[1][0])+np.abs(a[1][2])) and \
	(np.abs(a[2][2])>np.abs(a[2][0])+np.abs(a[2][1]))

# Generate matrix which can't be made diagonally dominant
# Note: This is for augmented matrix 
# i.e. for m x n matrix, m x (n-1) matrix would be diagonally non-dominant

"""Also note that a matrix which looks diagonally non-dominant
may be converted to diagonally dominant by interchanging the rows.
Hence, it's necessary to take care of this condition as well by 
making rows whose absolute value of each element is smaller than 
the sum of absolute values of other elements in the same row"""

size = int(input("Enter size of matrix: "))

flag = 0
while (flag != size*size):
	flag = 0
	b = 10 * random_state.rand(size,size+1)
	b = np.around(b, decimals=4)
	for i in range(len(b[:,0])):
		for j in range(len(b[0,:])-1):
			if abs(b[i][j]) < np.sum(abs(b[i][:size])) - abs(b[i][j]):
				flag += 1
			else:
				flag -= 1

print("\nThis is your diagonally dominant matrix:")
print(a)

print("\nThis is your diagonally non-dominant matrix:")
print(b)

diag_dom = int(input("\nEnter the condition: 0 for diagonally dominant, 1 for diagonally non-dominant: "))

if diag_dom == 0:
	c = copy.deepcopy(a)
elif diag_dom == 1:
	c = copy.deepcopy(b)


def decompose(A):
  nrow = len(A[:,0])
  L = np.tril(A)
  U = np.triu(A)
  for i in range(nrow):
    L[i][i] = 0.0
    U[i][i] = 0.0
  return L,np.identity(nrow),U

# For the norm calculation of Gauss Seidal method
# normalized matrix is used
def norm_gs(A):
	nrow = len(A[:,0])
	for i in range(nrow):
		A[i] = A[i]/A[i][i]
	
	L, I, U = decompose(d)
	
	i_plus_l = I + L
	i_plus_l_inv = np.linalg.inv(i_plus_l)
	
	p = np.matmul(i_plus_l_inv,U)
	frob_norm = np.linalg.norm(p)
	frob_norm = round(frob_norm, 4)
	print("\nThe Frobenius norm for Gauss Seidal method is: " + str(frob_norm))
	
	col_sum = []
	for i in range(len(p[:,0])):
		sum = np.sum(abs(p[i]))
		col_sum.append(sum)
	
	p_inf_norm = max(col_sum)
	p_inf_norm = round(p_inf_norm, 4)
	print("The infinite norm for Gauss Seidal method is: " + str(p_inf_norm))
	
	if p_inf_norm < 1.0:
		print("\nWe can guarantee that this matrix would converge!")

# For the norm calculation of Gauss Jacobi method
# unnormalized matrix is used
def norm_gj(A):
	L, I, U = decompose(A)
	D = np.diag(np.diag(A))

	l_plus_u = L + U
	d_inv = np.linalg.inv(D)

	p = -np.matmul(d_inv,l_plus_u)
	frob_norm = np.linalg.norm(p)
	frob_norm = round(frob_norm, 4)
	print("\nThe Frobenius norm for Gauss Jacobi method is: " + str(frob_norm))
	
	col_sum = []
	for i in range(len(p[:,0])):
		sum = np.sum(abs(p[i]))
		col_sum.append(sum)
	
	p_inf_norm = max(col_sum)
	p_inf_norm = round(p_inf_norm, 4)
	print("The infinite norm for Gauss Jacobi method is: " + str(p_inf_norm))
	
	if p_inf_norm < 1.0:
		print("\nWe can guarantee that this matrix would converge!")

e = copy.deepcopy(c)
d  = e[:,:size]
norm_gs(d)
norm_gj(d)

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (c[0][3]-c[0][1]*y-c[0][2]*z)/c[0][0]
f2 = lambda x,y,z: (c[1][3]-c[1][0]*x-c[1][2]*z)/c[1][1]
f3 = lambda x,y,z: (c[2][3]-c[2][0]*x-c[2][1]*y)/c[2][2]

# Implement Gauss Seidal Method
def gauss_seidal(x,y,z,e):
	count = 1
	condition = True
	print('\nCount\tx\ty\tz\n')
	while (condition and count<50):
		# In Gauss Seidal, newest available
		# values of variables are used
		x1 = round(f1(x,y,z),4)
		y1 = round(f2(x1,y,z),4)
		z1 = round(f3(x1,y1,z),4)
		print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
		e1 = abs((x-x1)/x1);
		e2 = abs((y-y1)/y1);
		e3 = abs((z-z1)/z1);

		count += 1
		x = x1
		y = y1
		z = z1

		condition = e1>e or e2>e or e3>e
	print('\nSolution from Gauss Seidal Method: x=%0.4f, y=%0.4f and z = %0.4f\n'% (x1,y1,z1))

# Implement Gauss Jacobi Method
def gauss_jacobi(x,y,z,e):
	count = 1
	condition = True
	print('\nCount\tx\ty\tz\n')
	while (condition and count<50):
		# In Gauss Jacobi, values of variables
		# available from last iteration are used
		x1 = round(f1(x,y,z),4)
		y1 = round(f2(x,y,z),4)
		z1 = round(f3(x,y,z),4)
		print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
		e1 = abs((x-x1)/x1);
		e2 = abs((y-y1)/y1);
		e3 = abs((z-z1)/z1);

		count += 1
		x = x1
		y = y1
		z = z1

		condition = e1>e or e2>e or e3>e

	print('\nSolution from Gauss Jacobi Method: x=%0.4f, y=%0.4f and z = %0.4f\n'% (x1,y1,z1))

# Initial setup
x0 = 0
y0 = 0
z0 = 0

# Reading tolerable error
e = float(input('Enter tolerance value required (in %): '))/100

gauss_seidal(x0,y0,z0,e)
gauss_jacobi(x0,y0,z0,e)