class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def __str__(self):
        return (f"Data of Person is {self.name} , {self.money} , {self.mood} , {self.healthRate}")

    def sleep(self, hours):
        if hours == 7:
            print("Happy!")
        elif hours < 7:
            print("Tired!")
        elif hours > 7:
            print("Lazy!")
        else:
            print(f"{hours} doesn't here")

    def eat(self, meals):
        if meals == 3:
            print("100% hth")
        elif meals == 2:
            print("75% hth")
        elif meals == 1:
            print("50% hth")

    def buy(self, items):
        if items:
            self.money -= 10
            print(
                f"You bought something so,\n decreased your money successful \n rest of money {self.money} \n be happy:)")

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


personobj = Person(name="ali", money=1000, mood="Notgood", healthRate="fine")
# print(personobj)
# print("sleep fn ")
# personobj.sleep(2)
# print("eat fn ")
# personobj.eat(3)
# print("buy fn ")
# personobj.buy(1)
# print("work fn ")
# personobj.work(8)
print("sendmail fn see file  ")
personobj.sendMail("FROM:- aliaa@gmai.com\n", "TO:- ali@gmail.com\n", "Subject:- come to eat \n",
                   "Msg:- Hi Bro the food close to finish come faster to eat \n Regards :)")
