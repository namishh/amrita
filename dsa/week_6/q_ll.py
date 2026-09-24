class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.capacity = 0
        
    def enqueue(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.capacity += 1
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.capacity += 1
        
    def dequeue(self):
        if not self.head:
            return
        self.head = self.head.next
        self.capacity -= 1
        
    def peek(self):
        if not self.head:
            return
        return self.head.data
    
    def display(self):
        current = self.head
        str = ''
        while current:
            str += f'{current.data} '
            current = current.next
        print("[" +  str.rstrip() + "]")

q = Queue()    

while True:
    x = input('1. Enqueue 2. Dequeue 3. Peek 4. Display X. Exit: ')
    if x == '1':
        q.enqueue(int(input("Element to enter: ")))
    elif x == '2':
        q.dequeue()
    elif x == '3':
        print(q.peek())
    elif x == '4':
        q.display()
    else:
        break