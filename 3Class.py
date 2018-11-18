###Assignment 3
#A.
class Dog:
    def __init__(self,age,name):
        self.age = age
        self.name = name

def main():
    rexi = Dog(5,'REXI')
    print(rexi.name)

if __name__ == '__main__':
    main()

#B.

#stevie.age = 3

#c.
class car:

    @staticmethod
    def start():
        print("START")


def main():
    car.start()


if __name__ == '__main__':
    main()

#D.

class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

class Huskey(Dog):
    def __init__(self, age, name):
        super().__init__(age, name)

    def howl(self):
        print("ahooo")

if __name__ == "__main__":
    DOGI=Huskey(5,"DOGI")
    DOGI.howl()

#E.
class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

class Huskey(Dog):
    def __init__(self, age, name):
        super().__init__(age, name)

    def howl(self):
        print("ahooo")

class BlackHuskey(Huskey):
    def __init__(self, age, name):
        super().__init__(age, name)

    def return_color(self):
        return "BLACK"

if __name__ == "__main__":
    DOGI=BlackHuskey(5,"DOGI")
    DOGI.howl()
    print(DOGI.return_color())

#F.

class Dog:

    @staticmethod
    def bark():
         print(132)

if __name__ == "__main__":
    Dog.bark()

#G1.

import array as arr

if __name__ == "__main__":

    a = arr.array("i",[100,200,300])
    for temp_num in a:
        print(temp_num)

#G2.

class Dog:
    def __init__(self,age,name):
        self.age = age
        self.name = name

if __name__ == "__main__":

    Arr1 = Dog(5, "John")
    Arr2 = Dog(8, "Joe")
    Arr3 = Dog(12, "George")

    dogs_list = [Arr1, Arr2, Arr3]

    for x in range (len(dogs_list)):
        print(dogs_list[x].name)