class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        count=0
        for i in s:
            if i=='(':
                stack.append(count)
                count=0
            else:
                count=stack.pop()+max(2*count,1)
        return count