# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_elements =[]
        q_elements = []
        def searchBST(root,arr, val):
            if root.val < val:
                arr.append(root.val)
                return searchBST(root.right, arr,  val)
            elif root.val > val:
                arr.append(root.val)
                return searchBST(root.left, arr, val)
            else:
                arr.append(root.val)                
                return arr
                
        def searchNode(root, val):
            if not root:
                return root
            if root.val < val:
                return searchNode(root.right, val)
            elif root.val > val:
                return searchNode(root.left, val)
            else:
                return root


        p_el = searchBST(root, p_elements, p.val)[::-1]
        q_el = searchBST(root, q_elements, q.val)[::-1]
        common = -1000000000000
        for i in p_el:
            if i in q_el:
                common = i
                break
        
        return searchNode(root, common)
        
        