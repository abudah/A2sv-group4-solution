tc=int(input())
for i in range(tc):
	length=int(input())
	sequence=[i for i in input().split()]
	start=0
	end=length-1
	arranged=[]
	while start<end:
		arranged.append(sequence[start])
		arranged.append(sequence[end])
		start+=1
		end-=1
	if length%2!=0:
		arranged.append(sequence[start])
	if length==1:
		print(' '.join(sequence))
	else:
		print(' '.join(arranged)) 