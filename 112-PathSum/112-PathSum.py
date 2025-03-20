# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # No TreeNode
        if not root:
            return False
        
        # Gets the remainder
        remainder = targetSum - root.val
        # Hit Zero return True
        if remainder == 0 and not root.left and not root.right:
            return True
        
        # Left or Right of the Node
        return self.hasPathSum(root.left, remainder) or self.hasPathSum(root.right, remainder)
