class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float('inf')

        # Expand the window using the right pointer
        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink the window from the left while the sum condition is satisfied
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        # Return min_len if a valid window was found, otherwise 0
        return min_len if min_len != float('inf') else 0