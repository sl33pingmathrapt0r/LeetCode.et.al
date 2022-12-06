from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]: return 0
        nums= sorted([*set(nums)])
        max=0
        consec=1
        for i in range(len(nums)-1):
            if nums[i]+1== nums[i+1]: consec+=1
            else: 
                max= consec if consec>max else max
                consec=1

        return max if max>consec else consec