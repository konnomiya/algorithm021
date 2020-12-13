import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set([1])
        factors = [2, 3, 5]

        val = None
        for _ in range(n):
            val = heapq.heappop(heap)
            for factor in factors:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(heap, val * factor)
        return val