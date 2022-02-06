# Definition for a binary tree node.
import math
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], lower, upper) -> bool:
            if node is None:
                return True

            if node.val <= lower or upper <= node.val:
                return False

            return (validate(node.left, lower, node.val)) and (validate(node.right, node.val, upper))

        if root is None:
            return True

        return validate(root, -math.inf, math.inf)
