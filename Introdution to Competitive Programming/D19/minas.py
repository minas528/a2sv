class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head: ListNode, G):  #input：linklist，output：numb of connected components
        dummy = prev = ListNode(-1)  # build dummy head for head
        dummy.next = head
        curr = head

        numb_c = 0
        while curr:  # traversal the linklist
            if prev.val not in G and curr.val in G:  # case 1
                numb_c += 1
            elif prev.val in G and curr.val in G:  # case 2
                pass
            elif prev.val in G and curr.val not in G:  # case 3
                pass
            prev = prev.next
            curr = curr.next

        return numb_c
