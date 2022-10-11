class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
    def setNext(self, newNext):
        self.next = newNext

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        node = self.head
        count = 0
        while node != None :
            count += 1
            node = node.getNext()

        return count
    
    def remove(self, item):
        node = self.head
        previous = None
        while node.data != item:
            previous = node 
            node = node.getNext()
        
        if previous == None:
            self.head = node.getNext()
        else:
            previous.setNext(node.getNext())

    def squish(self):
        node = self.head
        next = node.next
        while next != None:
            if node.data == next.data:
                node.setNext(next.next)
                next = next.next
            else:
                node = next
                next = node.next

    def dble(self):
        node = self.head
        while node is not None:
            newNode = Node(node.data)
            newNode.next = node.next
            node.next = newNode
            node = node.next.next

    def check(self):
        node = self.head
        element = []
        while node != None:
            element.append(node.data)
            node = node.next
        return element

list1 = UnorderedList()
list1.add(0)
list1.add(0)
list1.add(0)
list1.add(1)
list1.add(1)
list1.add(1)
list1.add(2)
list1.add(3)
list1.add(3)
list1.add(3)
print("First -->",list1.check())
print()
list1.squish()
print("After squish -->",list1.check())
list1.dble()
print()
print("After double -->",list1.check())