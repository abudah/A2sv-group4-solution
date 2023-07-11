from string import ascii_lowercase
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent ={i:i for i in ascii_lowercase}
        rank = {i:ord(i) for i in parent}

        def find(node):
            if node == parent[node]:
                return node
            parentNode = find(parent[node]) 
            return parentNode
        def union(f_node, s_node):
            pf_node = find(f_node)
            ps_node = find(s_node)
            if pf_node != ps_node:
                if rank[pf_node] <= rank[ps_node]:
                    parent[ps_node] = pf_node
                else:
                    parent[pf_node] = ps_node
                
        
        for s_one, s_two in zip(s1, s2):
            union(s_one, s_two)
        text = ''
        for i in baseStr:
            text += find(i)
        
        return text


