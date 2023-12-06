class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        cache= [None] * (len(s)+1)
        cache[-1]= 1
        cache[-2]= 0 if s[-1]=='0' else 1

        # def helper(n):
        #     """
        #     Top-down DP with recursive helper
        #     """
        #     if cache[n]:
        #         return cache[n]

        #     if s[n] == '0':
        #         cache[n] = 0
        #         return 0

        #     if s[n]=='1' or (s[n]=='2' and s[n+1]<'7'):
        #         cache[n] = helper(n+1) + helper(n+2)
        #         return cache[n]

        #     cache[n] = helper(n+1)
        #     return cache[n]

        # bottom-up DP with for-loop
        for i in range(len(s)-2, -1, -1):
            if s[i]=='0':
                cache[i] = 0

            elif s[i]=='1' or (s[i]=='2' and s[i+1]<'7'):
                cache[i] = cache[i+1] + cache[i+2]

            else:
                cache[i] = cache[i+1]

        return cache[0]
