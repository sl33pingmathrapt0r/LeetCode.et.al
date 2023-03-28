class Solution:
    def getSum(self, a: int, b: int) -> int:
        # find the carry bits when adding 2 numbers
        # find the xor sum
        # add the xor sum to the carry bits (i.e. repeat algo)
        i= 31
        if not a: return b
        if not b: return a
        while b!= 0 and i:
            carry= a&b
            a= a^b
            b= carry<<1
            i-= 1

        if b: 
            # cut off extra carry-bits, MSB should be 0
            bits= []
            for _ in range(31):
                bits.insert(0, str(a&1))
                a>>=1
            a= int(''.join(bits), 2)

        return a
    
        # BETTER SOLUTIONS
    
        # 1. Set a MASK to only include 32-bits
        # mask = 0xFFFFFFFF
        # while b:
        #     a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # return a if a <= 0x7FFFFFFF else ~(a ^ mask)
        
        # 2. Put the numbers in power to exploit multiplication
        # if not a: return b
        # if not b: return a
        # return int(log(exp(a) * exp(b)))
