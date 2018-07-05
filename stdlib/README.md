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
- `pathlib`
- `pickle`, and the dangers of using it
- `multiprocessing`
- `json`
- unittest: `Mock`, `MagicMock`, `patch`
- `urllib`
- `sys`

## Run the exercise

```bash
python main.py
```

## Running the tests

```bash
python tests.py
```