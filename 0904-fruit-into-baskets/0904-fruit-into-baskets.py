class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            # Add the current fruit to our window count
            count[fruits[right]] = count.get(fruits[right], 0) + 1
            
            # If we exceed 2 distinct types, shrink window from left
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            
            # Update the max window size found so far
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits