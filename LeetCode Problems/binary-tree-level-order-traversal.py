# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result
        queue = deque([root])
        result.append([root.val])
        while queue:
            
            res = []

            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    res.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    res.append(node.right.val)
                    queue.append(node.right)
            if not res:
                continue
            result.append(res)
        return result