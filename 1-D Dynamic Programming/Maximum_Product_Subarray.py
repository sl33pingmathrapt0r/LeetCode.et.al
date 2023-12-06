class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Using Kadane's algo for linearly
        traversing array with constant
        cache for current vs global max.
        """
        if not nums:
            return 0

        # min could be -ve with large absolute val
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        max_so_far = nums[0]

        for num in nums[1:]:
            max_ending_here, min_ending_here =\
                max(num, max_ending_here*num, min_ending_here*num),\
                min(num, max_ending_here*num, min_ending_here*num)

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

        return max_so_far
