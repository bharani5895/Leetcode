class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_len=float("inf")
        i=0
        for s in strs:
            if len(s)<min_len:
                min_len=len(s)
        
        while i < min_len:
            for s in strs:
                if s[i] !=strs[0][i]:
                    return s[:i]
            i+=1
        return strs[0][:i]