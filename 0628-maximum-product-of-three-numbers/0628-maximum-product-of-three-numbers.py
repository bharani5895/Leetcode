class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        mini = float('inf')
        smin = float('inf')
        
        maxi = float('-inf')
        smax = float('-inf')
        tmax = float('-inf')
        
        for num in nums:
          
            if num <= mini:
                smin = mini
                mini = num
            elif num < smin:
                smin = num
                
          
            if num >= maxi:
                tmax = smax
                smax = maxi
                maxi = num
            elif num >= smax:
                tmax = smax
                smax = num
            elif num > tmax:
                tmax = num
        
        p1 = maxi * smax * tmax
        p2 = mini * smin * maxi
        
        return max(p1, p2)