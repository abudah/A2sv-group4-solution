"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        res = [0]
        def dfs(node, depth):
            if not node:
                return 0
            depth += 1
            res[0] = max(res[0], depth)
            for nodes in node.children:
                dfs(nodes, depth)        
        dfs(root, 0)
        return res[0]