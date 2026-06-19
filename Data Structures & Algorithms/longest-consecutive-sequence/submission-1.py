class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        arr = sorted(set(nums))

        maxCount = 1
        count = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1] + 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 1

        maxCount = max(maxCount, count)
        return maxCount


        
        