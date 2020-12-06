# T = O(N)
# S = O(N)
# N = # of num in nums

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i in range(len(nums)):
            if target - nums[i] in num_to_idx:
                return [i, num_to_idx[target - nums[i]]]
            num_to_idx[nums[i]] = i