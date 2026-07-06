class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_prd=nums[0]
        min_prd=nums[0]
        ans=nums[0]

        for i in range(1,len(nums)):
            if nums[i]<0:
                max_prd,min_prd=min_prd,max_prd
            max_prd=max(nums[i],max_prd*nums[i])
            min_prd=min(nums[i],min_prd*nums[i])
            ans=max(ans,max_prd)
        return ans



        