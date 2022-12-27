// Solution 1
var detectCycle = function(head) {
    let seen = new Set();
    while (head) {
        if (seen.has(head)) {
            return head;
        }
        else {
            seen.add(head);
            head = head.next;
        }
    }
    return null;
};
// Time complexity: O(n) - one loop through the list and set lookup is O(1)
// Space complexity: O(n) - storing at most all n nodes

//Solution 2:
// We can also do O(n) without using additional memory
var detectCycle = function(head) {
    let slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            while (head != fast) {
                head = head.next;
                fast = fast.next;
            }
            return head;
        }
    }
    return null
};
// Explanation
// Lets call distance to start of the loop D, loop length L, and distance from start of the loop until meet point X
// Slow pointer has traveled S = D + X
// Fast pointer has traveled F = D + L + X and also it traveled 2x what S did so
// F = D + L + X = 2 * S = 2D + 2X. We are looking for distance to the start of the loop which is D.
// Simplify and we get D = L - X. 
// And since L is the loop length and X extra distance that fast traveled, if fast travels L - X it's gonna end up at the start of the loop.
// So we just let head and fast go 1 step at a time and they will meet up at loop start.
// Time complexity: O(n) - since n = D + L and we did D + X iterations in the first while loop and L - X in the second so in total D + X + L - X = D + L = n
// Space complexity: O(1) - we are not storing anything