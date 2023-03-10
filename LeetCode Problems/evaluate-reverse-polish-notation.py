class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations=['-','+','*','/']
        def operate(first,second,op):
            if op=='+':
                return first+second
            elif op=='-':
                return first-second
            elif op=="*":
                return first*second
            else:
                return int(first/second)

        for i in tokens:
            if i in operations:
                second=int(stack.pop())
                first=int(stack.pop())
                stack.append(operate(first,second,i))
            else:
                stack.append(int(i))
        return stack[-1]
            