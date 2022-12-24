var reverseList = function(head) {
    let reversed = null
    while (head) {
        let temp = head
        head = head.next
        temp.next = reversed
        reversed = temp
    }
    return reversed
};