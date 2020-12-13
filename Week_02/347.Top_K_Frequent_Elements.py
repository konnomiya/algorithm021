from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums).items()
        for num, freq in count:
            bucket[freq].append(num)
        res = []
        for sublist in bucket:
            for num in sublist:
                res.append(num)
        return res[::-1][:k]