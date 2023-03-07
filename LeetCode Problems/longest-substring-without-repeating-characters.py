class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        back=0
        front=0
        max_window=0
        while front<len(s):
            if s[front] in s[back:front]:
                while s[back]!=s[front]:
                    back+=1
                back+=1
            else:
                front+=1
            max_window=max(max_window,front-back)
        return max_window