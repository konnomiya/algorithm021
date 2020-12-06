class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        T = O(KN) S = O(1)
        """
        k %= len(nums)
        for i in range(k):
            tail = nums[-1]
            for j in range(len(nums)):
                nums[j], tail = tail, nums[j]

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        T = O(N), S = O(N)
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        T = O(N), S = O(1)
        """
        N = len(nums)
        k %= N
        self.reverse(0, N - 1, nums)
        self.reverse(0, k - 1, nums)
        self.reverse(k, N - 1, nums)

    def reverse(self, start, end, s):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

