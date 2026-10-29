class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        b = self.balance(root)

        # LL Case
        if b > 1 and value < root.left.value:
            return self.right_rotate(root)

        # RR Case
        if b < -1 and value > root.right.value:
            return self.left_rotate(root)

        # LR Case
        if b > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if b < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, value):
        if root is None:
            return None

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        b = self.balance(root)

        # LL Case
        if b > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR Case
        if b > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR Case
        if b < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL Case
        if b < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self.search(root.left, value)
        return self.search(root.right, value)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)


tree = AVLTree()
root = None

while True:
    x = input("1. Insert | 2. Remove | 3. Traverse | 4. Search | 5. Exit: ")

    if x == '1':
        value = int(input("Enter value to insert: "))
        root = tree.insert(root, value)

    elif x == '2':
        value = int(input("Value to remove: "))
        root = tree.delete(root, value)

    elif x == '3':
        tree.inorder(root)
        print()

    elif x == '4':
        value = int(input("Value to search for: "))
        print("Found" if tree.search(root, value) else "Not Found")

    elif x == '5':
        break

    else:
        print("Invalid choice")
