class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)

        numsStart= nums[:-1] + [0]
        numsEnd= [0] + nums[1:]
        cacheStart= [None]*n
        cacheEnd= [None]*n
        
        def helper(start, x):
            if x<0:
                return 0

            if start:
                if isinstance(cacheStart[x], type(None)):
                    cacheStart[x]= max(
                        numsStart[x] + helper(start, x-2),
                        helper(start, x-1)
                    )
            
                return cacheStart[x]

            else:
                if isinstance(cacheEnd[x], type(None)):
                    cacheEnd[x]= max(
                        numsEnd[x] + helper(start, x-2),
                        helper(start, x-1)
                    )
            
                return cacheEnd[x]

        return max(
            helper(True, n-1),
            helper(False, n-1)
        )
