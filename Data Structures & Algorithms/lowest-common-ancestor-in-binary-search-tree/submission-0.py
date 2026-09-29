from collections import defaultdict, deque

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # path from root (inclusive) down to each node
        d = {root.val: [root]}
        queue = deque([root])

        while queue:
            node = queue.popleft()
            path = d[node.val]
            if node.left:
                d[node.left.val] = path + [node.left]
                queue.append(node.left)
            if node.right:
                d[node.right.val] = path + [node.right]
                queue.append(node.right)

        a, b = d[p.val], d[q.val]
        lca = None
        for x, y in zip(a, b):
            if x is y:
                lca = x
            else:
                break
        return lca