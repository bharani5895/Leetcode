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



















       