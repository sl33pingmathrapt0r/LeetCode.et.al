from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans= []
        for i in range(n+1):
            k= i
            ans.append(0)
            while k: 
                ans[-1]+= k&1
                k >>= 1
        return ans
