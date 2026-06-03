class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap=[-s for s in stones]
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap)>1:

            height=len(self.maxHeap)

            first_smash = -heapq.heappop(self.maxHeap)
            second_smash = -heapq.heappop(self.maxHeap)

            if first_smash>second_smash:
                heapq.heappush(self.maxHeap, -(first_smash-second_smash))
            elif second_smash>first_smash:
                heapq.heappush(self.maxHeap, -(second_smash-first_smash))

        if len(self.maxHeap)==1:
            last = self.maxHeap.pop()
            if last>0:
                return last
            return -last
        return 0
            

        