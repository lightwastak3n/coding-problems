// Using recursion
var lowestCommonAncestor = function(root, p, q) {
    if (root.left && root.val > p.val && root.val > q.val) {
        return lowestCommonAncestor(root.left, p, q);
    }
    if (root.right && root.val < p.val && root.val < q.val) {
        return lowestCommonAncestor(root.right, p, q);
    }
    return root;
};

// Using iteration
var lowestCommonAncestor = function(root, p, q) {
    while (root) {
        if (root.val > p.val && root.val > q.val) {
            root = root.left;
        }
        else if (root.val < p.val && root.val < q.val) {
            root = root.right;
        }
        else {
            return root;
        }
    }
};

// Time complexity: O(n) for both
// Space complexity: O(1) for iteration, O(h) for the recursive stack
