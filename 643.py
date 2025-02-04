from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr=maxsum=sum(nums[:k])
        for i in range (k,len(nums)):
            curr+=nums[i]-nums[i-k]
            maxsum=max(maxsum,curr)
        return maxsum/k