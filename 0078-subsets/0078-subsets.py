class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ar=[]
        n=len(nums)
        for k in range(pow(2,n)):
            temp=[]
            for i in range(n):
                if k &(1<<(i)) !=0:
                    temp.append(nums[i])
            
            ar.append(temp)
        
        return ar