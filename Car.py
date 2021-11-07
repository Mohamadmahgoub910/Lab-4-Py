class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        print("Run method \n Decreased the fuelRate")
        if car.fuelRate > 0:
            car.fuelRate -= 10
        elif car.fuelRate == 0:
            self.stop()
            print("stop function called based on fulerate value = 0 ")
        else:
            print(f"fuelRate decreased done")

    def stop(self):
        self.velocity = 0


car = Car("F16", 0, 20)
car.run(0, 0)
