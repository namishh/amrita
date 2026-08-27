class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.capacity = 0
        
    def shift(self, data):
        new_node = Node(data)
        new_node.next = self.head
        
        if self.head:
                self.head.prev = new_node
        
        self.head = new_node
        self.capacity += 1
        
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.capacity += 1
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
        self.capacity += 1
        
    def insert(self, data, n):
        if n > self.capacity:
            print("Error: index out of bounds")
            return 
        if n < 0:
            print("Negative Index")
            return 
        
        if n == 0:
            self.shift(data)
            return
        
        if n == self.capacity:
            self.append(data)
            return
        
        new_node = Node(data)
        curr = self.head
        pos = 0
        while curr and pos < n:
            curr = curr.next
            
            pos += 1
            
        new_node.next = curr
        new_node.prev = curr.prev

        curr.prev.next = new_node
        curr.prev = new_node

        self.capacity += 1
        
    def remove_start(self):
        if not self.head:
            return
        self.head = self.head.next
        self.capacity -= 1
        
        if self.head:
            self.head.prev = None
            
            
    def remove_end(self):
        if not self.head:
            return
        
        curr = self.head

        while curr.next:
            curr = curr.next

        if curr.prev:
            curr.prev.next = None
        else:
            self.head = None
        
        self.capacity -= 1
        
    def remove_by_value(self, n):
        if not self.head:
            return
        curr = self.head
        
        while curr.next and curr.data != n:
            curr = curr.next
        
        if not curr:
            print('Element to be removed not fuond')
            return
        
        if curr.prev is None:
            self.head = curr.next
            
            if self.head:
                self.head.prev = None
                
        else:
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
        
        self.capacity -= 1
        
    def __str__(self):
        current = self.head
        str = ''
        while current:
            str += f'{current.data} '
            current = current.next
        return str.rstrip()

        
    def __len__(self):
        return self.capacity
        
        

dll = None

menu='''1.Create Doubly Linked List\n2.Insert at beginning\n3.Insert at end\n4.Insert at nth index\n5.Remove from start\n6.Remove from end\n7.Remove by value\n8.Length\n9.Display\nQuit by entering anything else'''

while True:
    print(menu)
    s = input("Your choice:")
    if s == '1':
        dll = DoublyLinkedList()
        n = int(input("How many items do you want to enter: "))
        for i in range(n):
            x = eval(input(f"What value to insert at index {i}: "))
            dll.append(x)
    elif s == '2':
        x = eval(input("Item to insert: "))
        dll.shift(x)
    elif s == '3':
        x = eval(input("Item to insert: "))
        dll.append(x)
    elif s == '4':
        x = eval(input("Item to insert: "))
        y = int(input(f"Index to insert at (0 to {dll.capacity}): "))
        dll.insert(x, y)
    elif s == '5':
        dll.remove_start()
    elif s == '6':
        dll.remove_end()
    elif s == '7':
        x = eval(input("what value do you want removed: "))
        dll.remove_by_value(x)
    elif s == '8':
        print(len(dll))
    elif s == '9':
        print(dll)
    else:
        break
