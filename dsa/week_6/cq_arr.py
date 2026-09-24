class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.queue = [None] * capacity
        
    def enqueue(self, item):
        if (self.rear + 1) % self.capacity == self.front:
            print("queue overflow")
            return
        if self.front == -1 and self.rear == -1:
            self.front += 1
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.front == -1:
            print("queue underflow")
            return
            
        self.queue[self.front] = None
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity


    def peek(self):
        return self.queue[self.front]
    
    def display(self):
        if self.rear >= self.front:
            print(self.queue[self.front:self.rear + 1])
        else:
            print(self.queue[self.front:self.capacity] + self.queue[0: self.rear + 1])

q = CircularQueue(20)    

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