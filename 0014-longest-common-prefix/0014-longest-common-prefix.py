class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        
        re=""
        if not arr:
            return ""
        
        for i in range(len(arr[0])):
            first=arr[0][i]
            for j in range(1,len(arr)):
                if i>=len(arr[j]) or first != arr[j][i]:
                    return re
                    
                    
            re+=first
        
        return re
        