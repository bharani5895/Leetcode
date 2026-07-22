class Solution:
    def findPairs(self, arr: List[int], x: int) -> int:
        arr.sort()
        i=0
        j=1
        count=0
        while(j<len(arr)):
            
            if(i==j):
                j+=1
                continue
            
            diff=arr[j]-arr[i]
            
            if(diff == x):
                count+=1
                a=arr[i]
                b=arr[j]
                while(i<len(arr) and arr[i]==a):
                    i+=1
                while(j<len(arr) and arr[j]==b):
                    j+=1
                continue

            
            if(diff<x):
                j+=1
            else:
                i+=1
                
        return count