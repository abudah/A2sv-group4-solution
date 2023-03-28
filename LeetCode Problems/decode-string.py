class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        k=''
        decode=''
        for i in s:
            if i=='[':
                stack.append(decode)
                stack.append(int(k))
                decode=k=''
            elif i.isdigit():
                k+=i
            elif i==']':
                num=stack.pop()
                s=stack.pop()
                decode=s+decode*num
            else:
                decode+=i
        return decode


