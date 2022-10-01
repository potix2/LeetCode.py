from explore.BinarySearchTree.contains_nearby_almost_duplicate import Solution

def test_contains_nearby_almost_duplicate():
    s = Solution()
    assert s.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) == True

def test_contains_nearby_almost_duplicate2():
    s = Solution()
    assert s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) == False
