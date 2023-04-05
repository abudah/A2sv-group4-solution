# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.answer = []

        def findPaths(root, paths):
            if not root:
                return self.answer
            if not root.left and not root.right: 
                paths.append(str(root.val))
                self.answer.append(''.join(paths))
                paths.pop()
                return self.answer

            # place
            paths.append(str(root.val))
            paths.append("->")

            # find paths
            findPaths(root.left, paths)
            findPaths(root.right, paths)
            
            # remove 
            paths.pop()
            paths.pop()
            
            return self.answer
        return findPaths(root, [])