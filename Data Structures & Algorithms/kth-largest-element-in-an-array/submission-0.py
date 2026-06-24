class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        mynums= [-n for n in nums]
        
        heapq.heapify(mynums)

        while k>1:
            heapq.heappop(mynums)
            k-=1

        answer=-heapq.heappop(mynums)
        return answer
        

        