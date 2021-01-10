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