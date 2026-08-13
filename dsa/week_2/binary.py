def binary(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


a = [int(input(f"Entry #{i+1}: ")) for i in range(int(input("How many entries do you want to add: ")))]
x = int(input("item to find: "))
i = binary(a, x)
print(f"item found at index {i}" if  i >= 0 else "item not found")
