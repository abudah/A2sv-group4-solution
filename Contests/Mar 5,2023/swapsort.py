el=int(input())

members=[int(i) for i in input().split()]
swap=[]

for step in range(el):
	min_idx = step
	for i in range(step + 1, el):
		if members[i] < members[min_idx]:
			min_idx = i
	if min_idx!=step:
		swap.append((step,min_idx))
		(members[step], members[min_idx]) = (members[min_idx], members[step])
print(len(swap))
for i in range(len(swap)):
	print(swap[i][0],swap[i][1])