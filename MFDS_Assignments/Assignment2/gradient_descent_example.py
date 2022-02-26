import numpy as np
import math
import sympy
from sympy import symbols, diff
np.set_printoptions(suppress=True)

n = 2
d = 4
starting_x = [1, 3]

partials, partials_second = [], []
x, y = symbols('x y', real=True)
symbols_list = [x, y]
f = 3*x*x + y*y 
print(f)

hessian = np.zeros((n,n))

#generate partial delta of f
for variable in symbols_list:
	partial_diff = diff(f, variable)
	partials.append(partial_diff)
	partial_diff = diff(partial_diff, variable)
	partial_diff = round(partial_diff, 4)
	partials_second.append(partial_diff)

# create Hessian matrix
for i in range(0, n):
	hessian[i][i] = np.round(float(partials_second[i]), 4)

# generate function for tou
num = 0
den = 0
for i in range(0, len(partials)):
	num += (partials[i] * partials[i]) 
	den += (hessian[i][i] * partials[i] * partials[i])
	tou = (partials[i] * partials[i]) / ((partials[i] * hessian[i][i]) * partials[i])
tou = num/den
print(partials)
print(num)
print(den)
print(tou)

f_val_updated = 1
for i in range(0, 10):
	partials_val = []
	tou_val = tou.subs([(x, starting_x[0]), (y, starting_x[1])])
	#print(tou_val)

	f_prev_value = f_val_updated
	for idx, variable in enumerate(symbols_list):
		#print(starting_x[idx], partials[idx], (abs(tou_val) * partials[idx].subs(variable, starting_x[idx])))
		val = starting_x[idx] - (abs(tou_val) * partials[idx].subs(variable, starting_x[idx]))
		val = round(val, 4)
		partials_val.append(val)

	f_val_updated = f.subs([(x, partials_val[0]), (y, partials_val[1])])
	starting_x = partials_val
	l_infinite_norm = abs(f_val_updated - f_prev_value)/abs(f_prev_value)
	#print(f_val_updated, f_prev_value, l_infinite_norm)
	#print(l_infinite_norm)
	print('{0:.10f}'.format(f_val_updated))
	#print()

#print(partials_val)
print(f_val_updated)
