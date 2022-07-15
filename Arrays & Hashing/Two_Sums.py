from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numD={}
#         for i in range(len(nums)):
#             if target-nums[i] in numD:
#                 return[numD[target-nums[i]], i]
#             else: numD[nums[i]]=i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num= set(nums)
        for i in range(len(nums)-1):
            if (target-nums[i] in num): 
                for j in range(i+1, len(nums)): 
                    if nums[j]==target-nums[i]: 
                        return [i, j]
    