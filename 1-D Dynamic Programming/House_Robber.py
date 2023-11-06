class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cache=[None]* n

        def helper(x):
            if x<0:
                return 0
            if isinstance(cache[x], type(None)):
                cache[x]= max(
                    nums[x] + helper(x-2),
                    helper(x-1)
                )
            
            return cache[x]

        return helper(n-1)
