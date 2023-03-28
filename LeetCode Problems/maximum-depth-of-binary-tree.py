# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        great=1
        def traverse(tree,depth):
            if tree != None:
                return max(traverse(tree.left,depth+1),traverse(tree.right,depth+1))
            return depth
        
        return traverse(root,0)