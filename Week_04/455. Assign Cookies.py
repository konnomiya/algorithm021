class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        sp = 0
        res = 0
        for gi in g:
            while sp < len(s) and s[sp] < gi:
                sp += 1
            if sp < len(s) and s[sp] >= gi:
                sp += 1
                res += 1
        return res