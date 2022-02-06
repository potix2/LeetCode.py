# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._index = -1
        self._sorted_nodes = []
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return

        self._inorder(root.left)
        self._sorted_nodes.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        self._index += 1
        return self._sorted_nodes[self._index]

    def hasNext(self) -> bool:
        return self._index + 1 < len(self._sorted_nodes)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
