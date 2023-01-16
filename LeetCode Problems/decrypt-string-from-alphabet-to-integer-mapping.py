class Solution:
    def freqAlphabets(self, s: str) -> str:
        dictionary={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10#':'j','11#':'k','12#':'l','13#':'m','14#':'n','15#':'o','16#':'p','17#':'q','18#':'r','19#':'s','20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}
        a=[]
        words=''
        for i in s:
            if i=='#':
                for j in range(len(words)-2):
                    a.append(dictionary[words[j]])
                greats=words[-2:]
                a.append(dictionary[greats+'#'])
                words=''
            else:
                words+=i
        if words:
            for i in words:
                print(i)
                a.append(dictionary[i])
        
        return "".join(a)