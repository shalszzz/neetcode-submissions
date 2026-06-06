class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[n for n in nums]
        postfix=[n for n in nums]
        for i in range(1,len(nums)):
            prefix[i]*=prefix[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i]*=postfix[i+1]

        result=[postfix[1]]
        for i in range(1,len(nums)):
            if i==len(nums)-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1]*postfix[i+1])
        return result

        