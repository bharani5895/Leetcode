class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Step 1: Manually count vowels in the initial window s[0:k]
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
                
        max_vowel_count = current_vowels
        
        # Step 2: Slide the window across s from index k to end
        for i in range(k, len(s)):
            # Early exit: we cannot exceed a window of size k
            if max_vowel_count == k:
                return k
            
            # Add the new character entering on the right (s[i])
            if s[i] in vowels:
                current_vowels += 1
                
            # Remove the old character leaving on the left (s[i - k])
            if s[i - k] in vowels:
                current_vowels -= 1
                
            # Update overall max
            if current_vowels > max_vowel_count:
                max_vowel_count = current_vowels
            
        return max_vowel_count