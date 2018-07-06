# Standard Library

- `datetime`
  - Objects of these types are immutable.
  - There are two kinds of date and time objects: “naive” and “aware” of timezones.
- `collections`
  - The `namedtuple()` and `OrderedDict` are the most remarcable helpers of this library IMO.
  - `namedtuple()` allows to create tuple subclasses with named fields.
  - `OrderedDict` same as `dict` but it remembers the order elements were inserted.
- `Queue`
  - Provides data structures suitable for multi-threaded programming (FIFO, LIFO, Priority).
  - Locking is handled for the caller, so many threads can work with the same Queue instance.
- `Decimal`
  - Has advantages over float type for example exactness, significant places.
  - A decimal number is immutable. It has a sign, coefficient digits, and an exponent.
  - Includes a lot of useful rounding rules.
- `Math`
  - Provides access to the mathematical functions defined by C.
  - Only for non complex numbers.
  - The module is always available.
- `itertools`
  - Building blocks were inspired by constructs from APL, Haskell, and SML.
  - This module is focused on being fast and memory efficient.
- `functools`
  - This module includes higher-order functions.
  - Any callable object can be treated as a function for the purposes of this module.
- `logging`
  - Implement a flexible logging for applications.
  - Provides handlers, filtering and formatting tools.
- `os`
  - Useful tools for reading and writing files in the OS.
  - Supports OS paths.
- `pathlib`
  - Allows to use classes representing filesystems paths.
  - Paths are divided between Pure and Concrete paths (the earlier does not provide I/O operations).
- `pickle`
  - Serialization module in Python, converts any object in bytestream.
  - Is not secure against erroneous or maliciously constructed data.
  - Never unpickle data received from an untrusted source.
- `multiprocessing`
  - Support spawning process as threading module.
  - Introduces `Pool` class that provides data paralellism.
- `json`
  - Super useful module to encode and decode basic python objects.
- unittest: `Mock`, `MagicMock`, `patch`
  - `Mock` allows to replace parts of your system with attributes and methods.
  - `MagicMock` is a subclass of `Mock` that includes default implementations of magic methods.
  - `patch` is a mock decorator which limit the mocking scope to a module or class function.
  - Any mock can return a value using `return_value` and have a function to be called (or exception raised) by using `side_effect`.
- `urllib`
  - Tools to work with URLs.
  - `urllib.parse.urlparse` is a super useful function to parse url in components.
- `sys`
  - Provides access to variables and functions used by the interpreter.

## Run the exercise

```bash
python main.py
```

## Running the tests

```bash
python tests.py
```