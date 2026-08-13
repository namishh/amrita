def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, int(input("how many terms of fibonacci to print: ")) + 1):
    print(fibonacci(i), end=" ")
print()