import functools
def get(path):
    @functools.wraps(fun)
    def decorator(fun)
        def wrapper(*args, **kw):
            return fun(*args, **kw)
        wrapper.__mathod__ = 'get'
        wrapper.__route__= path 
        return wrapper
    return decorator
