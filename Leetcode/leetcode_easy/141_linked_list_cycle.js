var hasCycle = function(head) {
    if (!head) return false;
    let [slow, fast] = [head, head];
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
};

// 2 pointers. If they meet it means there is a cycle. If fast reaches the end it means there is no cycle.
// Time complexity: O(n)
// Space complexity: O(1)
