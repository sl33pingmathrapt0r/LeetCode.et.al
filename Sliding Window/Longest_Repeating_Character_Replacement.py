class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # if there are k+1 char, then replace k char will guarantee all same char
        if k+1>=len(s): return len(s)
        
        maxlen= k+1
        count={}
        for i in range(k+2): count[s[i]]= count.get(s[i],0) +1

        start= 0; end= k+1
        while end<len(s):
            curlen= end-start+1
            if (curlen) - max(count.values()) <= k: 
                maxlen= curlen if curlen>maxlen else maxlen
                end+=1
                if end<len(s): count[s[end]]= count.get(s[end],0) +1
            else: 
                count[s[start]]-= 1
                start+=1
        
        return maxlen
      
