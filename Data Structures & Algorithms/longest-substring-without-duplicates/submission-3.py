class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        count=0

        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                count=max(count,len(seen))

            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
                seen.add(s[right])

        return(count)

        