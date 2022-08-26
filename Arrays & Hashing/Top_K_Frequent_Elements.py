from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elem= [*set(nums)]
        elem.sort(reverse= True, key= lambda x : nums.count(x))
        return [elem[i] for i in elem]