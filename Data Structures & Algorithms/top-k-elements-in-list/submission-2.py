class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {num: 0 for num in nums}
        

        for num in nums:
            myDict[num]+=1

        result=[]
        for i in range (k):
            high= max(myDict, key=myDict.get)
            result.append(high)
            myDict[high]=0

        return result

        
