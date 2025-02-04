from typing import List
from typing import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)
        
        ans = 1
        
        for left in range(len(nums)):
            p = nums[left]
            g = nums[left]
            l = nums[left]
            for right in range(left + 1, len(nums)):
                p *= nums[right]
                g = math.gcd(g, nums[right])
                l = lcm(l, nums[right])
                if p == (g * l):
                    ans = max(ans, right - left + 1)
        
        return ans
                