class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n  
        
        i = 0
        j = n - 1
        k = n - 1  
        
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                res[k] = nums[j] * nums[j]
                j -= 1
            else:
                res[k] = nums[i] * nums[i]
                i += 1
            k -= 1  
            
        return res