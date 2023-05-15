# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def insert(root, val):
            if not root:
                return TreeNode(val)
            elif root.val < val:
                root.right = insert(root.right, val)
            elif root.val > val:
                root.left = insert(root.left, val)
            return root
        root = None

        for el in preorder:
            root = insert(root, el)
        return root