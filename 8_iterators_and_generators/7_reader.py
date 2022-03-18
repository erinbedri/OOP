def read_next(*iterables):
    for iterable in iterables:
        for element in iterable:
            yield element