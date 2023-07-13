class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0]*n

        def find(node):
            if node == parent[node]:
                return node
            parentNode = find(parent[node])
            return parentNode
        def union(f_node, s_node):
            pf_node = find(f_node)
            ps_node = find(s_node)

            if pf_node != ps_node:
                if rank[pf_node] > rank[ps_node]:
                    parent[ps_node] = pf_node
                elif rank[pf_node] < rank[ps_node]:
                    parent[pf_node] = ps_node
                else:
                    parent[pf_node] = ps_node
                    rank[ps_node] += 1
        
        for start, destination, distance in roads:
            union(start-1, destination-1)
        
        pstart = find(0)
        res = inf
        
        for start, destination, distance in roads:
            pdestination = find(destination-1)
            
            if pstart == pdestination:
                res = min(res, distance)
        return res

    