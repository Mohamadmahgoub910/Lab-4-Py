class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity
    # velocity from 0 to 200
    # FuelRate between 0 to 100

    def run(self, velocity, distance):
        # decreases the fuelRate
        # for i in range(self.fuelRate, 1, -10):
        #     distance = distance-10
        #     if self.fuelRate == 0:
        #         self.stop()
        #         distance = 20 - distance
        #         print(f"remain distance is {distance}")
        #     else:
        #         print("arrive in the time")
        if velocity >0 and velocity<200:
            distance = self.fuelRate -10
            if distance == 20 and self.fuelRate != 0:
                print ( "arrive in time ")
            elif self.fuelRate == 0:
                distance = 20 - distance
                print (f"remain distance is {distance}")
                self.stop()
            else:
                print ("else")
        else:
            print ( "velo should between 0 and 200")

    def stop(self):
        # make the velocity changed to 0
        self.velocity = 0
        #print notification with the remain distance
