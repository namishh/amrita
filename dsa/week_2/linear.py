def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


a = [int(input(f"Entry #{i+1}: ")) for i in range(int(input("How many entries do you want to add: ")))]
x = int(input("item to find: "))
i = linear_search(a, x)
print(f"item found at index {i}" if  i >= 0 else "item not found")
