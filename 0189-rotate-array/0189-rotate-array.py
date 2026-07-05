class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        nums.reverse()
        for i in range(k//2):
            nums[i],nums[k-1-i]=nums[k-1-i],nums[i]

        remain=n-k
        for i in range(remain//2):
            nums[k+i],nums[n-1-i]=nums[n-1-i],nums[k+i]
            

        return nums