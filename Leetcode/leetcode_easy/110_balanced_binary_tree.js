var isBalanced = function(root) {
    function getHeight(root) {
	    if (!root) {
		    return 0;
		}
	    let leftHeight = getHeight(root.left);
	    let rightHeight = getHeight(root.right);
        if (leftHeight == -1 || rightHeight == -1 || Math.abs(rightHeight - leftHeight) > 1) {
            return -1;
        }
		return Math.max(leftHeight, rightHeight) + 1;		
    }
    return getHeight(root) != -1; 
};

// getHeight recursively traverses tree and compares left and right subtrees
// If there is difference of more than 1 between them it returns -1 otherwise it returns 0 or height of the tree.
// Time complexity: O(n) - checking every node only once
// Space complexity: O(h) - h is height of the tree, for balanced tree log(n) and for a skewed n
