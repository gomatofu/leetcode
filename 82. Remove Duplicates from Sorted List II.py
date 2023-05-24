class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0,head)
        pointer = sentinel

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next

                pointer.next = head.next
            else:
                pointer = pointer.next

            head = head.next

        return sentinel.next