def count_frequency(input_para):
	frequency_dict = {}
	count = 0
	with open(input_para,"r") as f:
		read_file = f.read()
		words = read_file.split()
		for word in words:
			frequency_dict[word] = 0
		for word in words:
			if word in frequency_dict.keys():
				frequency_dict[word] += 1
	return frequency_dict

def top_3_frequency(input_dict):
	top_1 = 0
	top_3_list = []
	#for i in range(0,3):
	for key in input_dict.keys():
		temp = input_dict[key]
		if top_1 < temp:
			top_3_list.append(key)
			#print(temp)
			top_1 = temp
			#del input_dict[key]
	print(top_1)
dict = count_frequency("paragraph.txt")
print(dict)
top_3_frequency(dict)