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

    def show(self, data):
        for i in self.items:
            print(i)
    
 
s = Stack()
while True:
    print('push _')
    print('pop')
    print('peek')
    print('size')
    print('contain _')
    print('quit')
    do = input('Command: ').split()
 
    operation = do[0].strip()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'size':
        print('Size value: ', s.size())
    elif operation == 'peek':
        print('Top value: ', s.peek())
    elif operation == 'contain':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Value in stack?: ', s.contain(int(do[1])))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break