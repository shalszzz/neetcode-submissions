class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap)>1:

            height=len(maxHeap)

            first_smash = -heapq.heappop(maxHeap)
            second_smash = -heapq.heappop(maxHeap)

            diff = abs(first_smash - second_smash)
            if diff:
                heapq.heappush(maxHeap, -diff)

        if len(maxHeap)==1:
            last = maxHeap.pop()
            return -last
        return 0
            

        