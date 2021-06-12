# This is the DSAD Assignment 1 – PS11 - [Laptop Rentals]

"""
Program that returns the minimum number of laptops that the 
school needs to rent such that all students will always have 
access to a laptop when they need one

Returns minimum number of laptops required to be rented.
We will first get the requirements of a laptop as the time 
intervals during which students need them.

For example if [x,y] is the time interval it means that a student 
will borrow a laptop at time 'x' and return it at time 'y'.

Note: If a student returns a laptop at time 'y' then as per the 
problem statement immediately this laptop becomes available and 
another student can borrow it at the same time 'y'.

We will add all the borrowing times of students in one list.
Similarly we will add all the returning times of students in 
another list.

We will sort the two lists using HeapSort algorithm!

The idea here is that once the borrow and return times are in 
sorted order we will track down the number of laptops at any 
time by tacking the laptops that have been borrowed but not 
yet returned.

For example let's say the time intervals provided are:
T[x, y] = [0, 2], [1, 5], [4, 6], [0, 3]

Sorted list of borrowing times: [0, 0, 1, 4]
Sorted list of returning times: [2, 3, 5, 6]

Total laptops given to students at any time is the difference 
between total laptops borrowed and total laptops returned 
by that time.

Time	Borrowed/Returned	Laptops needed at this time
0			Borrowed				1
0			Borrowed				2
1			Borrowed				3
2			Returned				2
3			Returned				1
4			Borrowed				2
5			Returned				1
6			Returned				0

Hence, minimum laptops required is the maximum of number of 
laptops needed at any particular point of time.

In this example minimum laptops required would be 3.

"""

# Below is the function for Max-Heapification

# Make sure heap can be made of the array

def max_heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and arr[largest] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		# Heapify the root.
		max_heapify(arr, n, largest)

# Below function builds a max-heap (as shown in DSA slides).
def max_heap_building(max_heap, n):

	# floor(n/2) is taken because non-leaf nodes are from 1 to n/2
	for i in range(n//2 - 1, -1, -1): 
		max_heapify(max_heap, n, i)

	return max_heap

# Below function sorts an array using Heap Sort
def heap_sort(arr):
	n = len(arr)

	# Build a max-heap
	heap = max_heap_building(arr, n)

	# Below is similar to removal of elements from heap
	# and making a max-heap of remaining elements
	for i in range(n-1, 0, -1): 
		heap[i], heap[0] = heap[0], heap[i]
		max_heapify(heap, i, 0)


def laptop_required(b_time, r_time, n):

	# Sort borrowal time and return time arrays
	heap_sort(b_time)
	heap_sort(r_time)

	laptop_needed = 1
	min_laptop_required = 1
	i = 1
	j = 0

	while (i < n and j < n):

		# If next event in sorted order is borrowal,
		# increment count of laptops needed
		if (b_time[i] < r_time[j]):

			laptop_needed += 1
			i += 1
			#print("Inside if-> laptop_needed: " + str(laptop_needed) + ", " + str(i) + ", " + str(j))

		# Else decrement count of laptops needed
		elif (b_time[i] >= r_time[j]):

			laptop_needed -= 1
			j += 1
			#print("Inside elif-> laptop_needed: " + str(laptop_needed) + ", " + str(i) + ", " + str(j))

		# Update minimum laptop required
		if (laptop_needed > min_laptop_required):
			min_laptop_required = laptop_needed

	return min_laptop_required

with open("inputsPS11.txt","r+") as  input_file:
	lines = input_file.readlines()

borrow_time = []
return_time = []

for i in range(1, len(lines)):
	time_intervals = lines[i].split(", ")
	borrow_time.append(int(time_intervals[0]))
	return_time.append(int(time_intervals[1]))

n_students = len(borrow_time)

final_output = laptop_required(borrow_time, return_time, n_students)

with open("outputPS11.txt", "w+") as output_file:
	output_file.write("Minimum laptops required: " + str(final_output))
	output_file.close()

print("Minimum laptops required: " + str(final_output))
