class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iteration
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root, ], []
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        if root is None:
            return

        res.append(root.val)
        self.traverse(root.left, res)