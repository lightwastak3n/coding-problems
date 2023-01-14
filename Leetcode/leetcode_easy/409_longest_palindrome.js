var longestPalindrome = function(s) {
    let freq = {};
    for (let i = 0; i < s.length; i++) {
        if (freq[s[i]]) {
            freq[s[i]]++;
        }
        else {
            freq[s[i]] = 1;
        }
    }
    let odds = 0;
    let total = 0;
    for (val of Object.values(freq)) {
        if (val % 2 == 0) {
            total += val;
        }
        else {
            total += val - 1;
            odds = 1;
        }
    }
    return total + odds;
};

// Build frequency hashmap
// Go through it and add even chars and odd -1 chars
// If there is at least 1 odd char add + 1 to total score
// Time complexity: O(n) - we go through all chars in s, we go through at most 52 different values in hashmap
// Space complexity: O(1) - storing at most 52 key:value pairs in hashmap



//Shorter version using Set()
var longestPalindrome = function(s) {
    let freq = new Set();
    for (char of s) {
        if (freq.has(char)) {
            freq.delete(char);
        }
        else {
            freq.add(char);
        }
    }
    let odds = freq.size ? 1 : 0;
    return s.length - freq.size + odds;
};
// Time complexity: O(n) - one loop through all of s
// Space complexity: O(1) - storing at most 52 odd chars in set
