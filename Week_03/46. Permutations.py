class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        permutation = []
        self.dfs(nums, permutation, results)
        return results

    def dfs(self, nums, permutation, results):
        if len(permutation) == len(nums):
            results.append(list(permutation))
            return

        for num in nums:
            if num not in permutation:
                permutation.append(num)
                self.dfs(nums, permutation, results)
                permutation.pop()