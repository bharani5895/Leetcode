class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dis=float('inf')
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            
            while l<r:
                total=nums[i]+nums[l]+nums[r]

                if total==target:
                    return total
                if abs(dis-target)>abs(total-target):
                     dis=total
                
                
                if total <target:
                    l+=1
                else:
                    r-=1

        return dis