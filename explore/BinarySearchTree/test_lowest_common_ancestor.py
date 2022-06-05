from explore.BinarySearchTree.lowest_common_ancestor import Solution, TreeNode


def test_case1():
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    p = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    q = TreeNode(8, TreeNode(7), TreeNode(9))
    s = Solution()
    assert(s.lowestCommonAncestor(root, p, q) == root)


def test_case2():
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    p = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    q = TreeNode(4, TreeNode(3), TreeNode(5))
    s = Solution()
    assert(s.lowestCommonAncestor(root, p, q) == p)