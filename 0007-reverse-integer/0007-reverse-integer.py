class Solution:
    def reverse(self, x: int) -> int:
        min_val=-21477483648
        max_val=2147483647

        sign =1 if x>=0 else -1

        x=x*sign

        rev=0

        while x!=0:
            dig=x%10
            rev =rev *10+dig
            x=x//10
        
        if(rev>max_val or rev <min_val):
            return 0
        return rev *sign