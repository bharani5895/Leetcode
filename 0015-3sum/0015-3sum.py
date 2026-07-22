class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        result=[]

        if len(arr)<3:
            return[]
        
        for i in range(len(arr)-2):
            if i>0 and arr[i]==arr[i-1]:
                continue
            
            j=i+1
            k=len(arr)-1

            while j<k:
                sum_=arr[i]+arr[j]+arr[k]

                if sum_==0:
                    result.append([arr[i],arr[j],arr[k]])
                    j+=1
                    k-=1
                    
                    while j<k and arr[j]==arr[j-1]:
                        j+=1
                    while j<k and arr[k]==arr[k+1]:
                        k-=1
                elif sum_<0:
                    j+=1
                    
                else:
                    k-=1
                    
        return result



















        """for i in range(0,len(nums)-2):
            if nums[i]==nums[i-1] and i>0:
                continue
           
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s==0:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    while nums[r]==nums[r+1] and l<r:
                        r-=1
                elif s<0:
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif s>0:
                    r-=1
                    while nums[r]==nums[r+1] and l<r:
                        r-=1
        return result         """