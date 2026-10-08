class BinaryTree:
    def __init__(self):
        self.tree = [None] * 20
        
    def insert(self, value):
        x = len(self.tree) - 1
        while True:
            if self.tree[x] is not None:
                break
            x = x - 1
            if x <= 0:
                break
        self.tree[x] = value
        
    def insert_left(self, value, parentIndex):
        if parentIndex >= len(self.tree) or self.tree[parentIndex] is None:
            print("invalid parent")
            return
        left_index = 2 * parentIndex + 1
        if left_index >= len(self.tree):
            self.tree.extend([None] * (left_index - len(self.tree) + 1))
            
        self.tree[left_index] = value

    def insert_right(self, value, parentIndex):
        if parentIndex >= len(self.tree) or self.tree[parentIndex] is None:
            print("invalid parent")
            return
        right_index = 2 * parentIndex + 1
        if right_index >= len(self.tree):
            self.tree.extend([None] * (right_index - len(self.tree) + 1))
            
        self.tree[right_index] = value

    def remove_index(self, index):
        self.tree[index] = None
        
    def traverse_inorder(self, index=0):
        if index < len(self.tree) and self.tree[index] is not None:
            self.traverse_inorder(2 * index + 1)       
            print(self.tree[index], end=" ")                    
            self.traverse_inorder(2 * index + 2)   
              
    def traverse_preorder(self, index=0):
        if index < len(self.tree) and self.tree[index] is not None:
            print(self.tree[index], end=" ")                    
            self.traverse_preorder(2 * index + 1)       
            self.traverse_preorder(2 * index + 2)        

    def traverse_postorder(self, index=0):
        if index < len(self.tree) and self.tree[index] is not None:
            self.traverse_postorder(2 * index + 1)       
            self.traverse_postorder(2 * index + 2)        
            print(self.tree[index], end=" ")                    


b = BinaryTree()
while True:
    x = input("1.In Order Insert 2. Insert Left 3. Insert Right 4. Remove 5. Inorder 6. Preorder 7. Postorder\nYour choice: ")
    if x == '1':
        b.insert(int(input("Value to Insert: ")))
    elif x == '2':
        b.insert_left(int(input("Value to Insert: ")), int(input("Parent Index: ")))
    elif x == '3':
        b.insert_right(int(input("Value to Insert: ")), int(input("Parent Index: ")))
    elif x == '4':
        b.remove_index(int(input("Index to remove: ")))
    elif x == '5':
        b.traverse_inorder()
        print()
    elif x == '6':
        b.traverse_preorder()
        print()
    elif x == '7':
        b.traverse_postorder()
        print()
    else:
        break
