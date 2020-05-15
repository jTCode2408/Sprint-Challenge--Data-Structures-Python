'''
buffer = RingBuffer(3)
buffer.get()   # should return []
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.get()   # should return ['a', 'b', 'c']
# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')
buffer.get()   # should return ['d', 'b', 'c']
buffer.append('e')
buffer.append('f')
buffer.get()   # should return ['d', 'e', 'f']
'''
from dll import DoublyLinkedList

#append pushes onto front, oldest leaves line
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.node = None
        self.storage = DoublyLinkedList() #will be stored in
        

    def append(self, item):
        if self.storage.length < self.capacity: #check capacity: if space: add item
            self.storage.add_to_tail(item) #put item in back
            self.node = self.storage.head #make mself head
        elif self.storage.length == self.capacity: #if capacity is full need:
            self.node.value = item #get the new item
            if self.node == self.storage.tail: #if at tail
                self.node = self.storage.head #add to dll head
            else:
                self.node = self.node.next #move nodes down a spot when adaded
            
    def get(self):
        storage = [] #list to add nodes to after getting
        node = self.storage.head #desingate head 
        #check for nodes to add, then add nodes to lsit 
        # while the exist
        while node is not None:
            storage.append(node.value)
            #get next node, then repeat add
            node = node.next
        #return ist of nodes
        return storage