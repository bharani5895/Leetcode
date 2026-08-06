class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=0
        maxright=0
        water=0
        l=0
        r=len(height)-1

        while l<r:

            if height[l]<=height[r]:
                if height[l]<maxleft:
                    water+=maxleft-height[l]

                else:
                    maxleft=height[l]
                l+=1

            else:
                if height[r]<=maxright:
                    water+=maxright-height[r]

                else:
                    maxright=height[r]
                r-=1
        
        return water