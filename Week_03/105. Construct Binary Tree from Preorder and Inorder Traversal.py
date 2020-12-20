# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            val = queue.popleft()
            root = TreeNode(val)
            index = index_map[val]
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)
            return root

        index_map = {val: idx for idx, val in enumerate(inorder)}
        queue = deque()
        for num in preorder:
            queue.append(num)
        return helper(0, len(inorder) - 1)