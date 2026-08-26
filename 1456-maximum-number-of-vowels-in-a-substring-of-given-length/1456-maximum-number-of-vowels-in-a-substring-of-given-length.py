class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"  # String is slightly faster than set for 5 chars
        current_vowels = 0
        
        # 1. Count vowels in the very first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
                
        max_vowels = current_vowels
        
        # Early exit check for the first window
        if max_vowels == k:
            return k
            
        # 2. Slide the window
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_vowels -= 1
                
            if s[i] in vowels:
                current_vowels += 1
                
            # Replacing max() with an if statement for speed
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                # Early exit check inside the loop
                if max_vowels == k:
                    return k
                    
        return max_vowels