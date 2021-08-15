#n_boxes = [7, 8, 19, 7, 8, 7, 10, 20, 2, 3, 5]
#wall_h = 38

n_boxes = [6,9,13,2,18,7,22,45,3,15,1,33]
wall_h = 55

#n_boxes = [6,9,13,9,8]
#wall_h = 55

#n_boxes = [2, 10, 4, 9]
#wall_h = 5

sorted_l = n_boxes.sort(reverse=True)

n = len(n_boxes)
print(n_boxes)
t1 = wall_h
t2 = wall_h
count_t1 = 1
count_t2 = 1
for i in range(0, n, 2):
	t1 = t1 - n_boxes[i]
	if t1 > 0:
		count_t1 += 1
		#print(t1, count_t1)
	else:
		#print(t1, count_t1)
		break
	
	#print(t1, count_t1)

for i in range(1, n, 2):
	t2 = t2 - n_boxes[i]
	if t2 > 0:
		count_t2 += 1
		#print(t2, count_t2)
	else:
		#print(t2, count_t2)
		break

if (t1 > 0 or t2 > 0):
	print("Impossible!")
else:
	print("The minimum requirement is: " + str(count_t1 + count_t2))

#print(count_t1, count_t2)
#print(count_t1 + count_t2)
