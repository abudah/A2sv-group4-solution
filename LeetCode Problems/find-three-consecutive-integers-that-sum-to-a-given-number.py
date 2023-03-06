class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        firstNumber=num//3-1
        if (3*firstNumber+3)==num:
            return [firstNumber,firstNumber+1,firstNumber+2] 
        else:
            return []
        