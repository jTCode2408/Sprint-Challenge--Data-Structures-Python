class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        prev = None #prev shoud be nothing initially
        node = self.head #set head as node passed in
        while node: #check for node
            new_next = node.get_next() #hold next for reassign
            node.set_next(prev) #set current next to prev to change pointer direction
            prev = node #previous will now be pointed at me, node
            node = new_next #reset my next 
            self.head = prev #reset the head prev


        #attempting recursively     
        '''
        prev = None
        node = self.head
        node.reverse_list(next_node)
        self.next_node  =self.head
        return nodes
'''