class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def letter_count(s):
            lc={}
            for ch in s:
                if ch not in lc:
                    lc[ch]=1
                else:
                    lc[ch]+=1
            return lc
            
        lc_1=letter_count(s)
        lc_2=letter_count(t)

        if lc_1 == lc_2:
            return True
        return False



        