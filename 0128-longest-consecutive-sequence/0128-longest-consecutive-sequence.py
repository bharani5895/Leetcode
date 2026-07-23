class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashh={}

        for i in nums:
            hashh[i]=True
        
        max_=0
        for i in hashh:

            if i-1 not in hashh:
                temp=1
                n=i
                while(n+1 in hashh):
                    n+=1
                    temp+=1
                max_=max(max_,temp)
        return max_

            


