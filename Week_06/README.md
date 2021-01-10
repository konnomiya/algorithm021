## 64. Minimum Path Sum
### 做题思路
1. Brute Froce: 自顶向下递归，对于每个元素来说，考虑向右或向下使整条路径和最小。T = O(2^(m+n)), S = O(m + n)
2. 用dp自顶向下，dp[i]定义为从左上角开始，以i位置为终点的最小和，这个和一定来自上方或左方的最小路径和 T=O(mn) S=O(mn) -> 如果修改原数据S=O(1)
3. 注意：面试的时候问清楚可不可以modify inputs
```
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = grid[i][j - 1]
                elif j == 0:
                    before = grid[i - 1][j]
                else:
                    before = min(grid[i - 1][j], grid[i][j - 1])
                grid[i][j] = grid[i][j] + before
        return grid[m - 1][n - 1]
```
## 91. Decode Ways
### 做题思路
1. 设定状态：dp[i] 表示字符串前i位有多少种解码方案
2. 若字符串中 s[i] 表示的阿拉伯数字在 1~9 范围内, dp[i] += dp[i-1]；若s[i-1]和s[i]连起来表示的数字在 10~26 范围内, dp[i] += dp[i-2] (若i==1, 则dp[i] += 1)
3. 边界：dp[0] = 1
4. 特殊处理：以’0‘开头，直接返回0，中途发现dp[i] == 0 也直接返回
```
class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == "0":
            return 0

        dp = [1, 1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != "0":
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i - 2: i]) == 10 or int(s[i - 2: i]) == 20:
                dp.append(dp[i - 2])
            elif s[i - 1] != "0":
                dp.append(dp[i - 1])
            else:
                return 0
        return dp[-1]

```
## 198. House Robber
### 做题思路
没记错的话貌似有道浇花题跟这一模一样...
优化思路都是，如果只用追踪前两个状态，就不必新开一个数组了，优化空间复杂度。
```
class Solution:
    def rob(self, nums: List[int]) -> int:
        cur_max = 0
        pre_max = 0
        for num in nums:
            temp = cur_max
            cur_max = max(cur_max, pre_max + num)
            pre_max = temp
        return cur_max

    def rob2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0] if len(nums) == 1 else 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
```
