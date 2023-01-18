var isAnagram = function(s, t) {
    if (s.length != t.length) {
        return false;
    } 
    let chars = {}
    for (let i = 0; i < s.length; i++){
        if (s[i] in chars) {
            chars[s[i]]++;
        }
        else {
            chars[s[i]] = 1;
        }
        if (t[i] in chars) {
            chars[t[i]]--;
        }
        else {
            chars[t[i]] = -1;
        }
    }
    return Object.values(chars).every(val => val == 0);
};

// Balance the strings out using a hash map.
// Time complexity: O(n) - it's like O(n) for the loop + O(n) for the Object.values(..) + O(n) for every() = O(3n) = O(n)
// Space complexity: O(n) - for the object