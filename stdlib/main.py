import datetime
import time
import decimal
import math
import queue
import itertools
import functools
import logging
import os
import pickle
import json
import sys

from collections import namedtuple
from collections import OrderedDict
from pathlib import Path
from multiprocessing import Pool
from urllib.parse import urlparse
from unittest.mock import MagicMock


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


def example_os():
    base = os.path.dirname(os.path.realpath(__file__))
    file_name = f'{base}/sample.txt'

    with open(file_name, 'w') as f:
        print(f)
        f.write('Something')

    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return f.read()


def example_path():
    p = Path('/etc')
    q = p / 'hosts'
    return os.name == 'posix' and q.exists()


def example_pickle(arg):
    print(f'Serializing {arg} in process {os.getpid()}')
    f = pickle.dumps(example_datetime)
    return f


def example_unpickle(data):
    return pickle.loads(data)


def example_multiprocessing():
    functions = [example_datetime, example_namedtuple, example_ordered_dict]
    pool = Pool(processes=3)
    return pool.map(example_pickle, functions)


def example_json():
    data = {
        "foo": "bar"
    }
    return json.dumps(data, indent=4)


def example_urllib():
    o = urlparse(
        'https://domain.com:3900/path/to/resource.html?foo=bar#anchor')
    return o


def example_sys():
    return f'{sys.version_info.major}.{sys.version_info.minor}'


def example_mock():
    thing = MagicMock()
    thing.__str__.return_value = 'My mock'
    thing.some_method.return_value = 42
    return thing


if __name__ == '__main__':
    print(f'\nDays since 2018s 4th of July: {example_datetime()}')
    print(f'\nOffice coordinates: {example_namedtuple()}')
    print(f'\nSorted Fruits (apple at the end): {example_ordered_dict()}')
    print(f'\nLIFO stack extracted elements: {example_queue()}')
    print(f'\nDecimal precision 42 sum 0.1 + 0.2 = {example_decimal()}'
          f' but float is: {0.1 + 0.2} instead')
    print(f'\nArea for a r=10 circle: {example_math()}')
    print(f'\nPermutations of the first 3 numbers: {example_itertools()}')
    print(f'\nUsing partial() to wrap power(), 10² = {example_functools()}')
    print('\nLogging everything')
    example_logging()
    print(f'\nCreate file and write something like: {example_os()}')
    print(f'\nDoes /etc/hosts file exists in UNIX?: {example_path()}\n')
    data = example_pickle(example_datetime)
    print(f'\nBinary representation of `example_datetime`: {data}')
    f = example_unpickle(data)
    print(f'\nDeserializing (should match first example): {f()}')
    print('\nMultithreading serialization of three functions')
    example_multiprocessing()
    print(f'\nEncode a dict to JSON string: {example_json()}')
    print(f'\nParse an URL: {example_urllib()}')
    print(f'\nRunning Python {example_sys()}')
    thing = example_mock()
    print(f'\nMocking thing.some_method() =  {thing.some_method()}')
