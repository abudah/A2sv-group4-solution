class DataStream:

    def __init__(self, value: int, k: int):
        self.integerStream=[]
        self.value=value
        self.k=k
        

    def consec(self, num: int) -> bool:

        if num!=self.value:
            self.integerStream.clear()
            return False
        self.integerStream.append(num)
        k=self.k
        if len(self.integerStream)>=k:
            return True
        return False
      
        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)