def fib(n: int) -> int:
    fi = (1 + 5 ** (0.5))/2
    return int((fi ** n - ((- fi) ** - n)) / 5 ** (0.5))



print(fib(3)) # 2
print(fib(5)) # 5
print(fib(10))  # 55

# BEGIN
'''def fib(num):
    if num == 0:
        return 0

    if num == 1:
        return 1

    first, second = 0, 1
    result = first + second

    index = 2
    while index <= num:
        result = first + second
        first, second = second, result

        index += 1

    return result'''
# END