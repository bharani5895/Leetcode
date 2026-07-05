class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        
        temp=[]

        for i in range(len(nums)):
            if nums[i]!=0:
                temp.append(nums[i])
        
        for i in range(len(temp)):
            nums[i]=temp[i]

        n=len(temp)

        for i in range(n,len(nums)):
            nums[i]=0


        return nums

        