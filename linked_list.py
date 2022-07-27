
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = Node() # used to start the list but nothing goes inside

    def append(self,data):
        new_node = Node(data) # putting the data into the node
        current = self.head # start at the beginning 
        while current.next != None: # traversing the list searching for 
            current = current.next # the last value where next is NONE
        current.next = new_node # now adding the new node(data) do tail
    
    def length(self): # no parameters because we just want to look
        current = self.head # start at the head
        total = 0 # placer for amount of Nodes
        while current.next != None: # iterate through list
            total += 1 # count each Node and add to total
            current = current.next #move to next Node
        return total # return the total integar number of Nodes

    def display(self):
        elements = [] #empty list
        current_node = self.head #start at head
        while current_node.next != None: #traversing the list
            current_node = current_node.next
            elements.append(current_node.data) # adding each data to list
        print(elements)    

    def get(self, index): # takes in an index perameter
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        current_index = 0 # start at index 0
        current_node =self.head # start at head
        
        while True: # iterate through list
            current_node = current_node.next 
            if current_index == index: 
                return current_node.data
            current_index += 1

    def erase(self, index):
        if index >= self.length(): # self explanitory
            print ("ERROR: 'ERASE' Index our of range!")
            return
        current_index = 0 # setting index
        current_node = self.head # start at head
        while True: 
            last_node = current_node # begin traversal
            current_node = current_node.next #
            if current_index == index: # search for index
                last_node.next = current_node.next # replace the index with the next
                return                          # which removes the index
            current_index += 1

            
""" ------SOME DRIVER CODE ------"""
my_list = linked_list()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
my_list.erase(2)
my_list.display()
