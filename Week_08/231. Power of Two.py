class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n != 0 and (n & -n) == n

    def isPowerOfTwo_1(self, n: int) -> bool:
        return n != 0 and n & (n - 1) == 0

    def isPowerOfTwo_2(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
