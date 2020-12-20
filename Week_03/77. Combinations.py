class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(n, k, 1, [], res)
        return res

    def dfs(self, n, k, start, combination, res):
        if len(combination) == k:
            res.append(list(combination))
            return

        for i in range(start, n + 1):
            # if choices are less than what we need
            if n - i + 1 < k - len(combination):
                return
            combination.append(i)
            self.dfs(n, k, i + 1, combination, res)
            combination.pop()
