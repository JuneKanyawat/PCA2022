class Stack(object):
    def __init__(self,max_length):
        self.max_length= max_length
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        if len(self.items)==self.max_length:
            print(">> Full <<")
        else:   
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
        print(self.items, end=" ")
                

    def find_index(self, data):
            return self.items.index(data)


a = input('Capacity of Soi 1: ')
b = input('Capacity of Soi 2: ')
c = 1
a=int(a)
b=int(b)
s = Stack(a)
soi2 = Stack(b)
order = Stack(c)

while True:
    soi = input('Soi: ')

    if soi == '1':
        do = input('Command: ').split(' ')
        operation = do[0].strip()
        if operation == 'push':
            s.push(int(do[1]))
        elif s.is_empty():
            print('Stack is empty.')
        elif not s.is_empty():
            if operation == 'get':
                if s.contain(int(do[1])):
                    ind = s.find_index(int(do[1]))
                    num = s.size() - ind
                    if num-1 <= b-soi2.size():
                       s.show(),soi2.show(),order.show(),print('\n')
                       for i in range(1,num):
                           a = s.pop()
                           soi2.push(a)
                       order.push(int(s.pop()))
                       s.show(),soi2.show(),order.show(),print('\n')
                       for i in range(1,num):
                           s.push(soi2.pop())
                       s.show(),soi2.show(),order.show(),print('\n')
                       order.pop()
                    else:
                        print("No empty space")
                else:
                    print("no that car")
            elif operation == 'size':
                print('Size value: ', s.size())
            elif operation == 'peek':
                print('Top value: ', s.peek())
            elif operation == 'show':
                s.show(),soi2.show(),order.show(),print('\n')
            elif operation == 'contain':
                print('Value in stack?: ', s.contain(int(do[1])))
            elif operation == 'pop':
                print('Popped value: ', s.pop())
            elif operation == 'pop':
                print('Popped value: ', s.pop())
            else:
                print('Wrong command')
    elif soi == '2':
        do = input('Command: ').split(' ')
        operation = do[0].strip()
        if operation == 'push':
            soi2.push(int(do[1]))
        elif soi2.is_empty():
            print('Stack is empty.')
        elif not soi2.is_empty():
            if operation == 'get':
                if soi2.contain(int(do[1])):
                    ind = soi2.find_index(int(do[1]))
                    num = soi2.size() - ind
                    if num-1 <= a-s.size():
                       s.show(),soi2.show(),order.show(),print('\n')
                       for i in range(1,num):
                           a = soi2.pop()
                           s.push(a)
                       order.push(int(soi2.pop()))
                       s.show(),soi2.show(),order.show(),print('\n')
                       for i in range(1,num):
                           soi2.push(s.pop())
                       s.show(),soi2.show(),order.show(),print('\n')
                       order.pop()
                    else:
                        print("No empty space")
                else:
                    print("no that car")
            elif operation == 'size':
                print('Size value: ', soi2.size())
            elif operation == 'peek':
                print('Top value: ', soi2.peek())
            elif operation == 'show':
                s.show(),soi2.show(),order.show(),print('\n')
            elif operation == 'contain':
                print('Value in stack?: ', soi2.contain(int(do[1])))
            elif operation == 'pop':
                print('Popped value: ', soi2.pop())
            elif operation == 'pop':
                print('Popped value: ', soi2.pop())
            else:
                print('Wrong command')

    elif soi == 'quit':
            break



    
    