class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if (head == None or head.next == None or k == 1): return head
        len = 0
        cur = head
        while (cur != None):
            len += 1
            cur = cur.next

        groups = len / k
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        start, prestart, pre = cur, dummy, dummy
        while (groups > 0):
            # reverse a group
            for i in range(k):  # (int i=0;i<k;i++){
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

            # connect the tail of current group with the head of the next group
            start.next = cur
            prestart.next = pre
            pre = start
            prestart = start
            start = cur
            groups -= 1

        return dummy.next;