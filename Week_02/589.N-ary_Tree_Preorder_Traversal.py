class Solution:
    # iteration
    def preorder(self, root: 'Node') -> List[int]:
        stack, res = [root,], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(node.children[::-1])
        return res

    # recursive
    def preorder2(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        res.append(root.val)
        for child in root.children:
            res.extend(self.preorder(child))
        return res