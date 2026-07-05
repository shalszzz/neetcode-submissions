class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def bin_search(left,right):
            if left>right:
                return -1
            
            mid=left+(right-left)//2
            if target==nums[mid]:
                return mid
            if nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    return bin_search(left,mid-1)
                else:
                    return bin_search(mid+1,right)
            else:
                if nums[mid]<target<=nums[right]:
                    return bin_search(mid+1,right)
                else:
                    return bin_search(left,mid-1)

            
            
        return bin_search(0,len(nums)-1)

            




        