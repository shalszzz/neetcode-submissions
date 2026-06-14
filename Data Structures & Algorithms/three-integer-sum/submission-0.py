class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums=sorted(nums)
        seen=[]

        for i in range (len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])

                first=i+1
                second=len(nums)-1

                while first<second:

                    som=nums[first]+nums[second]+nums[i]

                    if som==0:
                        triplet=[nums[i],nums[first],nums[second]]

                        if triplet not in result:
                            result.append(triplet)
                        first+=1
                        second-=1

                    elif som<0:
                        first+=1
                    else:
                        second-=1
        return result



        
        