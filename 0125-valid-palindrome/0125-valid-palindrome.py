class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
      
        for c in s:
            if 'a' <= c <= 'z':
                filtered += c
            elif 'A' <= c <= 'Z':
                filtered += chr(ord(c) + 32)
          
            elif '0' <= c <= '9':
                filtered += c

        
        i = len(filtered) - 1
        reversed_string = ""

        while i >= 0:
            reversed_string += filtered[i]
            i -= 1

       
        return filtered == reversed_string