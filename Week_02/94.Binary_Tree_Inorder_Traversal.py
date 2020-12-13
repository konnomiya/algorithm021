class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        if root is None:
            return

        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)

    # iteration
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                root = cur.right
        return res