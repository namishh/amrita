class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def find_node(self, value):
        if self.root is None:
            return None

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.value == value:
                return current

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return None

    def insert_left(self, value, parentValue):
        parent = self.find_node(parentValue)

        if parent is None:
            print("invalid parent")
            return

        if parent.left is not None:
            print("left child already exists")
            return

        parent.left = Node(value)

    def insert_right(self, value, parentValue):
        parent = self.find_node(parentValue)

        if parent is None:
            print("invalid parent")
            return

        if parent.right is not None:
            print("right child already exists")
            return

        parent.right = Node(value)

    def remove(self, value):
        if self.root is None:
            print("tree is empty")
            return

        if self.root.value == value:
            self.root = None
            return

        queue = [(self.root, None)]

        while queue:
            current, parent = queue.pop(0)

            if current.value == value:
                if parent.left == current:
                    parent.left = None
                elif parent.right == current:
                    parent.right = None

                return

            if current.left is not None:
                queue.append((current.left, current))

            if current.right is not None:
                queue.append((current.right, current))

        print("value not found")

    def traverse_inorder(self, node=None):
        if node is None:
            node = self.root

        if node is not None:
            self.traverse_inorder(node.left)
            print(node.value, end=" ")
            self.traverse_inorder(node.right)

    def traverse_preorder(self, node=None):
        if node is None:
            node = self.root

        if node is not None:
            print(node.value, end=" ")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_postorder(self, node=None):
        if node is None:
            node = self.root

        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.value, end=" ")


b = BinaryTree()

while True:
    x = input("1. Insert Left 2. Insert Right 3. Remove 4. Inorder 5. Preorder 6. Postorder\nYour choice: ")

    if x == '1':
        b.insert_left(int(input("Value to Insert: ")), int(input("Parent Value: ")))
    elif x == '2':
        b.insert_right(int(input("Value to Insert: ")), int(input("Parent Value: ")))
    elif x == '3':
        b.remove(int(input("Value to remove: ")))
    elif x == '4':
        b.traverse_inorder()
        print()
    elif x == '5':
        b.traverse_preorder()
        print()
    elif x == '6':
        b.traverse_postorder()
        print()
    else:
        break
