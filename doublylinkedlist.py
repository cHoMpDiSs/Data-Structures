class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def append(self, data):
        new_node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1 
        return temp

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self,index):
        
        if index > self.length -1:
            print("index out of range")
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
                
                
        return temp

    def set_value(self, index, data):
        if index > self.length -1:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
            temp.data = data
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
            temp.data = data
        
        return temp

    def insert(self,index,data):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(data)
        if index == self.length:
            return self.append(data)
        temp = self.head

        new_node = Node(data)
        before = self.get(index-1)
        after = before.next

        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
            
        self.length += 1


    def remove(self, index):

        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        else:
            temp = self.get(index)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = None
            temp.prev = None
            self.length -= 1
            return temp

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)
my_doubly_linked_list.print_list()
print("-------------------------")


my_doubly_linked_list.insert(1, 2)

print("-------------------------")

my_doubly_linked_list.print_list()

print("-------------------------")

my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()





