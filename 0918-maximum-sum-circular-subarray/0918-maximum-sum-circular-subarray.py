class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currsum=nums[0]
        maxsum=nums[0]
        currmin=nums[0]
        minsum=nums[0]
        totalsum=nums[0]
        for i in range(1,len(nums)):
            totalsum+=nums[i]
            currsum=max(nums[i],nums[i]+currsum)
            maxsum=max(maxsum,currsum)
            currmin=min(nums[i],nums[i]+currmin)
            minsum=min(minsum,currmin)

        
        if maxsum<0:
            return maxsum

        circular=totalsum-minsum

        return max(circular,maxsum)

        


        