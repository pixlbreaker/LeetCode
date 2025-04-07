# Last updated: 4/7/2025, 3:39:13 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        left = root.left
        right = root.right

        root.left = right
        root.right = left

        root.left = self.invertTree(right)
        root.right = self.invertTree(left)

        return root