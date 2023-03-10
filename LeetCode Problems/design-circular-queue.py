class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[-1]*k
        self.front=0
        self.rear=0
        self.size=0

    def enQueue(self, value: int) -> bool:
        if not self.isFull() and self.queue[self.rear]==-1:
            self.queue[self.rear]=value
            self.rear=(self.rear+1)%len(self.queue)
            self.size+=1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue[self.front]=-1
            self.front=(self.front+1)%len(self.queue)
            self.size-=1
            return True
        return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear-1]

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==len(self.queue)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()