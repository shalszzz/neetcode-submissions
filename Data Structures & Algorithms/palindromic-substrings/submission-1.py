class Solution:
    def countSubstrings(self, s: str) -> int:

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        ans = 0

        for start in range(len(s)):
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    ans += 1

        return ans