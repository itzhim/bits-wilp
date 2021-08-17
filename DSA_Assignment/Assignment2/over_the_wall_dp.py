boxes = [7, 8, 1, 7, 8, 7, 1, 2, 2, 3, 5]
wall_h = 38

#boxes = [6, 9, 13, 2, 18, 7, 22, 45, 3, 15, 1, 33]
#wall_h = 55

#n_boxes = [2, 10, 4, 9]
#wall_h = 5

boxes.sort(reverse=True)

n = len(boxes)
print(boxes)
t1 = wall_h
t2 = wall_h

def min_boxes(t1_l, t2_l, boxes_l, count_t1, count_t2):
	t1_l = t1_l - boxes_l[0]
	t2_l = t2_l - boxes_l[1]
	print(t1_l, t2_l)
	if (t1_l <=0 and t2_l <= 0):
		print("if condition")
		print(count_t1, count_t2)
		#print(count_t1 + count_t2)
		return count_t1 + count_t2
	if t1_l > 0:
		count_t1 += 1
	if t2_l > 0:
		count_t2 += 1
	print(count_t1, count_t2)

	
	if (t2_l >= t1_l):
		# swap the priority of towers because the one with the more remaining height
		# should be given more priority
		temp = t1_l
		t1_l = t2_l
		t2_l = temp
		boxes_l = boxes_l[2:]
		print(t1_l, t2_l)
		print(boxes_l)
		# recursive call
		tot_count = min_boxes(t1_l, t2_l, boxes_l, count_t1, count_t2)
		if tot_count > 0:
			return tot_count

	else:
		try:
			boxes_l = boxes_l[2:]
		except:
			print("Not suffcient boxes left")
		print(t1_l, t2_l)
		print(boxes_l)
		tot_count = min_boxes(t1_l, t2_l, boxes_l, count_t1, count_t2)
		if tot_count > 0:
			return tot_count
		#print("hello")


y = min_boxes(t1, t2, boxes, 0, 0)
print(y)
