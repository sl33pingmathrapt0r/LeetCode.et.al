from typing import List
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod= lambda arr: (1 if len(arr)<1 else reduce(lambda a,b: a*b, arr))
        if 0 in nums: 
            return [0 if nums[i]!=0 else prod(nums[:i])*prod(nums[i+1:]) for i in range(len(nums))]
        else:
            total= prod(nums)
            return [total//nums[i] for i in range(len(nums))]