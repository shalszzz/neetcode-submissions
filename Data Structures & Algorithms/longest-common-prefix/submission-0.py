class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        left=""
        minlen=min(len(word)for word in strs)

        while len(left)<minlen:

            left=strs[0][:len(left)+1]
            for word in strs:
                if word[:len(left)]!=left:
                    return word[:len(left)-1]
        return left 