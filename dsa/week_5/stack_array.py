class Stack:
    def __init__(self, capacity=100):
        self.stack = []
        self.capacity = capacity
    
    def new(self):
        self.stack = []
        n = int(input("how long should the stack be: "))
        self.capacity = n
        l = [int(input(f"entry {i+1}: ")) for i in range(int(input("how many entries do you want: ")))]
        for i in l:
            self.push(i)
            
    def push(self, item):
        if len(self.stack) >= self.capacity:
            print("stack overflow")
            return
        self.stack.append(item)
        
    def pop(self):
        if len(self.stack) == 0:
            print("stack underflow")
            return
        self.stack.pop()
        
    def peek(self):
        if len(self.stack) == 0:
            print("empty stack")
            return
        
        return self.stack[-1]
    
    def __str__(self):
        return str(self.stack)

s = Stack()
while True:
    c = input("1. New List.\n2. Push item into stack. \n3. Pop items.\n4. Peek the first entry.\n5. Print the stack.\nEnter your choice: ")
    if c == '1':
        s.new()
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
