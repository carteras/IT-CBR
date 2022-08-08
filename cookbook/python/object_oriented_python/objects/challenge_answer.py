from random import randint

class DogPark:
    pass

class Dog:
    def __init__(self, name):
        self.name = name
        self.desire_to_go_home = 1

    def barking(self):
        pass

    def sniffing(self, dog_park):
        pass

    def playing(self, dog_park):
        pass

    def running(self):
        pass

    def whine(self):
        pass

    def go_home(self, dog_park):
        pass

    def check(self, dog_park):
        leaving = False
        if dog_park.dogs_left_in_park <= 0:
            self.desire_to_go_home += 1

        rnd = randint(1, 20)
        if rnd < self.desire_to_go_home:
            self.go_home(dog_park)
        rnd = randint(1, 20)
        if rnd < 5:
            self.sniffing(dog_park)
        elif rnd < 10:
            self.playing(dog_park)
        elif rnd < 15:
            self.running()
        elif rnd < 20:
            self.barking()
