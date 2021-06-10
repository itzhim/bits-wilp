import numpy as np
from numpy.random import RandomState
np.set_printoptions(suppress=True)

#random_state = RandomState(1240)

size = int(input("Enter size of matrix: "))

# Note: This is for augmented matrix 
# i.e. for mxn matrix, mx(n-1) matrix would be diagonally non-dominant

# Generate matrix which can't be made diagonally dominant
flag = 0
while (flag != size*size):
	flag = 0
	a = 20 * np.random.rand(size,size+1)
	for i in range(len(a[:,0])):
		for j in range(len(a[0,:])-1):
			if abs(a[i][j]) < np.sum(abs(a[i][:size])) - abs(a[i][j]):
				flag += 1
			else:
				flag -= 1

print("This is your diagonally non-dominant matrix:")
print(a)