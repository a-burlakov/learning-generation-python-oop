def intersperse(iterable, delimiter):

    if not iterable:
        return

    started = False
    prev_item = None
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            if not started:
                started = True
                prev_item = item
                continue
            yield prev_item
            yield delimiter
            prev_item = item
        except StopIteration:
            yield prev_item
            break


data = intersperse(
    [
        "John Warner Backus",
        5,
        "Niklaus Emil Wirth",
        True,
        "Lawrence Gordon Tesler",
        None,
        {1, 2, 3},
        {"hello": "world"},
    ],
    "—",
)
print(list(data))
# ['John Warner Backus', '—', 5, '—', 'Niklaus Emil Wirth', '—', True, '—', 'Lawrence Gordon Tesler', '—', None, '—', {1, 2, 3}, '—', {'hello': 'world'}]
# ['John Warner Backus', '—', 5, '—', 'Niklaus Emil Wirth', '—', True, '—', 'Lawrence Gordon Tesler', '—', {1, 2, 3}, '—', {'hello': 'world'}]
