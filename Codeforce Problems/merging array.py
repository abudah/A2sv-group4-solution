first,second=[int(i) for i in input().split()]
mem1=[int(i) for i in input().split()]
mem2=[int(i) for i in input().split()]

ind1=0
ind2=0
merged=[]
while ind1<first and ind2<second:
	if mem1[ind1]<mem2[ind2]:
		merged.append(str(mem1[ind1]))
		ind1+=1
	else:
		merged.append(str(mem2[ind2]))
		ind2+=1
merged.extend([str(i) for i in mem1[ind1:]])
merged.extend([str(i) for i in mem2[ind2:]])
print(" ".join(merged))