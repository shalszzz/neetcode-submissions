class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(left,right):
            if left==right:
                return nums[left]
            mid=left+(right-left)//2
            if nums[mid]>nums[right]:
                return search(mid+1,right)
            return search(left,mid)
        return search(0,len(nums)-1)
        
