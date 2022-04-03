from explore.BinarySearchTree.basic_operations_in_a_bst import Solution, TreeNode

from typing import List

def helper(node: TreeNode) -> List[int]:
    if node is None:
        return []
    else:
        return [node.val] + helper(node.left) + helper(node.right)


def test_search_bst():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    expect = [2, 1, 3]
    solution = Solution()
    assert helper(solution.searchBST(root, 2)) == expect
