class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
n1 = Node('X')
n2 = Node('Y')
n3 = Node('Z')
n4 = Node('A')

n1.next = n2
n2.next = n3
n3.next = n4

start = n1
current = start

while current is not None:
    print(current.value)
    current = current.next
    

