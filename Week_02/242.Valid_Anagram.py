class Solution:
    # sort
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # hashmap
    def isAnagram2(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for item in s:
            s_dict[item] = s_dict.get(item, 0) + 1

        for item in t:
            t_dict[item] = t_dict.get(item, 0) + 1
        return s_dict == t_dict