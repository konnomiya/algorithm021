'''
T = O(N), S = O(1)
Question: which method is better?
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i + 1

    def removeDuplicates2(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N
        slow, fast = 0, 1
        while fast < N:
            while fast < N and nums[slow] == nums[fast]:
                fast += 1
            slow += 1
            if fast < N:
                nums[slow] = nums[fast]
        return slow


