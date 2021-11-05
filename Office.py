from Employee import *
class Office(Employee):
    employeesNum = 0
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
        Office.employeesNum +=1

    def getAllEmployees(self):
        return list(self.employees)

    def getEmployee(self,empId):
        if self.id == empId:
            print (f" emp name is {self.name}")
        else :
            print ("sorry not found")
    def hire(self,Empname):
        print (f"{Empname} is hired")

    def fire(self, EmpId):
        if self.id == empId:
            print(f"{self.name} is fired")
        else:
            print("sorry not found")

    def checkLate(self,empId, moveHour):
        if self.id == empId:
            if moveHour == 9:
                print (f" +10 increase {self.reward(empId,10)})
            else:
                print(f" -10 decreased {self.deduct(empId,10)})
        else:
            print("sorry not found")

        def reward(self, empId, reward):
            if self.id == empId:
                self.money = self.money + reward
            else:
                print("sorry not found")

    def deduct(self,empId , deduction):
        if self.id == empId:
            self.money = self.money - deduction
        else:
            print("sorry not found")
    def reward(self,empId,reward):
        if self.id == empId:
            self.money = self.money + reward
        else:
            print("sorry not found")
    @staticmethod
    def totalLate(targetHour , moveHour, distance, velocity):
        if velocity >0 and velocity <200:
            if moveHour == 9 :
                print("just in time")
            elif moveHour < 9:
                print ("late")
                distance = (velocity/moveHour) - targetHour
                print (f"you are away from target with{distance}km")
            else:
                print("Some thing else")
        else :
            print (f"velo should max eq 200")
    def changEmpsNum(self,num):
        print (f" office employees are {Office.employeesNum})