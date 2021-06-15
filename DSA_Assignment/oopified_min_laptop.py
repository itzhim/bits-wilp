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

import sys
class MaxHeap:

	def __init__(self, maxsize):
		
		self.maxsize = maxsize
		self.size = 0
		self.Heap = [0] * (self.maxsize + 1)
		self.Heap[0] = sys.maxsize
		self.FRONT = 1

	# Function to return the position of
	# parent for the node currently
	# at pos
	def parent(self, pos):
		
		return pos // 2

	# Function to return the position of
	# the left child for the node currently
	# at pos
	def leftChild(self, pos):
		
		return 2 * pos

	# Function to return the position of
	# the right child for the node currently
	# at pos
	def rightChild(self, pos):
		
		return (2 * pos) + 1

	# Function that returns true if the passed
	# node is a leaf node
	def isLeaf(self, pos):
		
		if pos >= (self.size//2) and pos <= self.size:
			return True
		return False

	# Function to swap two nodes of the heap
	def swap(self, fpos, spos):
		
		self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
											self.Heap[fpos])

	# Function to heapify the node at pos (motivation from DSA slides)
	def maxHeapify(self, pos):
		largest = pos

		# Check if left child of root exists and is
		# greater than root
		if (self.leftChild(pos) < self.size and 
			self.Heap[self.leftChild(pos)] > self.Heap[pos]):
			largest = self.leftChild(pos)
		else:
			largest = pos

		# Check if right child of root exists and is
		# greater than root
		if (self.rightChild(pos) < self.size and 
			self.Heap[self.rightChild(pos)] > self.Heap[largest]):
			largest = self.rightChild(pos)

		# Change root, if needed
		if largest != pos:
			self.Heap[pos], self.Heap[largest] = self.Heap[largest], self.Heap[pos]

			# Heapify the root.
			self.maxHeapify(largest)

	# Function to insert a node into the heap
	def insert(self, element):
		
		if self.size >= self.maxsize:
			return
		self.size += 1
		self.Heap[self.size] = element

		current = self.size

		while (self.Heap[current] >
			self.Heap[self.parent(current)]):
			self.swap(current, self.parent(current))
			current = self.parent(current)

	# Function to print the contents of the heap
	def Print(self):
		
		for i in range(1, (self.size // 2) + 1):
			print(" PARENT : " + str(self.Heap[i]) +
				" LEFT CHILD : " + str(self.Heap[2 * i]) +
				" RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

	# Function to remove and return the maximum
	# element from the heap
	def extractMax(self):
		popped = self.Heap[self.FRONT]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size -= 1
		self.maxHeapify(self.FRONT)
		return popped


def laptop_required(b_time, r_time, n):

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

def read_input(input_file):
	with open(input_file,"r+") as file:
		lines = file.readlines()
	return lines


def convert_input(lines):
	bor_t = []
	ret_t = []

	for i in range(1, len(lines)):
		t_int = lines[i].split(", ")
		bor_t.append(int(t_int[0]))
		ret_t.append(int(t_int[1]))

	return bor_t, ret_t

def create_output(file_name, output):
	with open(file_name, "w+") as file:
		file.write("Minimum laptops required: " + str(output))
		file.close()

	print("Minimum laptops required: " + str(output))

def create_heap(arr, size):
	max_heap = MaxHeap(n_students)

	for i in range(0, size):
		max_heap.insert(arr[i])
	return max_heap

def heap_sort(heap, size):
	sorted_heap = []

	for i in range(0, size):
		sorted_heap.insert(0, heap.extractMax())

	return sorted_heap

# Driver Code
if __name__ == "__main__":
	borrow_time, return_time = convert_input(read_input("inputsPS11.txt"))
	n_students = len(borrow_time)

	sorted_b_time = heap_sort(create_heap(borrow_time, n_students), n_students)
	sorted_r_time = heap_sort(create_heap(return_time, n_students), n_students)

	final_output = laptop_required(sorted_b_time, sorted_r_time, n_students)

	create_output("outputPS11.txt", final_output)
