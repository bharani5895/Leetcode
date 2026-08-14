class Solution:
    def compress(self, chars: List[str]) -> int:

        i=0
        write=0

        while i<len(chars):

            count=1
            j=i+1

           
            while j<len(chars) and chars[i]==chars[j]:
                count+=1
                j+=1

           
            chars[write]=chars[i]
            write+=1

            
            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1

            
            i=j

        return write