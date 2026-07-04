class Solution:
    def checkInclusion(self, s1: str, s2: str):
        def make_count(s):
            d = {}
            for ch in s:
                if ch not in d:
                    d[ch] = 1
                else:
                    d[ch] += 1
            return d

        d1 = make_count(s1)
        d = d1.copy()
        left = 0

        for right in range(len(s2)):

            #character not in s1 so reset 
            if s2[right] not in d1:
                d = d1.copy()
                left = right + 1
                continue

            d[s2[right]] -= 1

            while d[s2[right]] < 0:
                d[s2[left]] += 1
                left += 1

            #checking zero count
            if right - left + 1 == len(s1) and all(v == 0 for v in d.values()):
                return True

        return False