class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n

        for i in range (n):
            dp[i]=max(nums[i],nums[i]+ dp[i-1])

        return max(dp)

            