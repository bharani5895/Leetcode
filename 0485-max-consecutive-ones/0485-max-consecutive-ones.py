class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_cont=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                if count> max_cont:
                    max_cont=count
            else:
                count=0
    
        return max_cont

            
