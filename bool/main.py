class House:
    doors = 0
    windows = 0

    def __init__(self, doors, windows, *args, **kwargs):
        self.doors = doors
        self.windows = windows

    def __bool__(self):
        return self.doors > 0 and self.windows > 0


if __name__ == '__main__':
    house = House(2, 4)
    if house:
        print('This is a normal house')
    else:
        print('A normal house should have doors and windows ¯\_(ツ)_/¯')
