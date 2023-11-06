class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        n= len(s)
        if n==1:
            return s
        if n==2:
            return s if s[0]==s[1] else s[0]

        def expand(*args):
            if len(args)==1:
                i=j=args[0]
            else:
                i,j= args

            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]

        longest= s[0]
        for i in range(1,n):
            odd= expand(i)
            even= expand(i-1,i)

            longest= max(longest, odd, even, key=len)

        return longest
