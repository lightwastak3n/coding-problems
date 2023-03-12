var diameterOfBinaryTree = function(root) {
    let diameter = 0;
    function dfsHeight(root) {
        if (!root) {
            return 0;
        }
        let leftSubtree = dfsHeight(root.left);
        let rightSubtree = dfsHeight(root.right);
        diameter = Math.max(diameter, leftSubtree + rightSubtree);
        return 1 + Math.max(leftSubtree, rightSubtree);
    }
    dfsHeight(root);
    return diameter;
};

// Time complexity: O(n) - visiting each node once
// Space complexity: O(n) - recursive call stack
