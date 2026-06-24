import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        result=[]
        distances=[]
        for i,(x,y) in enumerate(points):
            dist=math.sqrt(math.pow(x,2)+ math.pow(y,2))
            distances.append([dist,i])

        heapq.heapify(distances)

        

        while k>0:

            minimum,idx=heapq.heappop(distances)
            result.append(points[idx])
            k-=1

        return result
            

        


            
        