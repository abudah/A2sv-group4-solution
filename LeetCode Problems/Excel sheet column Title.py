class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        def divide(n):
            if n == 0:
                return 
            n, remainder = divmod(n - 1, 26)                
            res.append(chr(65 + remainder))            
            divide(n)
        divide(columnNumber)
        return "".join(res[::-1])