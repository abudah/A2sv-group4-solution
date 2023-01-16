class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaced=''
        j=0
        for i in spaces:
            spaced+=s[j:i]+' '
            j=i
        spaced+=s[j:]
        return spaced