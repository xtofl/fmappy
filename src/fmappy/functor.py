
global fmap_vtable
fmap_vtable = {}


def fmap_for(type):
    def register_fmap(func):
        fmap_vtable[type] = func
        return func

    return register_fmap


def fmap(fn, data):
    return fmap_vtable[type(data)](fn, data)


apply = lambda fn, data: fn(data)


fmap_for(None)(lambda fn, data: None)
fmap_for(int)(apply)
fmap_for(str)(apply)
fmap_for(float)(apply)
fmap_for(bool)(apply)
fmap_for(list)(map)
fmap_for(tuple)(map)
fmap_for(dict)(lambda fn, data: { key: fn(value) for key, value in data.iteritems() })
