class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        vals, found = [], []
        if root:
            found.append(root)
        while found:
            new_nodes, level = [], []
            for node in found:
                level.append(node.val)
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            vals.append(level)
            found = new_nodes
        return vals

# Time complexity: O(n) - we visit each node once
# Space complexity: O(n) - storing n values in vals and at most n elements in found