class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()

        if amount == 0:
            return 0

        if coins[0] > amount:
            return -1

        while coins and coins[-1] > amount:
            coins.pop()

        cache = [None]*(amount+1)
        cache[0] = 0
        for i in range(1, coins[0]):
            cache[i] = -1

        for i in range(coins[0], amount+1):
            min = -1
            for coin in coins:
                sub = i - coin
                if sub<0:
                    break
                if cache[sub]>=0:
                    temp = cache[sub] + 1
                    min = temp if (temp<min or min==-1) else min
            cache[i] = min

        return cache[amount]
