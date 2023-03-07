var majorityElement = function(nums) {
    let n = nums.length;
    if (n < 3) return nums[0];
    let t = {[nums[0]]: 1};
    let current = nums[0];
    for (let i = 1; i < n; i++) {
            if (nums[i] === current) {
                t[nums[i]]++;
            }
            else {
                t[current]--;
                if (t[current] === 0) {
                    t = {[nums[i]]: 1};
                    current = nums[i];
                }
            }
    }
    return Object.keys(t)[0];
};

// Time complexity: O(n) - going once through the array
// Space complexity: O(1) - storing 1 int and an obj with one element