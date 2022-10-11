class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def setData(self, newData):
        self.data = newData
        
    def setPrev(self, newPrev):
        self.prev = newPrev
        
    def setNext(self, newNext):
        self.next = newNext
    

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def setName(self, newName):
        self.name = newName

    def setScore(self, newScore):
        self.score = newScore
    
    def __str__(self):
        return f"{self.name} {self.score}"


class GolfScore:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        newNode = Node(item)
        if self.first == None and self.last == None:
            self.first = newNode
            self.last = newNode
        else:
            if item.score <= self.first.data.score:
                newNode.setNext(self.first)
                self.first.setPrev(newNode)
                self.first = newNode
            elif item.score >= self.last.data.score:
                newNode.setPrev(self.last)
                self.last.setNext(newNode)
                self.last = newNode
            else:
                current = self.first
                while current.data.score < self.last.data.score:
                    next = current.next
                    if next != None and item.score >= current.data.score and item.score < next.data.score:
                        newNode.setPrev(current)
                        newNode.setNext(next)
                        current.setNext(newNode)
                        next.setPrev(newNode)
                        break
                    current = current.next

        return "item added"
    
    def ascendScore(self):
        current = self.first
        while current != None:
            print(current.data)
            current = current.next

    def descendScore(self):
        current = self.last
        while current != None:
            print(current.data)
            current = current.prev

    def sameScore(self, name):
        current = self.first
        while current != None:
            if current.data.name == name:
                target = current.data.score
                while current.prev != None and current.prev.data.score == target:
                    print(current.prev.data)
                    current = current.prev
                while current.next != None and current.next.data.score == target:
                    print(current.next.data)
                    current = current.next
                break
            current = current.next

        
score = GolfScore()
a = Player('Albert', 12)
b = Player('Bethoven', 12)
c = Player('Cathy', 12)
d = Player('Dorothy', 14)
e = Player('Eric', 16)
score.add(a) # 12
score.add(e) # 56
score.add(d) # 45
score.add(c) # 34
score.add(b) # 23
score.ascendScore()
print()
score.descendScore()
print()
score.sameScore("Cathy")