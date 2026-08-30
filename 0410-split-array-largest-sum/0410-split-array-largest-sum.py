class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(target_sum: int) -> bool:
            count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > target_sum:
                    count += 1
                    current_sum = num
                else:
                    current_sum += num
            return count <= k

        low, high = max(nums), sum(nums)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if canSplit(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans