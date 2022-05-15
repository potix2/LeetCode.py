from explore.BinarySearchTree.kth_largest import KthLargest


def test_simple():
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    assert(kth_largest.add(3) == 4)
    assert(kth_largest.add(5) == 5)
    assert(kth_largest.add(10) == 5)
    assert(kth_largest.add(9) == 8)
    assert(kth_largest.add(4) == 8)

def test_empty():
    kth_largest = KthLargest(1, [])
    assert(kth_largest.add(-3) == -3)
    assert(kth_largest.add(-2) == -2)
    assert(kth_largest.add(-4) == -2)
    assert(kth_largest.add(0) == 0)
    assert(kth_largest.add(4) == 4)