var isPalindrome = function(s) {
    s = s.toLowerCase();
    let l = 0;
    let r = s.length-1;
    while (l < r) {
        if (!s[l].match(/[a-z0-9]/)) {
            l++;
        }
        else if (!s[r].match(/[a-z0-9]/)) {
            r--;
        }
        else if (s[l] != s[r]) {
            return false;
        }
        else {
            l++;
            r--;
        }
    }
    return true;
};

// Time complexity: O(n) - we check each character once
// Space complexity: O(1) - nothing extra is stored

// Version 2 - might be a bit better since we are reducing string size before checking
// Same complexities
var isPalindrome = function(s) {
    s = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    let i = s.length-1;
    while (i >= s.length / 2 ) {
        if (s[s.length - 1 - i] != s[i]) {
            return false;
        }
        i--;
    }
    return true;
};