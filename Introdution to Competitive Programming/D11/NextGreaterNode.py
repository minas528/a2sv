# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        n = 0
        rev = None
        while head:
            n += 1
            temp = head.next
            head.next = rev
            rev = head
            head = temp
        res = [0] * n
        itr = n - 1
        Stack = None
        while rev:
            temp = rev
            rev = rev.next
            while Stack and Stack.val <= temp.val:
                Stack = Stack.next

            if Stack:
                res[itr] = Stack.val
            itr -= 1
            temp.next = Stack
            Stack = temp
        return res
