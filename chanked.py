def chunked(long: int,beadroll: any) -> any:
    n = 0
    result = []
    if len(beadroll) < long:
        result = [beadroll,]
        return result
    else:
        for i in beadroll:
            while n < long:
                result = result[-1:] + i[:-1]
                n += 1
            result.extend(result)
        return result


#print(chunked(2, ['a', 'b', 'c', 'd']))  # [['a', 'b'], ['c', 'd']]
#print(chunked(3, ['a', 'b', 'c', 'd']))  # [['a', 'b', 'c'], ['d']]
#print(chunked(3, 'foobar'))  # ['foo', 'bar']
print(chunked(10, (42,)))  # [(42,)]