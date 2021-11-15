# import virtualenv
# import pygame
# import flask

# To create a virtual Environment
# virtualenv myname
# virtualenv virt2

# to activate a virtualenv
# for Windows
# .\myname\scripts\activate.ps1
# for linux
# ./myname/bin/activate

# to install a module through command prompt
# pip install flask
# pip install pygame

# append the input to a file
# pip freeze > requirement.txt

# to create a similar Environment in new virtualenv
# pip install - r requirement.txt     # -r stands for recursively

# to deactivate virtualenv simply type
# deactivate

# name = input("enter your name :")
# marks = int(input("enter your marks :"))
# phonenumber = int(input("enter your phone number :"))


# def student(name, marks, phonenumber):

#     print("the name of the student is {0}, his marks are {1} and phone number is {2}".format(
#         name, marks, phonenumber))


# student1 = student(name, marks, phonenumber)
# print(student1)




# list=[str(i*5) for i in range(1,11)]
# print(list)

# vertical="\n".join(list)
# print(vertical)


lis=[25,3,61,4,58,95,1,26,3,6,45,2]
# sum = lambda a,b:a+b

fil=filter(lambda a: a%5==0, lis)
print(list(fil))
print(min(lis))

from functools import reduce
max=reduce(max,lis)
print (max)