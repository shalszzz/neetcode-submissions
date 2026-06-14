class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        first = 0
        
        for i in range (len(nums)-1):

            first=i
            second=first+1

            while second<len(nums):
                add=nums[first]+nums[second]

                if add==target:
                    return [first,second]
                
                second+=1