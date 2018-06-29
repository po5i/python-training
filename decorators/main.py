from functools import reduce

from decorators import double_decorator, uppercase_decorator


@double_decorator
def sum_all_numbers(limit):
    num_list = list(range(limit))
    return reduce(lambda x, y: x + y, num_list, 0)


@uppercase_decorator
def surround(text):
    return f'--- {text} ---'


if __name__ == '__main__':
    print(sum_all_numbers(4))
    print(surround('hello'))
