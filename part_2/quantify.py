def quantify(iterable, predicate):
    if predicate is None:
        predicate = bool
    return len([x for x in iterable if predicate(x)])


iterable = iter(["", 1, 0, (), [[]], [], {1: 2}])

print(quantify(iterable, None))
