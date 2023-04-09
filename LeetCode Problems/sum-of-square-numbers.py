class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # if c < 3:
        #     return True
        left, right = 0 , int(math.sqrt(c))
        
        while left <= right:
            val=left*left + right*right

            if  val > c:
                right -= 1
            elif val < c:
                left += 1
            else:
                return True
        return False

