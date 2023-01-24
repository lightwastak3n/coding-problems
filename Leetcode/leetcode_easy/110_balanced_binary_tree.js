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
