class StaticArrays:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
        # write your code here
		self.array=[]*capacity
		self.capacity=capacity
		self.length=length
  
    def insertEnd(self, value):
		self.array[length]=value
		self.length+=1
        # write your code here
       
    def removeEnd(self):
		if self.length>0:
			self.length-=1
        # write your code here
   
    def insertMiddle(self, index, value):
        if index>0 and index<self.length:
            self.length+=1
            for i in range(index,self.length):
                self.array[i]=self.array[i+1]
			self.array[index]=value
        # write your code here, you need to shift elements after insertion
       
    def removeMiddle(self, index):
        if index>0 and index<self.length:
            self.length+=1
            for i in range(index,self.length):
                self.array[i]=self.array[i-1]
			
        # write your code here, you need to shift elements after removal
   
    def printArr(self):
        print(self.array)
        # write your code here