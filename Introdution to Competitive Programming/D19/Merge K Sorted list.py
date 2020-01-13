# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        if len (lists)==1 :
            return (lists[0])
        
        h=[]
        for l in lists:            
            while l:
                heapq.heappush(h,l.val )
                l=l.next                
        
        head=tail =ListNode(0)      
        while h:            
            tail.next = ListNode(heapq.heappop(h))
            tail = tail.next            
            
        return(head.next)
