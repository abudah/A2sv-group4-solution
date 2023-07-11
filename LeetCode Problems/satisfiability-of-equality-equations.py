class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {i:i for i in ascii_lowercase}
        rank = {i:ord(i) for i in parent}

        def find(node):
            if node == parent[node]:
                return node
            parentNode = find(parent[node])
            return parentNode


        def union(f_node, s_node):
            f_node = find(f_node)
            s_node = find(s_node)

            if f_node != s_node:
                if rank[f_node] <= rank[s_node]:
                    parent[s_node] = f_node
                else:
                    parent[f_node] = s_node
     
        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[-1])
            
        for eq in equations:
            if eq[1] == "!":
                if find(eq[0]) == find(eq[-1]):
                    return False
            
        return True
