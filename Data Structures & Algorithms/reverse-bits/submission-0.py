class Solution:
    def reverseBits(self, n: int) -> int:
        result=0

        for i in range(32):
            bit=(n&1) << (31-i)
            result |= bit
            n=n>>1
        return result

        