# a generator that yields items instead of returning a list
def my_list_of(number):
    current = 0
    while current < number:
        yield current
        current += 1


def print_line(limit=40):
    print('-' * limit)


if __name__ == '__main__':
    n = 10
    print_line()
    print(f'Generate a list of {n} items')
    print(list(my_list_of(n)))

    n = 5
    print_line()
    print(f'Generate a list of {n} items')
    print(list(my_list_of(n)))

    print_line()
    print('Print each element in a loop')
    for x in my_list_of(n):
        print(x)

    print_line()
    print('Double each element using map')
    doubled = list(map(lambda x: x * 2, my_list_of(n)))
    print(doubled)

    print_line()
    print('Print each element using `next()`')
    my_generator = my_list_of(n)
    for x in range(n):
        print(next(my_generator))

    print_line()
    print('Try next when the generator stopped...')
    try:
        print(next(my_generator))
    except StopIteration as e:
        print(f'Generator is now consumed, got a StopIteration exception')
