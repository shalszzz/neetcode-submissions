class Solution:
    def trap(self, height: List[int]) -> int:
        trapped=0
        
        left=0
        right=len(height)-1
        maxL=height[left]
        maxR=height[right]

        while left<right:
            if maxL<=maxR:
                left+=1

                if(maxL-height[left])>0:
                    trapped+=(maxL-height[left])
                maxL=max(maxL,height[left])

            else:
                right-=1
                if(maxR-height[right])>0:
                    trapped+=(maxR-height[right])
                maxR=max(maxR,height[right])

        return trapped

            