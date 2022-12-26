from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Recursive solution

        # string= ''.join([x for x in s if x.isalnum()]).lower()
        # if len(string)==1 or len(string)==0: return True
        # if len(string)==2: return True if string[0]==string[-1] else False
        
        # return string[0]==string[-1] and Solution().isPalindrome(string[1:-1])

        string= ''.join([x for x in s if x.isalnum()]).lower()
        length= len(string)
        if length==1 or length==0: return True
        a= 0
        b= length-1
        while a<b:
            if string[a]!=string[b]: return False
            a+=1
            b-=1

        return True