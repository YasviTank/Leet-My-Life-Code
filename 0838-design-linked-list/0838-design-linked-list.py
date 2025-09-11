# class Node:
#     def __init__(self, val = 0):
#         self.val = val
#         self.next = None


# class MyLinkedList(object):

#     def __init__(self):
#         self.head = None
#         self.size = 0
        

#     def get(self, index):
#         """
#         :type index: int
#         :rtype: int
#         """
#         if index < 0  or index >= self.size:
#             return -1

#         current = self.head
#         for i in range(index):
#             current = current.next
        
#         return current.val

        

#     def addAtHead(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         new_node = Node(val)
#         new_node.next = self.head
#         self.head = new_node
#         self.size += 1
        

#     def addAtTail(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         current = self.head

#         #If the list is empty
#         if current == None:
#             self.addAtHead(val)
#             return

#         while current.next != None:
#             current = current.next

#         new_node = Node(val)
#         current.next = new_node
#         self.size += 1

        

#     def addAtIndex(self, index, val):
#         """
#         :type index: int
#         :type val: int
#         :rtype: None
#         """
#         if index > self.size or index < 0:
#             return
#         if index == 0:
#             self.addAtHead(val)
#             return
#         if index == self.size:
#             self.addAtTail(val)
#             return

#         new_node = Node(val)
#         current = self.head

#         for i in range(index - 1):
#             current = current.next

#         new_node.next = current.next
#         current.next = new_node
#         self.size += 1        

#     def deleteAtIndex(self, index):
#         """
#         :type index: int
#         :rtype: None
#         """
#         if index < 0 or index >= self.size:
#             return
        
#         current = self.head
#         if index == 0:
#             self.head = current.next
#             self.size -= 1
#             return
            

#         for i in range(index - 1):
#             current = current.next

#         # if index == self.size:
#         #     current.next = None
#         #     return 
#         current.next = current.next.next
#         self.size -= 1

            





###### DOUBLY LINKED LIST #######

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for i in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val):

        new_node = Node(val)

        if not self.head:  # empty list
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1


    def addAtTail(self, val):

        new_node = Node(val)

        if not self.head:  # empty list
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.size += 1


    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)
        current = self.head
        for i in range(index):
            current = current.next
        prev = current.prev
        
        prev.next = new_node
        new_node.prev = prev
        new_node.next = current
        current.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        
        current = self.head

        for _ in range(index):
            current = current.next

        # Case 1: deleting head
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next  # move head forward

        # Case 2: deleting tail
        if current.next:
            current.next.prev = current.prev

        self.size -= 1





# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)