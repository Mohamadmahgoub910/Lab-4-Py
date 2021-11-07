from Person import *
from Car import *


class Employee(Person):
    employeesNum = 0

    def __init__(self, id, car, email, salary, distanceToWork):
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        Employee.employeesNum += 1

    def reful(self, gazAmount):
        car.fuelRate = gazAmount
        print("reful assign value success \n Done in reful() ")

    def drive(self, distance):
        print("drive call")
        self.drive_obj = Car.run(self, velocity=3, distance=3)
        print("Done")

    def work(self, hours):
        if hours == 8:
            print("Happy!")
        elif hours > 8:
            print("Tired!")
        elif hours < 8:
            print("Lazy")
        else:
            print("else")

    def sendMail(self, to, receiverName, sub, msg):
        f = open("mail.txt", "a")
        f.write("|".join([to, receiverName, sub, msg]))
        f.write('\n')
        f.close()

    @classmethod
    def CalcNumsEmp(cls):
        cls.employeesNum += 1
        print(f" EmpsNum are {cls.employeesNum}")


employee = Employee(1, "f16", "medo@medo.com", 1000, 20)
employee2 = Employee(2, "f16", "medo@medo.com", 1000, 20)
# employee.drive(20)
employee.reful(0)
