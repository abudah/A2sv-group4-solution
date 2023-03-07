class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        # first we store the directions of shifts into one array
        char_shift=[0 for i in range(len(s)+1)]
        for st,end,d in shifts:
            if d==0:
                char_shift[st]-=1
                char_shift[end+1]+=1
            else:
                char_shift[st]+=1
                char_shift[end+1]-=1

        # then we use prefix sum inorder to see the effects of shifts on the string 
        cum_sum=0
        res=''
        for i in range(len(s)):
            cum_sum+=char_shift[i]
            #then now we decode and apply the effects of the shifts on the string
            new_code=(((ord(s[i])+cum_sum)-97)%26)+97
            res+=chr(new_code)
        return res