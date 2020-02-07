class Node:
    def __init__(self,val):
        super().__init__()
        self.val = val
        self.left = None
        self.right = None
# inserting data into the tree
    def insert(self,data):
        if self.val == data:
            return False
        elif self.val > data:
            if self.left:
                return self.left.insert(Node(data))
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(Node(data))
            else:
                self.right = Node(data)
                return True
    def find(self,data):
        if self.val == data:
            return True
        elif self.val > data:
            if self.left:
                return self.left.find(data)
            False
        else:
            if self.right:
                return self.right.find(data)
            return False

    def preOrder(self):
        if self:
            print(str(self. val))
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()
    def postOrder(self):
        if self:
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print(str(self. val))
    def inOrder(self):
        if self:
            if self.left:
                self.left.inOrder()
            print(str(self. val))
            if self.right:
                self.right.inOrder()


class Tree:
    def __init__(self):
        super().__init__()
        self.root = None
    def insert(self,data):
        if self.root :
            return self.root.insert(Node(data))
        else:
            self.root = Node(data)
            return True
    def find(self,data):
        if self.root :
            return self.root.find(data)
        else:
            return False

    def preOrder(self):
        print("pre-order")
        self.root.preOrder()


    def postOrder(self):
        print("pre-order")
        self.root.postOrder  ()
        
    def inOrder(self):
        print("pre-order")
        self.root.inOrder()
        


if __name__ == "__main__":
    # bst = Tree()
    # bst.insert(10)
    # bst.insert(9)
    # bst.insert(5)
    # bst.insert(2)
    # bst.insert(8)

    # bst.find(10)
    # bst.inOrder()
    # bst.preOrder()    
    # bst.postOrder()
    name = "Minasie"
    string = "I am {}".format(name)

    print(string)