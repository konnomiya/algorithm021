class Solution:
    # iteration
    def postorder(self, root: 'Node') -> List[int]:
        stack, res = [root, ], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(node.children)
        return res[::-1]

    # recursive
    def postorder2(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res