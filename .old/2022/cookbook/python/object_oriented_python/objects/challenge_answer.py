

class Car:
    def __init__(self, driver, number):
        from random import uniform, randint
        self.driver = driver
        self.number = number
        self.acceleration = uniform(0.5, 1.5)
        self.max_speed = randint(5, 10)
        self.speed = 0
        self.total_distance = 0

    def tick(self, obstacle=False):
        if obstacle:
            self.speed -= self.speed/2
        elif self.speed < self.max_speed:
            potential_speed = self.speed + self.acceleration
            self.speed += self.acceleration if potential_speed < self.max_speed else self.max_speed-self.speed
        self.total_distance += self.speed
        return self.total_distance

    def draw(self):
        return self.number

class RaceTrack:
    def __init__(self, racers = 10, distance = 1000):
        import names
        self.cars = []
        for i in range(racers):
            self.cars.append(Car(names.get_full_name(), i))
        self.distance = distance
        self.racing = True
        self.track = []
        self.ticks = 0
    
    def tick(self):
        from random import randint
        from math import floor
        self.ticks += 1
        obstacle = True if randint(1, 100) == 1 else False
        for car in self.cars:
            car_distance = floor(car.tick(obstacle))
            if car_distance >= self.distance:
                print(f"{car.driver} in number {car.number} crossed the line to win!")
                return True
            else: print(f"{car.driver} in number {car.number} has traveled {car.total_distance}")
        return f"Round: {self.ticks}"
            
race_track = RaceTrack()

while (foo := race_track.tick()) != True:
    print(foo)

# for i in range(100000): 
#     if race_track.tick(): break
    



# c = Car("bob", 88)
# for i in range(100):
#     if i == 50: print(i, c.tick(True), c.draw(), c.speed, c.max_speed)
#     else: print(i, c.tick(), c.draw(), c.speed, c.max_speed)
    
    