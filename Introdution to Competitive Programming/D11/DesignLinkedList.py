class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= 0 and index <= 1000:
            counter = 0
            node = self.head
            while node:
                if counter == index:
                    return node.val
                node = node.next
                counter += 1
        return -1
        
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head != None:
            newnode = ListNode(val)
            newnode.next = self.head
            self.head = newnode
        else:
            self.head = ListNode(val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head != None:
            newnode = ListNode(val)
            node = self.head
            while node:
                if node.next == None:
                    node.next = newnode
                    break
                node = node.next
        else:
            self.head = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index >= 0 and index <= 1000:
            node = self.head
            counter = 1
            if index == 0:
                if self.head != None:
                    newnode = ListNode(val)
                    newnode.next = self.head
                    self.head = newnode
                else:
                    self.head = ListNode(val)
            else:
                while node:
                    if index == counter:
                        newnode = ListNode(val)
                        temp = node.next
                        node.next = newnode
                        node.next.next = temp
                        break
                    node = node.next
                    counter += 1
        else:
            pass
            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self.head
        counter = 1
        if node.next != None:
            if index == 0:
                temp = node.next
                self.head = temp
            else:
                while node:
                    if index == counter and node.next != None:
                        node.next = node.next.next
                        break

                    node = node.next
                    counter += 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
