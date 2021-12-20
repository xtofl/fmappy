
global fmap_vtable
fmap_vtable = {}


def fmap_for(type):
    def register_fmap(func):
        fmap_vtable[type] = func
        return func

    return register_fmap


def fmap(fn, data):
    try:
        functor = fmap_vtable[type(data)]
    except KeyError as e:
        raise TypeError(f"{type(data)} is not registered as a Functor") from e
    return functor(fn, data)


apply = lambda fn, data: fn(data)
construct_from_mapped = lambda fn, data: type(data)(map(fn, data))


fmap_for(None)(lambda fn, data: None)
fmap_for(int)(apply)
fmap_for(str)(apply)
fmap_for(float)(apply)
fmap_for(bool)(apply)
fmap_for(list)(construct_from_mapped)
fmap_for(tuple)(construct_from_mapped)
fmap_for(dict)(lambda fn, data: { key: fn(value) for key, value in data.items() })
