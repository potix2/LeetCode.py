from explore.BinarySearchTree.height_balanced_bst import Solution, TreeNode

def test_is_balanced():
    s = Solution()
    assert s.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == True

def test_is_balanced2():
    s = Solution()
    assert s.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))) == False
