class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Map running_sum -> first occurrence index
        # Initialize with sum 0 at index -1 to handle prefix subarrays starting at index 0
        seen_sum = {0: -1}
        
        max_len = 0
        running_sum = 0
        
        for i, num in enumerate(nums):
            # Treat 0 as -1 and 1 as +1
            running_sum += 1 if num == 1 else -1
            
            if running_sum in seen_sum:
                # Calculate subarray length from first occurrence
                max_len = max(max_len, i - seen_sum[running_sum])
            else:
                # Store only the first time we see this sum to maximize distance
                seen_sum[running_sum] = i
                
        return max_len