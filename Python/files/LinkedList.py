class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
    
    def print(self):
        print(self.val)

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        node = self.getNode(index)

        return node.val

    def getNode(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        
        curNode = self.head
        for i in range(index):
            curNode = curNode.next
        
        return curNode

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val = val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = self.head.prev

        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val = val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = self.tail.next
        
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            return -1
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            fromTail = self.getNode(index)
            fromHead = fromTail.prev

            newNode = Node(val=val)
            newNode.prev = fromHead
            newNode.next = fromTail
            fromTail.prev = newNode
            fromHead.next = newNode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length:
            return -1

        if self.length == 1:
            nodeToDelete = self.head
            self.head = None
            self.prev = None
        elif index == 0:
            nodeToDelete = self.head
            self.head = self.head.next
            self.head.prev = None
        elif index + 1 == self.length:
            nodeToDelete = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            nodeToDelete = self.getNode(index)
            nodeToDeleteNext = nodeToDelete.next
            nodeToDeletePrev = nodeToDelete.prev
            nodeToDeleteNext.prev = nodeToDeletePrev
            nodeToDeletePrev.next = nodeToDeleteNext
        
        del(nodeToDelete)
        self.length -= 1

    def print(self) -> None:
        print("Start")
        curNode = self.head
        for i in range(self.length):
            curNode.print()
            curNode = curNode.next
        print("Done")

    def printAddrFor(self) -> None:
        print("Start")
        print(self.head)
        curNode = self.head
        for i in range(self.length):
            print(curNode)
            curNode = curNode.next
        print(self.tail)
        print("Done")

    def printAddrBack(self) -> None:
        print("Start")
        print(self.tail)
        curNode = self.tail
        for i in range(self.length):
            print(curNode)
            curNode = curNode.prev
        print(self.head)
        print("Done")

ll = MyLinkedList()
ll.addAtHead(4)
print(ll.get(1))


["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
[[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]
#ll.print()
'''print(ll.deleteAtIndex(0))
ll.addAtHead(5)
ll.addAtHead(3)
ll.addAtHead(2)
ll.addAtTail(6)
ll.addAtTail(7)
ll.print()
print(ll.deleteAtIndex(0))
print(ll.deleteAtIndex(3))
ll.print()
ll.printAddrFor()
ll.printAddrBack()'''
'''ll.addAtHead(1)
ll.addAtTail(3)
ll.print()
ll.printAddrFor()
ll.printAddrBack()
ll.addAtIndex(1, 2)
ll.print()
ll.printAddrFor()
ll.printAddrBack()
ll.deleteAtIndex(1)
ll.print()
ll.printAddrFor()
ll.printAddrBack()'''


        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)