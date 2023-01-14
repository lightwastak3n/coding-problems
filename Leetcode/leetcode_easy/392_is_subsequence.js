// Time: O(n) - where n is the length of string t
// Space: O(1) - we are only storing 3 ints

var isSubsequence = function(s, t) {
    let i = 0
    let j = 0
    let hits = 0
    while (i < s.length && j < t.length) {
        if (s[i] == t[j]) {
            i++
            hits++
            if (hits == s.length) {
                return true
            }
        }
        j++
    }
    return hits == s.length
};