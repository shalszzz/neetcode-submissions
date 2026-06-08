class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=max(nums)
        res=0
        for i in nums:
            res=res^i
        for i in range(m+1):
            res=res^i
        if res==0 and 0 in nums:
            return m+1
        return res
        