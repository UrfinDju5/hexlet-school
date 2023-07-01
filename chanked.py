def chunked(size, source):
    result = []
    index = 0
    while index < len(source):
        result.append(source[index:index + size])
        index += size
    return result


print(chunked(2, ['a', 'b', 'c', 'd']))  # [['a', 'b'], ['c', 'd']]
print(chunked(3, ['a', 'b', 'c', 'd']))  # [['a', 'b', 'c'], ['d']]
print(chunked(3, 'foobar'))  # ['foo', 'bar']
print(chunked(10, (42,)))  # [(42,)]
print(chunked(2, ('a', 'b', 'c', 'd')))
print(type(('a', 'b', 'c', 'd')))