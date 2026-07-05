class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        counts={}
        
        for ch in tasks:
            if ch not in counts:
                counts[ch]=1
            else:
                counts[ch]+=1
        myheap=[-v for v in counts.values()]
        heapq.heapify(myheap)
        time=0
        q=deque()
        while myheap or q:
            
            if q and q[0][1]==time:
                x,y=q.popleft()
                heapq.heappush(myheap,x)

            if myheap:
                top=heapq.heappop(myheap)
                top+=1
                if top!=0:
                    q.append((top,time+n+1))

            
            time+=1
        
        return time

            


        