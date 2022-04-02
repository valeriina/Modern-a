class Animal:
    def __init__(self, age, gender, group=""):
        self.age = age
        self.gender = gender
        self.group = group

    def sleep(self):
        print("{}: sleeps".format(self.name))

    def eat(self):
        print("The {} {}: eats".format(self.__class__.__name__, self.name))


class Pet(Animal):
    def __init__(self, name, owner, age, sex, is_vaccined: bool = False):
        # super().age = age
        # super().sex = sex
        super().__init__(age, sex)
        self.name = name
        self.owner = owner
        self.is_vaccined = is_vaccined

    def put_vaccine(self):
        self.is_vaccined = True

    def print_vaccine(self):
        print(self.is_vaccined)


class Dog(Pet):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def bark(self):
        print("{} barks: Bay bau".format(self.name))


dog1 = Dog("Sharo", "Ivan")
# print(dog1.is_vaccined)
dog1.put_vaccine()
print(dog1.is_vaccined)
dog1.bark()
dog1.sleep()

dog2 = Dog("Topcho", "Michail")
dog2.age = 2
print(dog2.age)
dog2.eat()