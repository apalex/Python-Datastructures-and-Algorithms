class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # T O(n), M O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    # T O(n), M O(n)
    def reverseRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseRecursive(head.next)
            head.next.next = head
        head.next = None

        return newHead
