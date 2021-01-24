class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            n -= (n & -n)
            ans += 1
        return ans
