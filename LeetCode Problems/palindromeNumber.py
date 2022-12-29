class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        revertedNum=0
        originalNum=x
        while x>0:
            revertedNum=revertedNum*10 + x%10
            x=x//10
        return revertedNum==originalNum