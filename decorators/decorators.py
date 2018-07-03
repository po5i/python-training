
def double_decorator(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs) * 2
    return wrapper


def bold_decorator(f):
    def wrapper(*args, **kwargs):
        return f'<strong>{f(*args, **kwargs)}</strong>'
    return wrapper


def bread(f):
    def wrapper():
        top = '</"""""""\>'
        bottom = '<\_______/>'
        return [top] + f() + [bottom]
    return wrapper


def vegetables(ingredient1, ingredient2):
    def dec(f):
        def wrapper():
            return [ingredient1, f(), ingredient2]
        return wrapper
    return dec
