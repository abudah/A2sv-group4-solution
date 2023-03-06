class Solution:
    def transform(self,nums):
        newNum=0
        c=0
        for i in nums[::-1]:
            newNum+=(ord(i)-48)*10**b
            b+=1
        return newNum
    def multiply(self, num1: str, num2: str) -> str:
        return(str(self.transform(num1)*self.transform(num2)))
        

        