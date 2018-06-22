# Inheritance

Python supports multiple inheritance, which leads to the diamond problem. Let's say we have a class A with a print method `method_print()`, later we can create two child classes B and C that inherits A. Finally we create a class D that inherits both B and C. Every class overrides its `method_print()`.

Naturally, if we decide to invoke the parent's `method_print()` at the end of each one, the method from class A will be invoked twice. To solve this, python offers the `super()` function which implements the Method Resolution Order (MRO) and it's based on the "[C3 superclass linearisation algorithm](https://en.wikipedia.org/wiki/C3_linearization)", so the tree structure is broken down in a linear order.

## Run the exercise

```bash
python main.py
```

## Running the tests

```bash
python tests.py
```