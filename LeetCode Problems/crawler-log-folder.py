class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations=0
        for i in logs:
            if i=='../':
                if operations:
                    operations-=1
            elif i=='./':
                continue
            else:
                operations+=1
        return operations