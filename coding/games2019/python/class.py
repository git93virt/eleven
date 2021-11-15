# class programmer:
#     company = "microsoft"

# a=programmer()


# class calculator:
#     def __init__(self, num):
#         self.number = num

#     def square(self):

#         print(f"the square of {self.number} is {self.number**2}")

#     def squareroot(self):

#         print(f"the square root of {self.number} is {self.number**0.5}")

#     def cube(self):

#         print(f"the cube of {self.number} is {self.number**3}")

#     @staticmethod
#     def greet():
#         print(f"hello this is a claculator")


# a = calculator(4)
# a.greet()
# a.square()
# a.squareroot()
# a.cube()


# class sample:
#     a = "raj"


# object = sample()
# object.a = "vijay"
# print(object.a)
# print(sample.a)

# #
# class train:
#     def __init__(self, trainName, trainSeat, trainFair):

#         self.company = "indian railways"
#         self.trainname = trainName
#         self.trainseat = trainSeat
#         self.trainfair = trainFair

#     def bookticket():
#         pass

#     def status(self):
#         print(
#             f"{self.company} train {self.trainname} available seats are {self.trainseat}")

#     def info(self, passenger):
#         self.passen = passenger
#         print(f"{self.company} train {self.trainname} passanger {self.passen} your train has been confirmed.And the fair is {self.trainfair}")

#     def __str__(self):
#         return "object"


# a = train("indian express", "22", "190")
# a.status()
# a.info("raj")

# print(a)


# class a:
#     company = "atom"


# class b:
#     company = "ball"


# class c(b, a):
#     # company = "milk"
#     pass


# x = c()
# print(x.company)


# class c2dvec:
#     pass
# class th3dvec(c2dvec):
#     pass


# class animal:
#     pass


# class pets(animal):
#      color="white"
#     #  print ("new")


# class dogs(pets):
#     @staticmethod
#     def bark():
#         print("bow bow bow bow")


# a = animal()
# p = pets()
# # d = dogs()
# # d.bark()


# from ast import increment_lineno


# class employee:
#     salary = 3000
#     increment = 1.5

#     @property
#     def salaryafterincrease(self):
#         return self.salary * self.increment

#     @salaryafterincrease.setter
#     def salaryafterincrease(self, sai):
#         self.increment = sai/self.salary


# e = employee()
# print(e.salaryafterincrease)
# print(e.increment)
# e.salaryafterincrease = 6000
# print(e.increment)


# class complex:
#     def __init__(self, i, r):
#         self.real = r
#         self.imagenary = i

#     # def __add__(self, c):
#     #     return complex(self.real + c.real, self.imagenary+c.imagenary)


# # (ac−bd) + (ad+bc)i

#     def __mul__(self, c):
#         newmul = self.real*c.real-self.imagenary*c.imagenary
#         imamul = self.real*c.imagenary+self.imagenary*c.real
#         return complex(newmul,imamul)

#     def __str__(self):
#         return f"{self.real}+{self.imagenary}i"


# o = complex(6, 9)
# s = complex(3, 8)
# # add = o+s
# # print(add)
# print(o*s)


# class vector:
#     def __init__(self) -> None:
#         pass


from ast import increment_lineno
from os import name
from typing import AsyncGenerator


class programmer:  # this is class creation
    company = "microsoft"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print(f"the name of the employee is {self.name}")
        print(f"the age of the employee is {self.age}")
        print(f"the name of the company is {self.company}")


raj = programmer("raj", 28)  # this is object instance
# print(harry.company)
raj.detail()


class calculator:
    @staticmethod
    def greet():
        print("hello wlecome to the new world")

    def square(self, a):

        return a*a

    def cube(self, a):

        print(a*a*a)

    def squareroot(self, a):
        return a*a


raj = calculator()
raj.greet()
raj.cube(5)
raj.square(5)


class a:
    attribute = "a"


obj = a()
obj.attribute = "new"
print(obj.attribute)


class train:
    railways = "indian railways"

    def ticketBook():
        pass

    def getStatus():
        pass

    def fairInfo():
        pass
    

person = train()
# person.getStatus()

class employee:
    company="nokia"
    salary=2500
    bouns=200
    totalsalary=salary+bouns
 

raj=employee()
print (raj.totalsalary)
raj.totalsalary=3000 
print(raj.totalsalary)
print(raj.salary)


class animal:
    pass
class pets(animal):
    pass
class dogs(pets):
    def bark(self):
        print("bow bow bwo")

dog=dogs()
dog.bark()
print (dog)


class employee:
    salary=200
    increment=3000
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sal):
       self.increment=sal/self.salary

raj=employee()
print(raj.salaryAfterIncrement)
print(raj.increment)
raj.salaryAfterIncrement=5000
print(raj.increment)






