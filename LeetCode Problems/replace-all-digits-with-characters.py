class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(a, b):
            return chr(ord(a)+b)
        s_list = [i for i in s]
        for i in range(len(s)):
            if i%2 != 0:
                s_list[i] = shift(s[i-1], int(s[i]))
        return ''.join(s_list)