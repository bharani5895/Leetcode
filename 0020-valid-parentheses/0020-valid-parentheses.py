class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        for i in range(len(s)):
            c=s[i]
            if c=="{" or c=="(" or c=="[":
                stack.append(c)
            elif not stack:
                return False
            elif (c==")" and stack[-1]=="(") or \
                 (c=="}" and stack[-1]=="{") or \
                 (c=="]" and stack[-1]=="["):
                stack.pop()
            else:
                return False
                
        return len(stack)==0