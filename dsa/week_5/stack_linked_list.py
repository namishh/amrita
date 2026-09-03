class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None 
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pop(self):
        if not self.head:
            return
        self.head = self.head.next
        self.size -= 1
        
        
    def __str__(self):
        current = self.head
        str = ''
        while current:
            str += f'{current.data} '
            current = current.next
        return str.rstrip()

    def peek(self):
        return self.head.data
        
    def __len__(self):
        return self.size
    
s = Stack()
while True:
    c = input("1. New List.\n2. Push item into stack. \n3. Pop items.\n4. Peek the first entry.\n5. Print the stack.\nEnter your choice: ")
    if c == '1':
        n = int(input("How many items do you want to enter: "))
        for i in range(n):
            x = int(input(f"What value to insert at index {i}: "))
            s.push(x)
    elif c == '2':
        n = int(input('item to enter: '))
        s.push(n)
    elif c == '3':
        s.pop()
    elif c == '4':
        print(s.peek())
    elif c == '5':
        print(s)
    else:
        break
