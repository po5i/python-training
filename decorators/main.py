from functools import reduce

from decorators import double_decorator, bold_decorator, bread, vegetables


@double_decorator
def sum_all_numbers(limit):
    num_list = list(range(limit))
    return reduce(lambda x, y: x + y, num_list, 0)


@bold_decorator
def to_uppercase(text):
    return text.upper()


@bread
@vegetables('#tomatoes#', '~salad~')
def sandwich(food='-- ham --'):
    return(food)


if __name__ == '__main__':
    print('Get the sum of all numbers from 0 to 3 and double the result:')
    print(sum_all_numbers(4))

    print('Uppercase a string and wraps in HTML bold tag:')
    print(to_uppercase('hello'))

    print('Render a sandwich with parametrized ingredients')
    print('\n'.join(sandwich()))
