class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s)<len(p):
            return []
            
        p_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        k = len(p)

        window = [0] * 26

        for i in range(k):
            window[ord(s[i]) - ord('a')] += 1

        ans = []
        left = 0

        if window == p_count:
            ans.append(0)

        while left + k < len(s):
        
            window[ord(s[left]) - ord('a')] -= 1

            window[ord(s[left + k]) - ord('a')] += 1

            left += 1

            if window == p_count:
                ans.append(left)

        return ans