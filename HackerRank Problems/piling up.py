# Enter your code here. Read input from STDIN. Print output to STDOUT
testCases=int(input())
for i in range(testCases):
    numOfInputs=int(input())
    inputs=[int(i) for i in input().split()]
    left=0
    right=numOfInputs-1
    result="Yes"
    block=[]
    block.append(max(inputs[0],inputs[-1]))
    while left<=right:
        blockSize=max(inputs[left],inputs[right])
        if blockSize>block[-1]:
            result="No"
            break
        block.append(blockSize)
        left+=1
        right-=1
    print(result)