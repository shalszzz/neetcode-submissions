class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            try:
                j=nums[i+1: ].index(nums[i])+i+1

                if abs(i-j)<=k:
                    return True
            except ValueError:
                pass
        return False
        