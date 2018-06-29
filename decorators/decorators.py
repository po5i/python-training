
def double_decorator(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs) * 2
    return wrapper


def uppercase_decorator(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs).upper()
    return wrapper
