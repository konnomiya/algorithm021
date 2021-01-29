class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        string = list(s)
        for i in range(0, len(string), 2 * k):
            string[i:i + k] = reversed(string[i:i + k])
        return "".join(string)