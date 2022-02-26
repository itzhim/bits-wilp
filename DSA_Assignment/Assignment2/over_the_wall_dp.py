<<<<<<< HEAD
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
=======
"""DSAD_Assn2_scratchspace.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H2ceNXk9UYL8yHN2dWoLG8m0ZcL0d-tz

#DSAD Assignment 2
###Problem Statement present at : https://bits-pilani.instructure.com/courses/915/assignments/4644

####First Impression
It seems to be a Knapsack sort of problem. Similar to finding the minimum number of coins of different denomination to make up a given value. [Reference | https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/]

However, instead of above method, we can also use Greedy algorithm to solve this as given here: https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/

In above case, GFG has used normal array and sorted it but we may as well use max-heap.
Also, we need to calculate minimum number of boxes for 2 towers. (or in GFG context, we need to find minimum no of coins for 2 values, not just .
one as shown in the example)
Why the above point is necessary? Its because, we need to construct both towers simultaneously, without discrimination.
For example consider a scenario where we have following blocks:
{6,5,1,1,1,1,1,1,1,1,1}
Consider that the wall height is 7.
If we first construct the first tower, our greedy algorithm will say that we can directly use blocks of height 6 and 5 to create a (6 + 5 ) = 11 height wall. Them for the second tower, we will have have to use 7x 1-height blocks.
Thus we will end up using (2 + 7) = 9 blocks.

Instead, if we construct them simultaneously, i.e. 6 will go for tower 1
5 will go for tower 2
Then,
next block, i.e. 1 will go for tower 1, thus matching the wall size
next block, i.e. 1 will go for tower 2.
next block will again go to tower 2, thus matching the wall size.
Thus, we have used (2 + 3) = 5 blocks for constructing the towers
"""

import sys
class Block:
    def __init__(self, height):
        self.ht = height

class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0   #1 because the first entry is already put to 1(ignore)
        self.Heap = []  #Initialize empty array instead#[Block(0,0)] * (self.maxsize + 1)
        self.Heap.append(Block(1*sys.maxsize))
        self.FRONT = 1

    @classmethod
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
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],self.Heap[fpos])
  
    # Function to heapify the node at pos (motivation from DSA slides)
    def maxHeapify(self, pos):
        largest = pos
        if (self.leftChild(pos) <= self.size and self.Heap[self.leftChild(pos)].ht > self.Heap[pos].ht):
            largest = self.leftChild(pos)
        if (self.rightChild(pos) <= self.size and self.Heap[self.rightChild(pos)].ht > self.Heap[largest].ht):
            largest = self.rightChild(pos)
        if largest != pos:
            self.Heap[pos], self.Heap[largest] = self.Heap[largest], self.Heap[pos]
            self.maxHeapify(largest)
            
    def build_max_heap(self):
        for i in reversed(range(1, (self.size//2) + 1)):
            self.maxHeapify(i)

	# Function to insert a node into the heap
    def insert(self, element):
        self.size += 1
        self.Heap.insert(self.size, Block(element))        #This insert is list insert method. Do not confuse it for the def'ed insert
        current = self.size

        #Upheap bubbling
        while (self.Heap[current].ht > self.Heap[self.parent(current)].ht):
            self.swap(current, self.parent(current))
            current = self.parent(current)
        
        if self.size > self.maxsize:
            self.maxsize = self.size

	# Function to print the contents of the heap
    def Print(self):
        print("<Position> : (ht)")
        for i in range(1, (self.size // 2) + 1):
            if (i<=self.size):
                print(f" PARENT : ({self.Heap[i].ht})", end = "\t")
            if (2*i <= self.size):
                print(f" LEFT CHILD : ({self.Heap[2 * i].ht})", end="\t")
            if ((2*i + 1) <= self.size):
                print(f" RIGHT CHILD : ({self.Heap[2 * i + 1].ht})")
        print("")

	# Function to remove and return the maximum
	# element from the heap
    def extractMax(self):
        if (self.size <= 0):
            sys.exit("Heap extractMax called but there are no more elements in heap.\nExitting...")
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.build_max_heap()
        return popped

def read_input(input_file):
    try:
        with open(input_file,"r+") as file:
            lines = file.readlines()
        return lines
    except:
        sys.exit("Could not read input file. Please check")

unlimited_boxes = 0
def append_box(block, Rem_ht):
    """
    Check whether the given block can be used 
    Returns a list which contains the block height(s) if that block can be used
    This also check if the Rem_ht is greater than zero
    If it is less than zero, the function indicates its callee that the condition has been met
    Rem_ht <= 0 indicates that the tower has been constructed to satisfy its purpose.
    The indication is mostly from the Rem_ht passing :-)
    """
    global unlimited_boxes
    sub_blck_lst=[]

    if (unlimited_boxes != 0):
        while (block<Rem_ht):
            sub_blck_lst.append(block)
            Rem_ht -= block
    else:
        sub_blck_lst.append(block)
        Rem_ht -= block
    return sub_blck_lst, Rem_ht

"""
Creates two lists corresponding to the two towers, each containing the blocks 
(identified by the block height) that were used to build that particular tower
"""
# initially, remaining height of tower is K
def calculate_DP(heap, t1_rem_ht, t2_rem_ht, t1_blocks, t2_blocks, tot_box):

    if (heap.size > 0):
        # simultaneous update
        # update for tower 1
        if (t1_rem_ht > 0):
            block = heap.extractMax()

            # we want to prioritize the tower for which the difference
            # of the remaining height and current block size is lesser
            # this will save us from using extra boxes later on
            if (abs(t2_rem_ht - block.ht) < abs(t1_rem_ht - block.ht)):
                temp = t1_rem_ht
                t1_rem_ht = t2_rem_ht
                t2_rem_ht = temp
                ret_list, t1_rem_ht = append_box(block.ht, t1_rem_ht)
                t1_blocks.extend(ret_list)
            else:
                ret_list, t1_rem_ht = append_box(block.ht, t1_rem_ht)
                t1_blocks.extend(ret_list)

        # check if we still have blocks left
        if (heap.size <= 0):
            return -1

        # update for tower 2
        if (t2_rem_ht > 0):
            block = heap.extractMax()
            ret_list, t2_rem_ht = append_box(block.ht, t2_rem_ht)
            t2_blocks.extend(ret_list)

        if (t1_rem_ht <= 0 and t2_rem_ht <= 0):
            return len(t1_blocks) + len(t2_blocks), t1_rem_ht, t2_rem_ht

        tot_box, t1_rem_ht, t2_rem_ht = calculate_DP(heap, t1_rem_ht, t2_rem_ht, t1_blocks, t2_blocks, tot_box)

    if tot_box > 0:
        return tot_box, t1_rem_ht, t2_rem_ht
    else:
        return -1, t1_rem_ht, t2_rem_ht

if __name__ == "__main__":

    inputlines = read_input("inputPS11.txt")
    num_testcases = int(inputlines[0])
    data_lines = inputlines[1:]
    f = open("outputPS11.txt", "w+")
    print(len(data_lines))
    if len(data_lines) != 2 * num_testcases: 
        sys.exit("Something's wrong. I can feel it.") 

    for i in range(0, len(data_lines), 2):
        print("---------------TestCase_" + str(i//2) + "---------------")
        N = int(data_lines[i].split()[0])
        K = int(data_lines[i].split()[-1])
        block_list = [int(x) for x in data_lines[i + 1].split()]

        if(len(block_list) != N):
            sys.exit("Something's wrong, I can feel it.")

        heap = MaxHeap(N)
        for block in block_list:
            heap.insert(block)
        heap.Print()

        t1_blocks = []
        t2_blocks = []
        min_box = 0
        min_box, t1_rem_ht, t2_rem_ht = calculate_DP(heap, K, K, t1_blocks, t2_blocks, min_box)
        if ((t1_rem_ht > 0) or (t2_rem_ht > 0)):
            print(f"Unable to build both towers.\nRemaining height for tower 1: {t1_rem_ht} \
                \nRemaining height for tower 2: {t2_rem_ht}")
        print(min_box)

        f.write(f"{min_box} \n")

    f.close()
>>>>>>> 2bed254f49d0fd17af03ab9a72412a80858c6ae6
