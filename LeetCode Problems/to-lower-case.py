class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        for i in s:
            n = ord(i)
            if n >= 65 and n <= 90:
                res += chr(n+ 32)
            else:
                res += i
        return res