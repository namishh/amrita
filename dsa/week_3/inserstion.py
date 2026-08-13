def isort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


a = [int(input(f"Entry #{i+1}: ")) for i in range(int(input("How many entries do you want to add: ")))]
print(isort(a))
