class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.capacity = 0
        
    def shift(self, data):
        new_node = Node(data)
        new_node.next = self.head
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
        self.capacity += 1
        
    def insert(self, data, n):
        if n > self.capacity:
            print("Error: index out of bounds")
            return 
        if n < 0:
            print("Negative Index")
            return 
        
        new_node = Node(data)
        curr = self.head
        pos = 0
        while curr and pos < n - 1:
            curr = curr.next
            
            pos += 1
            
        new_node.next = curr.next
        curr.next = new_node
        self.capacity += 1
        
    def remove_start(self):
        if not self.head:
            return
        self.head = self.head.next
        self.capacity -= 1
        
    def remove_end(self):
        if not self.head:
            return
        
        curr = self.head
        while curr.next.next:
            curr = curr.next
        
        curr.next = None        
        
        self.capacity -= 1
        
    def remove_by_value(self, n):
        if not self.head:
            return
        curr = self.head
      
        if curr and curr.data == n:
            self.head = curr.next
            self.capacity -= 1
            return
        
        prev = None
        while curr and curr.data != n:
            prev = curr
            curr = curr.next
        
        if not curr:
            print("not found")
            return
        
        prev.next = curr.next
        curr = None
        
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
        

ll = None

menu='''1.Create Linked List\n2.Insert at beginning\n3.Insert at end\n4.Insert at nth index\n5.Remove from start\n6.Remove from end\n7.Remove by value\n8.Length\n9.Display\nQuit by entering anything else'''

while True:
    print(menu)
    s = input("Your choice:")
    if s == '1':
        ll = LinkedList()
        n = int(input("How many items do you want to enter: "))
        for i in range(n):
            x = eval(input(f"What value to insert at index {i}: "))
            ll.append(x)
    elif s == '2':
        x = eval(input("Item to insert: "))
        ll.shift(x)
    elif s == '3':
        x = eval(input("Item to insert: "))
        ll.append(x)
    elif s == '4':
        x = eval(input("Item to insert: "))
        y = int(input(f"Index to insert at (0 to {ll.capacity}): "))
        ll.insert(x, y)
    elif s == '5':
        ll.remove_start()
    elif s == '6':
        ll.remove_end()
    elif s == '7':
        x = eval(input("what value do you want removed: "))
        ll.remove_by_value(x)
    elif s == '8':
        print(len(ll))
    elif s == '9':
        print(ll)
    else:
        break
