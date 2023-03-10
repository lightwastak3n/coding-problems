var containsDuplicate = function(nums) {
    let freq = {};
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in freq) {
            return true;
        }
        else {
            freq[nums[i]] = '';
        }
    }
    return false;
};

// Using Map seems to give about the same time
// Time complexity: O(n)
// Space complexity: O(n)