import datetime
import time
import decimal
import math
import queue
import itertools
import functools
import logging
from collections import namedtuple
from collections import OrderedDict


def example_datetime():
    now = datetime.datetime.now()
    fourth_of_july = datetime.datetime(2018, 7, 4)
    delta = now - fourth_of_july
    return delta.days


def example_namedtuple():
    Coordinate = namedtuple('Coordinate', 'latitude, longitude, altitude')
    data = {
        'latitude': -0.17511714727665964,
        'longitude': -78.48592701759645,
        'altitude': 2800
    }
    office = Coordinate(**data)
    return office


def example_ordered_dict():
    d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    o = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    o.move_to_end('apple')
    return o


def example_queue():
    output = []
    q = queue.LifoQueue()

    for i in range(5):
        q.put(i)

    while not q.empty():
        output.append(q.get())
    return output


def example_decimal():
    decimal.getcontext().prec = 42
    a = decimal.Decimal(0.1)
    b = decimal.Decimal(0.2)
    return a + b


def example_math():
    radius = 10
    area = math.pi * math.pow(radius, 2)
    return area


def example_itertools():
    numbers = range(1, 4)
    permutations = itertools.permutations(numbers, 2)
    return list(permutations)


def example_functools():
    def power(base, exponent):
        return base ** exponent
    square = functools.partial(power, exponent=2)
    return square(10)


def example_logging():
    logger = logging.getLogger('python_training')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.info('Going to sleep for a sec, good night!')
    time.sleep(1)
    logger.info('Waking up!')


if __name__ == '__main__':
    print(f'Days since 2018s 4th of July: {example_datetime()}')
    print(f'Office coordinates: {example_namedtuple()}')
    print(f'Sorted Fruits (apple at the end): {example_ordered_dict()}')
    print(f'LIFO stack extracted elements: {example_queue()}')
    print(f'Decimal precision 42 sum 0.1 + 0.2 = {example_decimal()} but float is: {0.1 + 0.2}')
    print(f'Area for a r=10 circle: {example_math()}')
    print(f'Permutations of the first 3 numbers: {example_itertools()}')
    print(f'Using partial() to wrap power(), 10² = {example_functools()}')
    print('Logging everything')
    example_logging()
