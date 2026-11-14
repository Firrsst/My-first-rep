class Student:
    def __init__(self, name, age, height, money=0):
        self.name = name
        self.age = age
        self.height = height
        self.money = money

    def setAge(self, age):
        if age > 100:
            return
        self.age = age

    def grow_up(self, grow):

        new_height = self.height + grow

        if new_height > 200:
            self.height = 200
        else:
            self.height = new_height

    def setMoney(self, money):
        if money < 0:
            return
        self.money = money

    def change_money(self, amount):

        new_money = self.money + amount

        if new_money < 0:
            self.money = 0
        else:
            self.money = new_money

    def info(self):
        print(f»Ім’я {self.name}, вік {self.age}, зріст {self.height}, гроші {self.money}»)


st1 = Student(«Vasya», 15, 170, 100)
st1.info()

st2 = Student(«Petya», 16, 180)
st2.info()