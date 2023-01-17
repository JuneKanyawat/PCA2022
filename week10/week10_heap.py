class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Heap:
    cnt = 0
    stop = 0
    next = 0
    level = 0

    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.cnt == 0 and self.root is None:
            self.root = new_node
        else:
            self.cnt += 1
            self.stop += 1
            for i in range(self.next, 2 ** self.cnt):
                if self.stop == 2 ** i:
                    self.stop = 0
                    self.next = i + 1
                    self.level += 1
                    break
            #print(new_node.data, self.level)
            self.__insert_node(self.root, new_node)

    def __insert_node(self, current_node, new_node):
        return





'''
          0                 2^0
    1           2           2^1
3       4   5       6       2^2
...    
'''

l = [5, 6, 10, 8, 9, 3, 8, 4]
tree = Heap()
for i in l:
    tree.insert(Node(i))

