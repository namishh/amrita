p = float(input("Enter principal amount: "))
n = int(input("Enter years: "))

def calculate(p, n):
    if n == 1:
        return p
    return p * calculate(p, n-1)

print(calculate(p,n))