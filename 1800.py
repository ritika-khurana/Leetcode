from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum=0

        for i in range(len(nums)):
            current_subarray_sum = nums[i]

            j=i+1
            while j<len(nums) and nums[j]>nums[j-1]:
                current_subarray_sum +=nums[j]
                j+=1
            max_sum = max(max_sum,current_subarray_sum)
        return max_sum    