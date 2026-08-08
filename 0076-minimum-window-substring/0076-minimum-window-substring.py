from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        l = 0

        min_len = float('inf')
        start = 0

        for r in range(len(s)):

            
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

           
            if ch in need and window[ch] == need[ch]:
                have += 1

        
            while have == need_count:

                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                left_ch = s[l]
                window[left_ch] -= 1

            
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                l += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]