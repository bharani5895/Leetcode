class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        
       
        def coin_count(n: int, current_amount: int) -> int:
            if current_amount == 0:
                return 1
            if n == 0:
                return 0
            if dp[n][current_amount] != -1:
                return dp[n][current_amount]
            
            if coins[n - 1] <= current_amount:
                take = coin_count(n, current_amount - coins[n - 1])
                not_take = coin_count(n - 1, current_amount)
                dp[n][current_amount] = take + not_take
            else:
                dp[n][current_amount] = coin_count(n - 1, current_amount)
                
            return dp[n][current_amount]

        return coin_count(len(coins), amount)