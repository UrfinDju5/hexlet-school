def chunked(long: int,beadroll: any) -> any:
    result = []
    if len(beadroll) < long:
        result = [beadroll,]
        return result
    else:
        lst = beadroll[:]
        cash = beadroll[0:0]
        while len(lst) > 0:
            cash = lst[0:long]
            result.append(cash)
            lst = lst[long:]
        return result


print(chunked(2, ['a', 'b', 'c', 'd']))  # [['a', 'b'], ['c', 'd']]
print(chunked(3, ['a', 'b', 'c', 'd']))  # [['a', 'b', 'c'], ['d']]
print(chunked(3, 'foobar'))  # ['foo', 'bar']
print(chunked(10, (42,)))  # [(42,)]
print(chunked(2, ('a', 'b', 'c', 'd')))
print(type(('a', 'b', 'c', 'd')))