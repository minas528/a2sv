# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        root = ListNode(0)
        cur = root.next = head
        while cur and cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                temp = cur.next
                cur.next = cur.next.next
                pre = root
                while pre.next.val <= temp.val:
                    pre = pre.next
                temp.next = pre.next
                pre.next = temp
                
        return root.next
