class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        permutation = []
        visited = [False] * len(nums)
        results = []
        self.dfs(nums, permutation, results, visited)
        return results

    def dfs(self, nums, permutation, results, visited):
        if len(permutation) == len(nums):
            results.append(list(permutation))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, permutation, results, visited)
            visited[i] = False
            permutation.pop()