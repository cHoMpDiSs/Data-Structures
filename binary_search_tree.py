class Node:
    def __init__ (self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self, value, current_node):
        if value < current_node.value: # if value is less than current node
            if current_node.left_child == None: # and current nodes left child is NONE
                current_node.left_child = Node(value) # assign new node to left child
            else:
                self._insert(value,current_node.left_child) # recurse down the left part of tree 
                # until it meets its base case and insertion point
        elif value > current_node.value:
            if current_node.right_child == None: # we are doing the same as above but 
                current_node.right_child = Node(value) # for values greater than node
            else:                                       #putting it on the right side of the tree
                self._insert(value, current_node.right_child) # more recursion down the tree
        else:
            print("Value already in tree!")

    def print_tree(self): # print tree
        if self.root != None:
            self._print_tree(self.root)
    
    def _print_tree(self, current_node): # recursive print tree function
        if current_node != None: 
            self._print_tree(current_node.left_child)
            print (str(current_node.value))
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,current_node, current_height):
        if current_node == None:
            return current_height
        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height,right_height)

    def search(self, value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False
    
    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._search(value, current_node.right_child)
        return False
    


"""driver code to test"""            
def fill_tree(tree,nums = 100, maxint= 1000):
    from random import randint
    for x in range (nums):
        current_elem = randint (0, maxint)
        tree.insert(current_elem)
    return tree

tree = BinarySearchTree()
tree = fill_tree(tree)

tree.insert(5)
tree.insert(4)
tree.insert(5)
tree.insert(34)
tree.insert(786)
tree.insert(4)
tree.insert(56)
tree.insert(76)
tree.insert(3)
tree.insert(89)

print(tree.search(56))
print(tree.search(235))


# tree.print_tree()

# print ("tree height is", tree.height())