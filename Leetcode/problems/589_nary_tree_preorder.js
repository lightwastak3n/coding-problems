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

// Iterative approach
var preorder = function(root) {
    if (!root) {
        return [];
    }
    let stack = [root];
    let vals = [];
    while (stack.length) {
        let current = stack.pop();
        vals.push(current.val);
        stack = stack.concat(current.children.reverse());
    }
    return vals;
};

// Same complexity
// Time: O(n) - one loop for each node when we take it out of stack
// Space: O(n) - we are just moving elements from stack to vals so combined they have at most n elements
