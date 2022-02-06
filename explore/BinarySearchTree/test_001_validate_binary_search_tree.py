from explore.BinarySearchTree.validate_binary_search_tree import Solution, TreeNode


def test_empty():
    solution = Solution()
    assert solution.isValidBST(None) == True


def test_valid_bst():
    valid_bst = TreeNode(2, TreeNode(1), TreeNode(3))
    solution = Solution()
    assert solution.isValidBST(valid_bst) == True


def test_valid_bst2():
    valid_bst = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6)))
    solution = Solution()
    assert solution.isValidBST(valid_bst) == True


def test_invalid_bst():
    invalid_bst = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    solution = Solution()
    assert solution.isValidBST(invalid_bst) == False


def test_symmetry():
    tree = TreeNode(2, TreeNode(2), TreeNode(2))
    solution = Solution()
    assert solution.isValidBST(tree) == False


def test_invalid_bst2():
    invalid_bst = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    solution = Solution()
    assert solution.isValidBST(invalid_bst) == False
