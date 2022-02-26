import numpy as np
import math
import sympy
from sympy import symbols, diff
from numpy.random import RandomState
np.set_printoptions(suppress=True)
random_state = RandomState(1242)

# Round numbers according to significant digits
def my_round(d, x):
	return d - int(math.floor(math.log10(abs(x)))) - 1

n = 8
d = 4

#a = random_state.uniform(low=-3, high=2, size=(n))
pos_x = random_state.uniform(low=8, high=9, size=(n//2))
neg_x = random_state.uniform(low=-1, high=0, size=(n//2))
a = np.concatenate((pos_x,neg_x), axis = 0)

starting_x = random_state.uniform(low=1, high=2, size=(n))
starting_x = np.round(starting_x, 4)
print(starting_x)

for i in range(n):
	a[i] = np.around(a[i], d)
print(a)

partials, partials_second = [], []
x1, x2, x3, x4, x5, x6, x7, x8 = symbols('x1 x2 x3 x4 x5 x6 x7 x8', real=True)
symbols_list = [x1, x2, x3, x4, x5, x6, x7, x8]
f = a[0]*x1*x1 + a[1]*x2*x2 + a[2]*x3*x3 + a[3]*x4*x4 + a[4]*x5*x5 + a[5]*x6*x6 + a[6]*x7*x7 + a[7]*x8*x8
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
for i in range(0, 5):
	partials_val = []
	# get value of tou for a particular iteration
	tou_val = tou.subs([(x1, starting_x[0]), (x2, starting_x[1]), (x3, starting_x[2]), (x4, starting_x[3]), \
		(x5, starting_x[4]), (x6, starting_x[5]), (x7, starting_x[6]), (x8, starting_x[7])])
	#print(tau_val)

	f_prev_value = f_val_updated
	for idx, variable in enumerate(symbols_list):
		#print(starting_x[idx], partials[idx], (abs(tou_val) * partials[idx].subs(variable, starting_x[idx])))
		# run the main equation of gradient descent x_i+1 = x_i - tou*delta(f)
		val = starting_x[idx] - (abs(tou_val) * partials[idx].subs(variable, starting_x[idx]))
		val = round(val, 4)
		partials_val.append(val)
	#print(partials_val)
	# substitute the obtained values of variables to obtain new value of f
	f_val_updated = f.subs([(x1, partials_val[0]), (x2, partials_val[1]), (x3, partials_val[2]), (x4, partials_val[3]), \
		(x5, partials_val[4]), (x6, partials_val[5]), (x7, partials_val[6]), (x8, partials_val[7])])
	starting_x = partials_val #update the x variables for next iteration
	l_infinite_norm = abs(f_val_updated - f_prev_value)/abs(f_val_updated)
	
	#print(l_infinite_norm)
	#print(updated_x)
	#print(f_val_updated, f_prev_value, l_infinite_norm)
	print(f_val_updated)
	#print()

print(partials_val)
print(f_val_updated)


