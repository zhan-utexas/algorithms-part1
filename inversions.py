fin = open("IntegerArray.txt")
original=[]
for line in fin:
    original.append(int(line.strip()))

def sort_and_count(input):
	n = len(input)

	if n == 1:
		return 0
	else:
		A = input[0:(n//2)]
		B = input[(n//2):]

		c = sort_and_count(A)
		d = sort_and_count(B)
		e = merge_and_count(C, D)

		return c + d + e

def merge_and_count(a, b):
	count = 0 #count of inversions
	output = []
	i = 0;
	j = 0;
	a_i = a[i]
	b_j = b[j]

	while (i < len(a) and j < len(b)):
		if a[i] <= b[j]:
			output.append(a[i])
			i += 1
		elif a[i] > b[j]:
			output.append(b[j])
			count = count + (len(a)-i)
			j += 1
	if i == len(a):
		output.extend(b[j:])
	else:
		output.extend(a[i:])

	return count

print sort_and_count([1,3,5,2,4,6])
print sort_and_count(original)
