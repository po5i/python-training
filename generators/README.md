# Generators

Python provides an optimized way to create iterators. A generator is a function that returns an iterator object which can be iterated one value at a time. Generator builds the iterator in memory every time it's needed instead of build the whole list at the start.

In this exercise, I've created a function `my_list_of(number)` which returns a generator that builds a list of max `number` consecutive items.

Three approaches are used to iterate this generator. A `for` loop, a `map` function and the `next()` function. Note that when using `next()` function, a `StopIteration` exception is raised when the generator already reached the end of the iteration.

## Run the exercise

```bash
python main.py
```

## Running the tests

```bash
python tests.py
```