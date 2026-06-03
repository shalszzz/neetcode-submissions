class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        combos=[]

        def dfs(i,sum):

            if i>=len(nums) or sum>target:
                return

            if sum==target:
                result.append(combos.copy())
                return 

            combos.append(nums[i])
            dfs(i, sum+nums[i])

                  
            combos.pop()
            dfs(i+1,sum)

        dfs(0,0)
        return result
            


        