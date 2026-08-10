class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_element=nums[0]
        max_check=nums[0]
        for i in range(1,len(nums)):
            max_element=max(nums[i],nums[i]+max_element)
            max_check=max(max_check,max_element)
        

        return max_check