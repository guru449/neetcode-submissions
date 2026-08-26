# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = list1
        cur2 = list2
        result = temp = ListNode()

        while cur1 and cur2:
            if cur1.val < cur2.val:
                result.next = cur1
                cur1 = cur1.next
            else:
                result.next = cur2
                cur2 = cur2.next
            result = result.next
        
        if cur1 != None:
            result.next = cur1
        if cur2 != None:
            result.next = cur2
        
        return temp.next
        
#easy almost solved on own
