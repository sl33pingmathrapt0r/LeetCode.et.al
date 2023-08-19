class Solution:
    def reverseBits(self, n: int) -> int:
        value= 0
        for i in range(32):
            value *= 2
            value += n%2
            n //= 2
        return value
    
    # or
    # def reverseBits(self, n: int) -> int:
    #     value= 0
    #     for i in range(32):
    #         value <<= 1
    #         value += n&1
    #         n >>= 1
    #     return value
