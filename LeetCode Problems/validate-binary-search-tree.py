# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversed = []
        def inorderTraversal(root,arr):
            if root != None:
                inorderTraversal(root.left, arr)
                arr.append(root.val)
                inorderTraversal(root.right, arr)
            
        inorderTraversal(root, traversed)

        return sorted(traversed) == traversed and len(traversed) == len(set(traversed))