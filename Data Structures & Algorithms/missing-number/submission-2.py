class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mynums=sorted(nums)
        for i in range(len(nums)):
            if i!=mynums[i]:
                return i
        return i+1
        