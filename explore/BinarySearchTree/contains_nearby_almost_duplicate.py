from typing import List
from sortedcontainers import SortedList


class Solution:
   def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
       window = SortedList()
       for i in range(len(nums)):
           if i > k:
               window.remove(nums[i - k -1])
           idx1 = SortedList.bisect_left(window, nums[i] - t)
           idx2 = SortedList.bisect_right(window, nums[i] + t)

           if idx1 != idx2 and idx1 != len(window):
               return True

           window.add(nums[i])

       return False