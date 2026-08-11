class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            c=c^nums[i]
        return c
            
                