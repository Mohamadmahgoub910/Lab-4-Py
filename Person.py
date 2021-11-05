class Person:
    def __init__(self, name, money=None, mood=None, healthRate=None):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        print(f" {self.name} can sleep ")
        if hours == 7:
            print("Happy")
        elif hours < 7:
            print("Tired")
        elif hours>7:
            print("Lazy")
        else:
            print("else")

    def eat(self,meals):
        print(f" {self.name} can eat ")
        if meals == 3:
            print("100% hth")
        elif meals == 2:
            print("75% hth")
        elif meals ==1:
            print("50% hth")

    def buy(self,items):
        print(f" {self.name} can buy ")
        if items == 1:
            self.money-10
        else:
            print("any Else")


P = Person("ali", 1200, "fight", "good")
P.sleep(7)
P.eat(3)
P.buy(1)
