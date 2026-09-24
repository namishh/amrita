class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.queue = [None] * capacity
        
    def enqueue(self, item):
        if self.rear >= self.capacity - 1:
            print("queue overflow")
            return
        if self.front == -1 and self.rear == -1:
            self.front += 1
        self.rear += 1
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.front > self.rear:
            print("queue underflow")
            self.front = -1
            self.rear = -1
            return
        self.queue[self.front] = None
        self.front += 1
        
    def peek(self):
        return self.queue[self.front]
    
    def display(self):
        print(self.queue[self.front:self.rear + 1])

q = Queue(20)    

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
