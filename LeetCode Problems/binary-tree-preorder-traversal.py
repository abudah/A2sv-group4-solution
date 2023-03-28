# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def traverse(sub_tree):
            if sub_tree!=None:
                arr.append(sub_tree.val)
                traverse(sub_tree.left)
                traverse(sub_tree.right)
        traverse(root)
        return arr