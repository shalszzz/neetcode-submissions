class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=left+1


        while right<len(nums) and nums[right]>nums[left]:
            left=right
            right+=1

        if right==len(nums):
            return nums[0]
        
        return nums[right]

            
