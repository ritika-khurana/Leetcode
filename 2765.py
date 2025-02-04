from typing import List
from typing import pairwise
class Solution:
  def alternatingSubarray(self, nums: List[int]) -> int:
    best = streak = 1
    for a,b in pairwise(nums):
      streak = (streak if a == b + (1, -1)[streak % 2] else a == b - 1) + 1
      best = max(best, streak)
    return -1 if best == 1 else best