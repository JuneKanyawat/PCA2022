class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def contain(self, data):
        if data in self.items:
            return True
        else:
            return False
    
    def show(self):
        for i in self.items:
            print(i)       

    def find_index(self, data):
            return self.items.index(data)



s = Stack()
soi2 = Stack()

while True:
    do = input('Command: ').split(' ')
 
    operation = do[0].strip()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'get':
        if s.is_empty():
            print('No car here')
        else:
            if s.contain(int(do[1])):
                ind = s.find_index(int(do[1]))
                for i in range(ind+1,s.size()):
                    a = s.pop()
                    soi2.push(a)
                print ('Car taken: ',s.pop())
                while not soi2.is_empty():
                    s.push(soi2.pop())
            else:
                print('No that car')
    elif operation == 'size':
        print('No of cars: ', s.size())
    elif operation == 'peek':
        print('Latest car: ', s.peek())
    elif operation == 'show':
        if s.is_empty():
            print('No car here')
        else:
            s.show()
    elif operation == 'contain':
        if s.is_empty():
            print('No car here')
        else:
            print('Is that car here: ', s.contain(int(do[1])))
    elif operation == 'pop':
        if s.is_empty():
            print('No car here')
        else:
            print('Car out: ', s.pop())
    elif operation == 'quit':
        break