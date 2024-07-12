// Find maximum sum that ends at the index i
// It will either include the previous max sum ending at index i-1 maxSum(i-1) + nums[i], or it will just be nums[i]
// Go through the entire array and keep track of max sum found

var maxSubArray = function(nums) {
    let maxSum = currentSum = -Infinity;
    for (let i = 0; i < nums.length; i++) {
        currentSum = Math.max(currentSum + nums[i], nums[i]);
        maxSum = Math.max(currentSum, maxSum);
    }
    return maxSum;
};
