# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        if not head:
            return head
        curr = head.next
        prev = head
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next