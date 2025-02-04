from typing import List
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        min_sum = float('inf')
        
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                subarray_sum = prefix[i + length] - prefix[i]
                if subarray_sum > 0:
                    min_sum = min(min_sum, subarray_sum)
    
        return min_sum if min_sum != float('inf') else -1