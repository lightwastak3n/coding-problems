var twoSum = function(nums, target) {
    let seen = {};
    for (let i = 0; i < nums.length; i++) {
        if (target - nums[i] in seen) {
            return [seen[target-nums[i]], i];
        }
        seen[nums[i]] = i;
    }
};

// Maintain hash map of already seen values so that you can compare to current one
// We need index of target - current value if it exists
// Time complexity: O(n) - one pass through the list, checking hash map is O(1)
// Space complexity: O(n) - we are adding array to hash map, on avg n/2 elements, n in worst case 
