var isValidBST = function(root, min = -Infinity, max = Infinity) {
		if (!root) {
			return true;
		}
		if ((root.val <= min) || (root.val >= max)) {
			return false;
		}
		return isValidBST(root.left, min, root.val) && helper(root.right, root.val, max)
};

// Check if root is empty since that is valid
// root.val (current node val) should be between min and max values. If its outside return false.
// If current node is not empty and values are between [min, max] go recursively with checking left and right subtrees. 
// Current node val becomes new min and max for those recursive calls.
// Time complexity: O(n) - visiting each node once
// Space complexity: O(d) - d depth of the tree for call stack