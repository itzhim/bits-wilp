print("Enter a number: ")
num = int(input())
ref_num = num
print("Enter order: ")
order = int(input())
sum = 0

"""while num!=0:
	digit = num % 10
	sum += digit
	num = num // 10
print(sum)"""

sum=0
while num!=0:
	digit = num % 10
	sum += digit**order
	num = num // 10
print(sum)
if sum == ref_num:
	print("It's an Armstrong number")
else:
	print("It's not an Armstrong number")