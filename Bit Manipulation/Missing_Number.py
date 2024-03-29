from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen= [0]*(len(nums)+1)
        for x in nums: seen[x]=1
        return seen.index(0)
    
    # or
    # def missingNumber(self, nums: List[int]) -> int:
    #     n= len(nums)
    #     max= n*(n+1)//2
    #     return max-sum(nums)
