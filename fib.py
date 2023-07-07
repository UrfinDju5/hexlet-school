def fib(n: int) -> int:
    return int((((1 + 5 ** (0.5))/2) ** n - ((1 - 5 ** (0.5))/2) ** n) / 5 ** (0.5))



print(fib(3)) # 2
print(fib(5)) # 5
print(fib(10))  # 55