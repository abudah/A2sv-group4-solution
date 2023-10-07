class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        

        def sm_fr(s):
            return s.count(min(s))

        wordfr = [sm_fr(i) for i in words]
        answer = []
        wordfr.sort()
        
        for query in queries:
            n = sm_fr(query)
            left = 0 
            right = len(wordfr) - 1
            while left <= right:
                md = (left + right)//2
                if wordfr[md] <= n:
                    left = md + 1
                else:
                    right = md - 1
            answer.append(len(wordfr) - left)
        return answer