class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BT:
    def __init__(self):
        self.root = None
        
    def insert(self, new_node): 
        if (self.root is None): 
            self.root = new_node 
        else: 
            self.__insert_node(self.root, new_node)
            
    def __insert_node(self, current_node, new_node): 
        if new_node.data <= current_node.data: # new node น้อยกว่า
            if current_node.left is not None: 
                self.__insert_node(current_node.left, new_node) 
            else: 
                current_node.left = new_node 
        elif new_node.data > current_node.data: 
            if current_node.right is not None: 
                self.__insert_node(current_node.right, new_node) 
            else: 
                current_node.right = new_node 
    
    def find(self, item): 
        node = self.root
        return self.__find_node(node, int(item))
    
    def __find_node(self, node, item):
        if node is None:
            return False
        
        if item == node.data:
            return True
        
        if item <= node.data:
            return self.__find_node(node.left, item)
        
        if item > node.data:
            return self.__find_node(node.right, item)
        
    def remove(self, item):
        node = self.root
        return self.__remove(node, int(item))
        
    def __remove(self, node, item):
        # print(type(node))
        # print(1)
        
        # check The tree
        if node is None:
            return node
        
        #Find the target node
        if item < node.data:
            node.left = self.__remove(node.left, item)

        elif item > node.data:
            node.right = self.__remove(node.right, item)
            
        else:
            # ไม่มีหรือมี1
            if node.left is None:
                temp = node.right
                node = None
                return temp
            
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # ถ้ามี2ใบ
            # สลับตัว
            temp = self.find_min(node.right)     
            node.data = temp.data
            
            # ลบ
            node.right = self.__remove(node.right, temp.data)
            
        return node
    
    def is_empty(self):
        if self.root is None:
            return True
        
        elif self.root is not None:
            return False
            
    def find_min(node):
        # Find the inorder successor
        current = node
        print(current)

        # Find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current
            
    def inorder(self, node):
        if node is None:
            return
        else:
            if node.left is not None:
                self.inorder(node.left)
            print(node.data, end=" ")

            if node.right is not None:
                self.inorder(node.right)
            
    def preorder(self, node):
        if node is None:
            return
        else:
            print(node.data, end=" ")
            if node.left is not None:
                self.preorder(node.left)

            if node.right is not None:
                self.preorder(node.right)
            
    def postorder(self,node):
        if node is None:
            return
        else:
            if node.left is not None:
                self.postorder(node.left)
            if node.right is not None:
                self.postorder(node.right)

            print(node.data, end=" ")
        
        
    def print(self, node, i):
        if node is None:
            return
        
        elif node is not None:
            i += 1
            self.print(node.right, i)
            # print(i)
            print( ' ' * (10 * i), end = '')
            print(node.data)
            self.print(node.left, i)
      
    
binaryTree = BT()

root = Node(25)
binaryTree.insert(root)
binaryTree.insert(Node(15))
binaryTree.insert(Node(10))
binaryTree.insert(Node(4))
binaryTree.insert(Node(12))
binaryTree.insert(Node(22))
binaryTree.insert(Node(18))
binaryTree.insert(Node(24))
binaryTree.insert(Node(50))
binaryTree.insert(Node(35))
binaryTree.insert(Node(31))
binaryTree.insert(Node(44))
binaryTree.insert(Node(70))
binaryTree.insert(Node(66))
binaryTree.insert(Node(90))

print(binaryTree.find(25))
print(binaryTree.is_empty())
binaryTree.inorder(root)
print("")
binaryTree.preorder(root)
print("")
binaryTree.postorder(root)
print("")
binaryTree.print(root,0)
binaryTree.remove(35)
print("----------------------- after remove -----------------------")
binaryTree.print(root,0)
