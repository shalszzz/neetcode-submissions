class Solution:
    def reorganizeString(self, s: str) -> str:

        final=""
        
        if not s:
            return final
        counts={}
        
        for ch in s:
            if ch not in counts:
                counts[ch]=1
            else:
                counts[ch]+=1
        
        heap=[]
        for ch in counts:
            heapq.heappush(heap,(-counts[ch],ch))

        result=[]
        prevcount=0
        prev_char=""

        while heap:

            val, char=heapq.heappop(heap)
            val+=1

            result.append(char)

            if prevcount<0:
                heapq.heappush(heap,(prevcount,prev_char))

            prevcount=val
            prev_char=char


        if len(result)<len(s):
                return ""
        return "".join(result)


        

            


        
        
        