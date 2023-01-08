var search = function(nums, target) {
    let l = 0;
    let r = nums.length-1;
    while (l <= r) {
        let mid = Math.floor((l + r) / 2);
        if (nums[mid] < target) {
            l = mid + 1;
        }
        else if (nums[mid] > target) {
            r = mid - 1;
        }
        else {
            return mid;
        }
    }
    return -1;
};

// Time complexity: O(log(n)) - halving search domain in every iteration 
// Space complexity: O(1)
