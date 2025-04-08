# Last updated: 4/8/2025, 5:22:24 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        # Null case
        if not root:
            return 0
        
        # Recursive statement
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)