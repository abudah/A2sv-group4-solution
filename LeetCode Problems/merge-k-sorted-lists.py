# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedList = ListNode()
        dummy = mergedList
        heap = []

        for i in lists:
            while i:
                heappush(heap, i.val)
                i = i.next
        while heap:
            val = heappop(heap)
            newNode = ListNode(val)
            dummy.next = newNode
            dummy = dummy.next
            
        return mergedList.next
        