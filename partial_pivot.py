import numpy as np

#a = np.array([[0.2248, 0.3513, 0.564 ],[0.6588, 0.9757, 0.8529]])
#a = np.around(a, decimals=p)
#a = np.array([[0.0,2.0,0.0,1.0,0.0],[2.0,2.0,3.0,2.0,-2.0],[4.0,-3.0,0.0,1.0,-7.0],[6.0,1.0,-6.0,-5.0,6.0]])
a = np.array([[0.2248, 0.9513, 0.564 ],[0.0000, 0.5757, 0.8529],[0.0000, -0.8468, 0.3572]])
#a = np.array([[0.0004, 1.4020, 1.4060],[0.4003, -1.5020, 2.5010]])
temp = np.zeros(2)

print()

"""for i in range(2):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!') 
        
    for j in range(i+1, 2):
        print(a[i][0],a[j][0])
        if a[j][0] > a[i][0]:
            a[i] = a[i] - a[j]
            a[j] = a[i] + a[j]
            a[i] = a[j] - a[i]"""

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

for i in range(1):
		column_highest = a[i+1:, i+1]
	#for j in range (i+1, 3):
max_index = np.argmax(abs(column_highest))
print(column_highest)	
print(max_index)

print(a)

"""print("before swap")
print(matrix)
#Himanshu new add start
if i+1 != size:
	col_largest = np.argmax(abs(matrix[i+1:, i+1]))
	print(col_largest)
	#print(matrix[i+1:, i+1],col_largest)
	matrix[i+1], matrix[col_largest+i+1] = swap_rows(matrix[i+1], matrix[col_largest+i+1])
#Himanshu new add end
print("after swap")
print(matrix)
print("\n")"""