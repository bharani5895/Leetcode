class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=nums[0]
        min_product=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):

            x=nums[i]

            oldmax=max_product
            oldmin=min_product

            max_product=max(x,max(oldmax*x,oldmin*x))
            min_product=min(x,min(oldmax*x,oldmin*x))

            result=max(result,max_product)
        return result