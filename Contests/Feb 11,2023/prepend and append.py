tc=int(input())
for i in range(tc):
	length=int(input())
	binary=input()
	left=0
	right=len(binary)-1
	while left<right:
		if binary[left]==binary[right]:
			break
		left+=1
		right-=1
	print(right-left+1)