class Solution(object):
    def sortColors(self, nums):
        c1=0
        c2=0
        c3=0
        for i in range(len(nums)):
            if nums[i]==0:
                c1+=1
            elif nums[i]==1:
                c2+=1
            else:
                c3+=1
        for i in range(c1):
            nums[i]=0
        for j in range(c1,c1+c2):
            nums[j]=1
        for k in range(c1+c2,len(nums)):
            nums[k]=2
        return nums