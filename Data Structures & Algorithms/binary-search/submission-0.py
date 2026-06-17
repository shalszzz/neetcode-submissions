class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left=0
        right=len(nums)-1

        found=-1

        def binary_search(left,right,target):

            nonlocal found

            if left>right:
                return -1

            mid = left+ (right-left)//2
            if nums[mid]==target:
                found=mid
                return
            elif nums[mid]<target:
                binary_search(mid+1,right,target)
            else:
                binary_search(left,mid-1,target)

        binary_search(left,right,target)
        return found
            
        