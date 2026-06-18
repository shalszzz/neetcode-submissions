class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mynums=set()

        for i in nums:
            if i not in mynums:
                mynums.add(i)
            else:
                return True
        return False
        