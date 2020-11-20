def fib_recursive(n):
    if (n <= 1):
        return n

    r = fib_recursive(n-2) + fib_recursive(n-1)

    return r

def fib_interative(n):
    last0 = 0
    last1 = 1

    for i in range(0, n-1):
        r = last0 + last1
        last0 = last1
        last1 = r

    return r

print(fib_interative(18))
print(fib_recursive(18))