
class House:

    def __init__(self):
        self.numberOfFloor = 10

    def go_to_floor(self):
        for i in range(1, self.numberOfFloor + 1):
            print('Текущий этаж равен ', i)

my_house = House()
my_house.go_to_floor()

