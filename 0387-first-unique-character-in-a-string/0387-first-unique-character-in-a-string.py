class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for x in s:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
            
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
                
        return -1