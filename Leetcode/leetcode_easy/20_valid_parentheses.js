var isValid = function(s) {
    if (s.length % 2 == 1) {
        return false;
    }
    let stack = []
    let paren = {"(": ")", "[": "]", "{": "}"}
    for (let i = 0; i < s.length; i++) {
        if (s[i] in paren) {
            stack.push(paren[s[i]])
        }
        else if (stack.pop() != s[i]) {
            return false;
        }
    }
    return stack.length == 0;
};

// Check if you are on opening char. If yes push closing char.
// If not, it means you are at a closing char and it should be equal to the char you last pushed.
// Time complexity: O(n)
// Space complexity: O(n)
