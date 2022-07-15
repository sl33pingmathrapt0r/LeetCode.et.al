from typing import List

class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has= {}
        for x in strs: 
            cha= [0]*26
            for l in x:
                cha[ord(l)-97]+=1
            cha= tuple(cha)
            if cha in has: has[cha]+= [x]
            else: has[cha]= [x]
        return list(has.values())