class Solution:
    def hammingWeight(self, n: int) -> int:
        wt= 0
        while n: 
            wt+= n%2
            n//=2
        return wt
    
    # or
    # def hammingWeight(self, n: int) -> int:
    #     wt= 0
    #     while n: 
    #         wt+= n & 1
    #         n >>= 1
    #     return wt
