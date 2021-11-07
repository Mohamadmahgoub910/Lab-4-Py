from Employee import *
import json


class Office:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

    def gAEmpID(self):
        print(f"all id emps are {employee.employeesNum}")
        print("Done in gAEp")

    def gEmpID(self, EmpID):
        print(f" Emp id based in given {employee.id} ")
        print("Done in gAEp")

    def hire(self, empId):
        print(f"employee {employee.id} is hired")
        print("Done in hire!")

    def fire(self, empId):
        print(f"employee {employee.id} is fired")
        print("Done in fire!")

    def deduct(self, empId, deduction):
        employee.salary -= deduction
        print(f"employee {employee.id} deduct succsess and all money remains are {employee.salary}")
        print("Done in deduct()!")

    def reward(self, empId, reward):
        employee.salary += reward
        print(f"employee {employee.id} reward succsess and  money are {employee.salary}")
        print("Done in rewardFN()!")

    @staticmethod
    def CalcLate(targetH, moveH, Dist, Velo):
        moveH = ((Velo * Dist) / 60)
        if targetH == moveH:
            print("Arrived on time ")
            print("Done in CalcLateFN!")
        else:
            print(f"you are late {targetH - moveH}")
            print("Done in CalcLateFN!")
    # def __str__(self):
    #     print(f"{self.name} , {self.employee} , {self.gEmpID()}"
    #           f"{self.gAEmpID()}, {self.hire()}, {self.fire()}")
office = Office(name="ITI", employee=23)
office.gAEmpID()
office.gEmpID(1)
office.hire(1)
office.fire(1)
office.deduct(1, 10)
office.reward(1, 10)
office.CalcLate(9, 7, 20, 200)
with open('data.json', 'w') as f:
    json.dump(office.__dict__, f)
    print(office)