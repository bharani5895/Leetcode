class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        def count_days(capacity: int) -> int:
            needed_days = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > capacity:
                    needed_days += 1
                    current_weight = w
                else:
                    current_weight += w
            return needed_days

        while low < high:
            mid = (low + high) // 2
            if count_days(mid) <= days:
                high = mid  # Try finding a smaller valid capacity
            else:
                low = mid + 1  # Capacity too small, increase it
                
        return low