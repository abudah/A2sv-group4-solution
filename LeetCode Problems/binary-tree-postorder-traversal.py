# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def traverse(tree):
            if tree!=None:
                traverse(tree.left)
                traverse(tree.right)
                arr.append(tree.val)
        traverse(root)
        return arr
