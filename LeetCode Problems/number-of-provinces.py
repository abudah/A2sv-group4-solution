class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        n = len(isConnected)
        visited = set()

        def dfs(curr):
            for child in range(n):
                if isConnected[curr][child] == 1 and child != curr and child not in visited:
                    visited.add(child)
                    dfs(child)
        for v in range(n):
            if v not in visited:
                province += 1
                dfs(v)
        return province
