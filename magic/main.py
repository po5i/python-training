class EngineBase:
    cylinders = 0
    active_pistons = 0

    def start(self):
        self.active_pistons = self.cylinders


class V6Engine(EngineBase):
    cylinders = 6


class V8Engine(EngineBase):
    cylinders = 8


class Car:
    def __init__(self, engine, *args, **kwargs):
        self._engine = engine

    def __repr__(self):
        return f'<Car with V{self._engine.cylinders} Engine>'

    def __str__(self):
        return f'V{self._engine.cylinders} Car'

    def turn_on(self):
        self._engine.start()

    def print_status(self):
        print(f'Number of pistons running: {self._engine.active_pistons}')


if __name__ == '__main__':
    print('Creating car with V6 engine...')
    car1 = Car(V6Engine())
    car1.turn_on()
    car1.print_status()

    print('Creating car with V8 engine...')
    car2 = Car(V8Engine())
    car2.turn_on()
    car2.print_status()

    #  __get__, __set__
