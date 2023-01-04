var preorder = function(root) {
    function dfs(node, values) {
        if (!node) {
            return;
        }
        values.push(node.val);
        for (child of node.children) {
            dfs(child, values);
        }
    }
    let values = [];
    dfs(root, values);
    return values;
};

// Time: O(n)
// Space: O(n)