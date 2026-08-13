def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge(arr[:mid])
    right = merge(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


a = [int(input(f"Entry #{i+1}: ")) for i in range(int(input("How many entries do you want to add: ")))]
print(merge(a))
