from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size= len(nums)
        nums.sort()
        result= set()
        for i in range(size-1):
            if i>0 and nums[i]==nums[i-1]: continue
            seen= set()
            for num in nums[i+1:]:
                if -numｓ[i] -num in seen:
                    result.add( (nums[i], num, -nums[i]-num) )
                seen.add(num)

        return [list(sol) for sol in result]