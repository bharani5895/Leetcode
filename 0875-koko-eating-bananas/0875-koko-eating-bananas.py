class Solution:
    def minEatingSpeed(self, piles: List[int], k: int) -> int:
        def checkans(arr,k,s):
        
            time=0
            for i in arr:
                if i%s !=0:
                    time+= (i//s)+1

                else:
                    time+=i//s


            return time<=k

        
        max_=float('-inf')
        for i in piles:
            if i>max_:
                max_=i

        
        l=1
        r=max_
        ans=float('inf')
        while(l<=r):
            mid=(l+r)//2
            if checkans(piles,k,mid):
                ans=min(ans,mid)
                r=mid-1

            else:
                l=mid+1

        
        return ans

            