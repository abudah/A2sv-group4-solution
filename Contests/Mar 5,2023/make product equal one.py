el=int(input())

members=[int(i) for i in input().split()]

negatives=0
zeros=0
even=False
members.sort()
for i in members:
	if i<0:
		negatives+=1
	if i==0:
		zeros+=1
if negatives%2==0:
	even=True

operations=0
if even:
	for i in range(negatives):
		operations+=-1-members[i]
		members[i]=str(-1)
	for i in range(negatives,negatives+zeros):
		operations+=1
		members[i]=str(1)

	for i in range(negatives+zeros,el):
		operations+=members[i]-1
		members[i]=str(1)
else:
	for i in range(negatives-1):
		operations+=(-1-members[i])
		members[i]=str(-1)
	operations+=(1-members[negatives-1])
	members[negatives-1]=str(1)
	for i in range(negatives,el):
		operations+=members[i]-1
		members[i]=str(1)

print(operations)
	
	