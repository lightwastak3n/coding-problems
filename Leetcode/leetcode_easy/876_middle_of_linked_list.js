var middleNode = function(head) {
    let p1 = head
    let p2 = head.next
    while (p2) {
        p1 = p1.next
        if (p2.next) {
            p2 = p2.next.next
        }
        else {
            return p1
        }
    }
    return p1    
};