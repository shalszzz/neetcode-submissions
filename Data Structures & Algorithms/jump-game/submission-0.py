class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        dp = [0] * n
        dp[n - 1] = 1

        for i in range(n - 2, -1, -1):

            for jump in range(1, nums[i] + 1):

                if i + jump < n and dp[i + jump] == 1:
                    dp[i] = 1
                    break

        return dp[0] == 1