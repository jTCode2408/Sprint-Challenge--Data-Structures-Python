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
##FIFO, queue style. num for input var, get-gets all in order from Front to back
#append pushes onto front, oldest leaves line
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.node = None
        self.storage = DoublyLinkedList() #will be stored in
        

    def append(self, item):
        if self.storage.length < self.capacity: #check capacity: if space: add item
            self.storage.add_to_tail(item)
            self.node = self.storage.head
        elif self.storage.length == self.capacity: #if capacity is full need:
            self.node.value = item #get item value to add
            if self.node ==self.storage.tail: #if node is on tail, move to front
                self.node = self.storage.head #else put node in front
            else:
                self.node = self.current.next #move nodes down a spot when adaded
            
    def get(self):
        pass