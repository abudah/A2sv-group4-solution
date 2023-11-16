from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = set()
	    
	    def dfs(node, parent, visited):
	        if node in visited:
	            return True
    	    visited.add(node)
    	    for neigh in adj[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node, visited):
                    return True
            return False
        
        for node in range(V):
            if node in visited:
                continue
            if dfs(node, node, visited):
                return True
                
        return False

