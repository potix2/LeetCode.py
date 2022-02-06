# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        leftmost = self.root
        while leftmost:
            self.node = leftmost
            leftmost = leftmost.left

    def _find_successor(self) -> Optional[TreeNode]:
        successor = None
        root = self.root

        while root:
            if self.node.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor

    def next(self) -> int:
        val = self.node.val
        self.node = self._find_successor()
        return val

    def hasNext(self) -> bool:
        return self.node

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
