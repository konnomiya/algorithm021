class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) < 2:
            return True

        mapping = {}
        visited = []
        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]

            if ch_t not in mapping:
                if ch_s not in visited:
                    mapping[ch_t] = ch_s
                    visited.append(ch_s)
                else:
                    return False
            elif mapping[ch_t] != ch_s:
                return False
        return True
