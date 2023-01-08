var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let l = 0;
        while (l < n) {
            let mid = Math.floor((l + n) / 2);
            if (isBadVersion(mid)) {
                n = mid;
            }
            else {
                l = mid + 1;
            }
        }
        return n;
    };
};

// This is just a binary search
// Time complexity: O(log(n))
// Space complexity: O(1)