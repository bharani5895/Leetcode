class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Map stores remainder -> earliest index where it occurred
        # Initialize remainder 0 at index -1 to handle subarrays starting from index 0
        remainder_map = {0: -1}
        running_sum = 0
        
        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k
            
            # If the remainder was seen before, check if the subarray length >= 2
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Only store the earliest index of a remainder to maximize subarray length
                remainder_map[remainder] = i
                
        return False