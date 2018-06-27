# Duck Typing

The main idea of duck typing is that it doesn't matter what type the data is, if it does what I need I can use it. Since Python does not use interfaces, we can use multiple inheritance and duck typing. 

This example demonstrates that a `Car` instance can be injected any dependency that implements a `start()` method. After the car invokes the `turn_on()` method the engine starts and it prints how many pistons are running (should be the same as the number of cylinders).

# Magic Methods

Blah

## Run the exercise

```bash
python main.py
```

## Running the tests

```bash
python tests.py
```