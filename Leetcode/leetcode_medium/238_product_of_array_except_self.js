var productExceptSelf = function(nums) {
    let output = Array(nums.length).fill(1);
    let l = 1;
    let r = 1;
    for (let i = 0; i < nums.length; i++) {
        output[i] *= l;
        output[nums.length - 1 - i] *= r;
        l *= nums[i];
        r *= nums[nums.length - 1 - i];
    }
    return output;
};

// Time complexity: O(n) - one loop through array
// Space complexity: O(n) - one additional n length output array
