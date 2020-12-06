'''
T = O(N), S = O(1)
Need to handle special test case: [0,0] -> [0,1]
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(len(digits)):
            idx = n - 1 - i
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits

        return [1] + digits