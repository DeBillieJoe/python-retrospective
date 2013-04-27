def groupby(func, seq):
    result = {}

    for element in seq:
        result.setdefault(func(element), []).append(element)

    return result


def zip_with(func, *iterables):
    for args in zip(*iterables):
        yield func(*args)


def iterate(func):
    yield lambda ident: ident

    for stream_element in iterate(func):
        yield lambda arg: func(stream_element(arg))