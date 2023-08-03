# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        arr = []

        if node:
            while node.next:
                arr.append(node.val)
                node = node.next
            arr.append(node.val)
            arr.sort()
            node = head
            for i in arr:
                node.val = i
                node = node.next
        return head