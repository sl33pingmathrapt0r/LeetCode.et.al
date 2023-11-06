class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return s

        n= len(s)
        if n==1:
            return 1
        if n==2:
            return 3 if s[0]==s[1] else 2

        def expand(*args):
            if len(args)==1:
                i=j=args[0]
            else:
                i,j= args

            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            return (j-i)//2

        count= 0
        for i in range(n):
            odd= expand(i)
            even= expand(i-1,i)

            count+= odd + even

        return count
