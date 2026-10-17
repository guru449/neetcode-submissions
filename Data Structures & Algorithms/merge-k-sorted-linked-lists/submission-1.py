# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        def mergeLists(list1, list2):
            res = ListNode()
            cur = res
            while list1 and list2:
                if list1.val >= list2.val:
                    cur.next = list2
                    cur = cur.next
                    list2 = list2.next
                else:
                    cur.next = list1
                    cur = cur.next
                    list1 = list1.next
            if not list1:
                cur.next = list2
            else:
                cur.next = list1
            return res.next
        

        while len(lists) > 1:
            result = []
            for i in range(0 , len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i +1 < len(lists) else None
                result.append(mergeLists(list1, list2))
            lists = result

        return lists[0]
                    

        