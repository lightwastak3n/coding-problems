class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        current = list3
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current, list1 = current.next, list1.next
            else:
                current.next = list2
                current, list2 = current.next, list2.next
        if list1 or list2:
            current.next = list1 or list2
        return list3.next