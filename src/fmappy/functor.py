
global fmap_vtable
fmap_vtable = {}


def register_functor(type, func):
    fmap_vtable[type] = func
    return func


def fmap(fn, data):
    try:
        functor = fmap_vtable[type(data)]
    except KeyError as e:
        raise TypeError(f"{type(data)} is not registered as a Functor") from e
    return functor(fn, data)


apply = lambda fn, data: fn(data)
construct_from_mapped = lambda fn, data: type(data)(map(fn, data))


register_functor(None, lambda fn, data: None)
register_functor(int, apply)
register_functor(str, apply)
register_functor(float, apply)
register_functor(bool, apply)
register_functor(list, construct_from_mapped)
register_functor(tuple, construct_from_mapped)
register_functor(dict, lambda fn, data: { key: fn(value) for key, value in data.items() })
