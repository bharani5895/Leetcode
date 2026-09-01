"""class Solution:
    def checksubset(self,arr,n,target,dp):

        if target==0:
            return True
        if n==0:
            return False
        nottake=self.checksubset(arr,n-1,target)
        if arr[n-1]<=target:
            take=self.checksubset(arr,n-1,target-arr[n-1])
            return take or nottake

        

    def canPartition(self, nums: List[int]) -> bool:
        
        sums=sum(nums)
        n=len(nums)
        
        
        if sums%2 !=0 :
            return False
        else:
            target=sums//2
            return self.checksubset(nums,n,target)"""

class Solution:
    def checksubset(self, arr: List[int], n: int, target: int, dp: list) -> bool:
        if target == 0:
            return True
        if n == 0:
            return False
            
        # Return memoized result if already computed
        if dp[n][target] != -1:
            return dp[n][target]

        if arr[n - 1] <= target:
            take = self.checksubset(arr, n - 1, target - arr[n - 1], dp)
            nottake = self.checksubset(arr, n - 1, target, dp)
            dp[n][target] = take or nottake
        else:
            dp[n][target] = self.checksubset(arr, n - 1, target, dp)

        return dp[n][target]

    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        n = len(nums)

        if sums % 2 != 0:
            return False
            
        target = sums // 2
        # Initialize a 2D DP table with -1 (size: (n + 1) x (target + 1))
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        
        return self.checksubset(nums, n, target, dp)