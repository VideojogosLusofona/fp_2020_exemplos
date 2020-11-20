def factorial_recursive(n):
    if (n == 1):
        return 1

    r = n * factorial_recursive(n - 1)

    return r

def factorial_iterative(n):
    r = 1

    for i in range(1, n + 1):
        r = r * i

    return r

print(factorial_recursive(5))
print(factorial_iterative(5))