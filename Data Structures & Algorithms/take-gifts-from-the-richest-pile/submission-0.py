import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        myheap=[-n for n in gifts]
        heapq.heapify(myheap)

        while k>0:
            top = -heapq.heappop(myheap)
            heapq.heappush(myheap,-int(math.sqrt(top)))
            k-=1
        result=0
        for num in myheap:
            result+=num
        return -result
        