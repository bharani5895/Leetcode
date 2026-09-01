"""class Solution:
    def mincoins(self,coins,amount,n,dp):
        if amount==0:
            return 0
        if n==0:
            return float('inf')-1

        if coins[n-1]<=amount:
            take=1+self.mincoins(coins,amount-coins[n-1],n,dp)
            nottake=self.mincoins(coins,amount,n-1,dp)
            return min(take,nottake)
        else:
            return self.mincoins(coins,amount,n-1)
            
    def coinChange(self, coins: List[int], amount: int) -> int:
        k=self.mincoins(coins,amount,len(coins))
        if k==float('inf')-1:
            return -1

        return k"""


class Solution:
    def mincoins(self, coins: List[int], amount: int, n: int, dp: List[List[int]]) -> int:

        if amount == 0:
            return 0
        if n == 0:
            return float('inf') - 1

        if dp[n][amount] != -1:
            return dp[n][amount]

        if coins[n - 1] <= amount:
            take = 1 + self.mincoins(coins, amount - coins[n - 1], n, dp)
            nottake = self.mincoins(coins, amount, n - 1, dp)
            dp[n][amount] = min(take, nottake)
        else:
            dp[n][amount] = self.mincoins(coins, amount, n - 1, dp)

        return dp[n][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
      
        dp = [[-1] * (amount + 1) for _ in range(n + 1)]

        k = self.mincoins(coins, amount, n, dp)
        return -1 if k >= float('inf') - 1 else k
        

        