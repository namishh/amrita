class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class CircularQueue:
    def __init__(self):
        self.head = None
        self.capacity = 0
        
    def enqueue(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            self.capacity += 1
            return
        
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head        
        
        self.capacity += 1
        
    def dequeue(self):
        if not self.head:
            return 
        
        removed_data = self.head.data
        
        if self.head.next == self.head:
            self.head = None        
               
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next     
            self.head = self.head.next
            curr.next = self.head
            
        self.capacity -= 1
        return removed_data

        
    def peek(self):
        if not self.head:
            return
        return self.head.data
    
    def display(self):
        if not self.head:
            return ''
        current = self.head
        str = ''
        while True:
            str += f'{current.data} '
            current = current.next
            if current == self.head:
                break
        print("[" +  str.rstrip() + "]")

q = CircularQueue()    

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