from Person import *
class Employee(Person):
    def __init__(self, id, name, car, email, distanceToWork):
        super().__init__(name)
        self.id = id
        self.car = car
        self.email = email
        self.distanceToWork = distanceToWork

    def __str__(self):
        return f"{self.id} , {self.name},{self.car}"

    def work(self, hours):
        if hours == 8:
            print("Happy")
        elif hours > 8:
            print("Tired")
        elif hours < 8:
            print("Lazy")
        else:
            print("else")

    def drive(self, distance):
        # i can't understand the logic he asked.
        # is it?
        # Give the order to run method and give it distance and velocity
        return distance * 1 * 1

    def refuel(self, gazAmount=100):
        # add gasAmount to fuelRate
        return gazAmount

    def sendMail(self, to, subject, msg, receiverName):
        pass


Emp = Employee(id=1, name="Employee", car="BMW", email="emp@emp.com", distanceToWork=120)
print(Emp)
