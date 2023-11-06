class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache=[None]*46
        for i in range(3):
            cache[i]= i

        def helper(n):
            if isinstance(cache[n], type(None)):
                cache[n]= helper(n-1) + helper(n-2)

            return cache[n]

        return helper(n)
