class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    
    def __init__(self):
        
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right



    def contains(self,value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: 
                return True
        return False

    def min_value_node(self, current_node):
        
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value



    def print_tree_left(self):
        temp = self.root
        while temp is not None:
            print(temp.value)
            temp = temp.left










my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(123)
my_tree.insert(45)
my_tree.insert(543)
my_tree.insert(43523)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)


print(my_tree.contains(3))   
my_tree.print_tree_left()   

print(my_tree.max_value_node(my_tree.root.right))