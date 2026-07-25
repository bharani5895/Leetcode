class Solution:
    def search(self, arr: List[int], k: int) -> int:
        i=0
        j=len(arr)-1
        
        while(i<=j):
            mid=(i+j)//2
            
            if(arr[mid] == k):
                return mid
                
            elif arr[mid]>k:
                j=mid-1
                
            else:
                i=mid+1
                
        return -1