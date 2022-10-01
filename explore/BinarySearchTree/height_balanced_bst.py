from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            lh = self.height(root.left)
            rh = self.height(root.right)
            return 2 + max(lh, rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        elif self.isBalanced(root.left) and self.isBalanced(root.right):
            lh = self.height(root.left)
            rh = self.height(root.right)
            return abs(lh - rh) <= 1
        else:
            return False

