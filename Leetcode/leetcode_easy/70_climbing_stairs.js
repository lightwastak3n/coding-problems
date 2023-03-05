var climbStairs = function(n) {
    if (n < 4) {return n}
    let f0 = 0;
    let f1 = 1;
    for (let i = 0; i < n; i++) {
        let temp = f0 + f1;
        f0 = f1;
        f1 = temp;
    }
    return f1;
};

// Iterative solution
// Time Complexity: O(n) - going once through all steps
// Space Complexity: O(1) - storing only 3 variables


var climbStairs = function(n, memo = {}) {
    if (n < 4) return n;
    if (n in memo) return memo[n];
    memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo);
    return memo[n];
}

// Recursive solution
// Time Complexity: O(n) - calculating each step reached once
// Space Complexity: O(n) - storing all n solutions