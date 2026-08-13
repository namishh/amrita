def factorial(f):
    if f == 0 or f == 1:
        return 1
    return f * factorial(f-1)

print(factorial(int(input())))