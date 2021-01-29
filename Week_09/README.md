## Unique Path II
1. 确定状态，dp表示到达某坐标的方案总数
2. 状态转移方程：   
通过所有到达(i-1,j)这个点的路径往下走一步可到达(i,j), 这路径数总共有dp[i-1][j]条     
通过所有到达(i,j-1)这个点的路径往右走一步可到达(i,j), 这路径数总共有dp[i][-1j]条    
由此可以推出递推式dp[i][j] = dp[i-1][j]+dp[i][j-1]     
3. 处理边界条件，第一行和第一列的情况
4. 代码如下，不新开数组修改原数组的话，S = O(1)，用一维数组也可以做
```
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for col in range(n)] for row in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            else:
                dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                break
            else:
                dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

```
