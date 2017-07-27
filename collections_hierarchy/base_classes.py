from .node import Node 


class Sequenceable(object):
    def __init__(self):
        self.start = None #attribute
        self.end = None

    def get_elements(self):
        result = []
        current = self.start
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

# Node(X) > Node(Y) > Node(Z) > /
#           ^         *
#Node(A)

class Appendable(object):
    def append(self, element):
        new_node = Node(element)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node
            
        
"""
    def append(self, element): ###inefficient method
        new_node = Node(element)
        if self.start is None:
            self.start = new_node
        else:
            previous_node = self.start
            current_node = self.start.next
            while current_node is not None:
                previous_node = current_node
                current_node = previous_node.next
            
            previous_node.next = new_node
"""            


class Popable(object):
    def pop(self):
        if self.start is None:
            raise IndexError()
        
        first_node = self.start
        self.start = self.start.next
        return first_node.value
        
            

class Pushable:
     def push(self, element):
        new_node = Node(element)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.next = self.start
            self.start = new_node
#            new_node = self.start.next (WHY IS THIS WRONG?)
#            self.start = new_node



#sequence.start = n1