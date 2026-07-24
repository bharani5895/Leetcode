class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrom(sub:str) -> bool:
            return sub==sub[::-1]
            """i=0
            j=len(s)-1

            while(i<j):
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1

            return True"""
        
        
        i=0
        j=len(s)-1
        
        while(i<j):
            if s[i]!=s[j]:
                temp=s[:i]+s[i+1:]
                temp2=s[:j]+s[j+1:]

            
                return palindrom(temp) or palindrom(temp2)
                    
            i+=1
            j-=1
        
        return True