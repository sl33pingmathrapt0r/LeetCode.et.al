class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def valid(stringCount, wordCount):
            """
            Given the character frequency of a word and a string, 
            check that the string contains every character of the 
            word, including duplicates. 

            Returns a boolean. 
            """
            for x in wordCount:
                if stringCount.get(x,0)< wordCount[x]: return False
            
            return True

        m= len(s); n= len(t)
        if m<n: return ''
        
        tcount= {}
        for x in t: tcount[x]= tcount.get(x, 0)+1
        scount= {}
        for x in s: scount[x]= scount.get(x, 0)+1

        if not valid(scount, tcount): return ''

        scount= {}
        for i in range(n): scount[s[i]]= scount.get(s[i], 0)+1
        if tcount==scount: return s[:n]

        minlen= m
        start=0; end= n-1
        subs= [start, end]
        while end<m: 
            if valid(scount, tcount): 
                curlen= end-start
                if curlen<minlen: 
                    minlen= curlen
                    subs= [start,end+1]
                scount[s[start]]-=1
                start+=1
            else: 
                end+=1
                if end<m: scount[s[end]]= scount.get(s[end],0)+1
        
        return s[subs[0]:subs[1]]
