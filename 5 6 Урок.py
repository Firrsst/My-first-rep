import random


class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.car = car
        self.job = job
        self.money = 100
        self.satiety = 50      # ситість, 0 - помер від голоду
        self.house = House()

    def work(self):
        if self.job is not None:
            if self.car is not None and self.car.drive():
                print(«Я поїхав на роботу»)
            else:
                print(«Я пішов на роботу»)
            print(f»Я працюю : {self.job.name}, заробив сьогодні {self.job.salary}»)
            self.money += self.job.salary
        else:
            print(«У мене немає роботи»)

    def shopping(self):
        print(«Шопінг:»)
        if self.money >= 10:
            amount = min(self.money // 10, 3)
            self.house.food += amount
            self.money -= amount * 10
            print(f»Я купив їжі: {amount}»)
        else:
            print(«Немає грошей на їжу»)

        if self.car is not None and self.car.fuel < 20:
            if self.money >= 30:
                self.money -= 30
                self.car.add_fuel()
                print(«Я заправив авто»)
            else:
                print(«Немає грошей на пальне»)

    def eat(self):
        if self.house.food > 0:
            self.house.food -= 1
            self.satiety = min(100, self.satiety + 30)
            print(«Я поїв»)
        else:
            print(«Немає їжі»)

    def cleaning(self):
        print(«Прибирання:»)
        rnd = random.randint(1, 2)
        if rnd == 1:
            print(«Я поганяв пилюку»)
            self.house.pollution -= 2
        else:
            print(«Я виконав генеральне прибирання»)
            self.house.pollution -= 5

        if self.house.pollution < 0:
            self.house.pollution = 0

    def info(self):
        print(f»Ім’я: {self.name}, гроші: {self.money}, ситість: {self.satiety}»)
        print(self.house)
        if self.car is not None:
            print(self.car)

    def live(self, day):
        print(f»\n=== День {day}, {self.name} ===«)
        self.satiety -= 20
        self.house.pollution += random.randint(1, 3)

        if self.satiety <= 0:
            print(f»{self.name} помер від голоду...»)
            return False

        if self.satiety < 40:
            if self.house.food == 0:
                self.shopping()
            self.eat()
        elif self.house.pollution >= 5:
            self.cleaning()
        elif self.job is not None:
            self.work()
            if self.house.food < 2:
                self.shopping()
        elif self.money <= 0:
            print(«Я відпочиваю вдома, немає грошей»)
        else:
            print(«Я відпочиваю вдома»)
            if self.house.food < 2:
                self.shopping()

        self.info()
        return True


class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60     # літри
        self.state = 100   # %

    def add_fuel(self):
        self.fuel += 20
        if self.fuel > 60:
            self.fuel = 60

    def drive(self):
        if self.fuel >= 5 and self.state > 0:
            self.fuel -= 5
            self.state -= 1
            return True
        return False

    def __str__(self):
        return f»Авто: {self.model}, пальне: {self.fuel} л, стан: {self.state}%»


class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        return f»Дім: їжа {self.food}, забруднення {self.pollution}»


class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


car = Car(«Tesla Model U13»)
job = Job(«Програміст», 100)

people = [
    Human(«Vasya», car=car, job=job),
    Human(«Petya»),
]

for day in range(1, 11):
    for human in people[:]:
        if not human.live(day):
            people.remove(human)

print(«\n=== Підсумок ===«)
for human in people:
    human.info()