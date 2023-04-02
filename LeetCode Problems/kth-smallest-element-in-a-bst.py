# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []
        def traverse(sub_tree,arr):
            if sub_tree != None:
                traverse(sub_tree.left, arr)
                arr.append(sub_tree.val)
                traverse(sub_tree.right, arr)
            return arr
        return traverse(root, elements)[k-1]