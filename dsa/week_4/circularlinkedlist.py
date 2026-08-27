class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.capacity = 0
        
    def shift(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
            
        new_node.next = self.head
        curr.next = new_node
        self.head = new_node
        
        self.capacity += 1

    def append(self, data):
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
        while pos < n - 1:
            curr = curr.next
            pos += 1
            
        new_node.next = curr.next
        curr.next = new_node
        self.capacity += 1
        
    def remove_start(self):
        if not self.head:
            return
        
        if self.head.next == self.head:
            self.head = None
            self.capacity -= 1
            return

        curr = self.head

        while curr.next != self.head:
            curr = curr.next

        self.head = self.head.next
        curr.next = self.head

        self.capacity -= 1
        
    def remove_end(self):
        if not self.head:
            return

        if self.head.next == self.head:
            self.head = None
            self.capacity -= 1
            return

        curr = self.head

        while curr.next.next != self.head:
            curr = curr.next

        curr.next = self.head

        self.capacity -= 1

        
    def remove_by_value(self, n):
        if not self.head:
            return

        if self.head.data == n:
            self.remove_start()
            return

        curr = self.head

        while curr.next != self.head and curr.next.data != n:
            curr = curr.next

        if curr.next == self.head:
            print("not found")
            return

        curr.next = curr.next.next

        self.capacity -= 1


        
    def __str__(self):
        if not self.head:
            return ''
        current = self.head
        str = ''
        while True:
            str += f'{current.data} '
            current = current.next
            if current == self.head:
                break
        return str.rstrip()

        
    def __len__(self):
        return self.capacity
        

cll = None

menu='''1.Create Circular Linked List\n2.Insert at beginning\n3.Insert at end\n4.Insert at nth index\n5.Remove from start\n6.Remove from end\n7.Remove by value\n8.Length\n9.Display\nQuit by entering anything else'''

while True:
    print(menu)
    s = input("Your choice:")
    if s == '1':
        cll = CircularLinkedList()
        n = int(input("How many items do you want to enter: "))
        for i in range(n):
            x = eval(input(f"What value to insert at index {i}: "))
            cll.append(x)
    elif s == '2':
        x = eval(input("Item to insert: "))
        cll.shift(x)
    elif s == '3':
        x = eval(input("Item to insert: "))
        cll.append(x)
    elif s == '4':
        x = eval(input("Item to insert: "))
        y = int(input(f"Index to insert at (0 to {cll.capacity}): "))
        cll.insert(x, y)
    elif s == '5':
        cll.remove_start()
    elif s == '6':
        cll.remove_end()
    elif s == '7':
        x = eval(input("what value do you want removed: "))
        cll.remove_by_value(x)
    elif s == '8':
        print(len(cll))
    elif s == '9':
        print(cll)
    else:
        break
