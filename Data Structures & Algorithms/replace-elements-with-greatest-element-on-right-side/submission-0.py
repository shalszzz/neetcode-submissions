class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result=[]
        for i in range(len(arr)):
            if i==len(arr)-1:
                result.append(-1)
            else:
                curr_max=max(arr[i+1:])
                result.append(curr_max)
        return result