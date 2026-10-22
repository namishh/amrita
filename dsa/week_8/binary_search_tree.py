class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)
        if root.value == value:
            return root

        if root.value < value:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)

        return root

    def traverse_inorder(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return

        self._inorder(node)

    def _inorder(self, node):
        if node is None:
            return

        self._inorder(node.left)
        print(node.value, end=" ")
        self._inorder(node.right)

    def search(self, root, value):
        if root is None or root.value == value:
            return root
        if root.value < value:
            return self.search(root.right, value)

        return self.search(root.left, value)

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

            if root.right is None:
                return root.left

            curr = root.right
            while curr.left is not None:
                curr = curr.left
            root.value = curr.value
            root.right = self.delete(root.right, curr.value)
        return root


b = BinarySearchTree()

while True:
    x = input("1. Insert | 2. Remove | 3. Traverse | 4. Search | 5. Exit: ")
    if x == '1':
        value = int(input("Enter value to insert: "))
        b.root = b.insert(b.root, value)
    elif x == '2':
        value = int(input("Value to remove: "))
        b.root = b.delete(b.root, value)
    elif x == '3':
        b.traverse_inorder()
        print()
    elif x == '4':
        value = int(input("Value to search for: "))
        print("Found" if b.search(b.root, value) else "Not Found")
    elif x == '5':
        break
    else:
        print("Invalid choice")
