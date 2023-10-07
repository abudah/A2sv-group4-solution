class Solution:
    def smallestSubsequence(self, s: str) -> str:
        collections = defaultdict(list)

        for key, value in Counter(s).items():
            collections[key].extend([value, False])
    

        stack = []

        for i in s:
            while stack and stack[-1] >= i and collections[stack[-1]][0] > 1 and not collections[i][1]:
                collections[stack[-1]][1] = False
                collections[stack[-1]][0] -= 1
                stack.pop()

            if not collections[i][1]:
                collections[i][1] = True
                stack.append(i)
            else:
                collections[i][0] -= 1
        
        return "".join(stack)
