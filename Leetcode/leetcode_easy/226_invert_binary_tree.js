var invertTree = function(root) {
    if (root) {
        [root.left, root.right] = [root.right, root.left];
        invertTree(root.left);
        invertTree(root.right);
    }
    return root;
};
// Pretty straightforward, go through a tree and swap left and right
// Time complexity: O(n)
// Space complexity: O(1)

// Same but shorter. Maybe it's just me but I find this way less readable.
var invertTree = function(root) {
    if (root) {
        [root.left, root.right] = [invertTree(root.right), invertTree(root.left)];
    }
    return root;
};