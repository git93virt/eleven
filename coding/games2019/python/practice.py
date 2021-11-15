# fruits0 = input("enter a seven fruit name 0 : \n ")
# fruits1 = input("enter a seven fruit name 1 : \n ")
# fruits2 = input("enter a seven fruit name 2 : \n ")
# fruits3 = input("enter a seven fruit name 3 : \n ")
# fruits4 = input("enter a seven fruit name 4 : \n ")
# fruits5 = input("enter a seven fruit name 5 : \n ")
# fruits6 = input("enter a seven fruit name 6 : \n ")


# fruitlist = [fruits0, fruits1, fruits2, fruits3, fruits4, fruits5, fruits6]

# print(fruitlist)


# student1 = int(input("student1 marks : \n"))
# student2 = int(input("student2 marks : \n"))
# student3 = int(input("student3 marks : \n"))
# student4 = int(input("student4 marks : \n"))
# student5 = int(input("student5 marks : \n"))
# student6 = int(input("student6 marks : \n"))


# marks = [student1, student2, student3, student4, student5, student6]
# marks.sort()
# print(marks)


# tup = (1, 25, 2, 53, 6)
# tup[0] = 25
# print(tup)


# a = (7, 0, 8, 0, 0, 9)
# print(a.count(0))


# problem number 2


# dicthindi = {
#     "kya": "what",
#     "aur": "and",
#     "ab": "now"
# }
# print("find the meaning of these words: ", dicthindi.keys())
# hindi = (input("enter your word :\n"))

# print("meaning is : ", dicthindi.get(hindi))


# print(dicthindi.values())

# print(dicthindi)

# problem

# num1 = int(input("enter number1 : "))
# num2 = int(input("enter number2 : "))
# num3 = int(input("enter number3 : "))
# num4 = int(input("enter number4 : "))
# num5 = int(input("enter number5 : "))
# num6 = int(input("enter number6 : "))
# num7 = int(input("enter number7 : "))
# num8 = int(input("enter number8 : "))


# user = {num1, num2, num3, num4, num5, num6, num7, num8}


# print(user)

# problem

# sett = {18, "18"}


# print(len(sett))

# print(sett)


# problem

# dic = {}

# friend1 = input("your fav lang  raj: \n ")
# friend2 = input("your fav lang rajt : \n ")
# friend3 = input("your fav lang narad: \n ")
# friend4 = input("your fav lang navn : \n ")

# dic["raj"] = friend1
# dic["rajat"] = friend2
# dic["narad"] = friend3
# dic["navn"] = friend4

# print(dic)

# problem

# s = {8, 7, 12, "raj", [1, 2]}
# print(s)

# problem

# num1 = int(input("enter firstno user1 :"))
# num2 = int(input("enter secondno user1 :"))
# num3 = int(input("enter thirdno user1 :"))
# num4 = int(input("enter fouthno user1 :"))

# if (num1 > num2):
#     print("im greater num1 ", num1)
# elif(num2 > num3):
#     print("im greater num2", num2)
# elif(num3 > num4):
#     print("im greater num3", num3)
# else:
#     print("im great num4", num4)


# problem

# if (num1 > num2):
#     s1 = num1
# else:
#     s1 = num2

# if (num3 > num4):
#     s2 = num3
# else:
#     s2 = num4

# if (s1 > s2):
#     print("im greater my number is " + str(s1))
# else:
#     print("im greater than any other no" + str(s2))

# problem


# sub1 = int(input("enter eng mark  :"))
# sub2 = int(input("enter math mark :"))
# sub3 = int(input("enter hindi mark :"))

# if(sub1 > 33 or sub2 > 33 or sub3 > 33):
#     print("fail !! your have less than 33  in one of subjects")
# elif((sub1+sub2+sub3)/3 < 40):
#     print("fail!! you have less than 40 percentage")
# else:
#     print("you are pass")

# problem

# user = input("enter your name : \n")
# cou = len(user)

# if(cou < 6):
#     print("character is less than 6 letter")
# else:
#     print("character is more than six letter")

# print(cou)

# problem

# lis = ["raj", "rajesh", "rajet", "ranjeet"]

# user = input("enter your name : \n")

# if (user in lis):
#     print(user + " is a valid name")
# else:
#     print(user + " is not a vaild person")

#####################################################
# num = 1
# while(num <= 50):
#     print(num)
#     num +=
# print("done")

# for(num=1, num <= 50, num++)
#################################################


# lis = ["meana", "lal", "manju", "kirti", "vijay", "lal"]
# i = 0
# while(i < len(lis)):
#     print(lis[i])
#     i = i+1

# print("hello below line is  for loop ")

# for item in lis:
#     if item == "lal":
#         continue
#     print(item)


# problem for and while loops

# table = int(input("enter table no : "))
# for i in range(1, 11):
#     print(str(table) + "X" + str(i) + "=" + str(table*i))
# you can write like this also both do same this but this is shoter version
#     print(f"{table}X{i}={table*i}")


# l1 = ["raj", "rajat", "narad", "vinay"]

# for i in l1:
#     if i.startswith("r"):
#         print(i + " welocme to the club")


# table = int(input("enter a table no"))
# i = 1
# while (i <= 10):

#     print(str(table) + "x" + str(i) + "=" + str(table*i))
#     i = i+1


# yourNumber=int(input("enter a number : "))
# import os
# os.remove("hello2.txt")
# f = open("hello.txt", "r")
# data = f.read()
# print(data)
# f.close()


#################------------File input and output----------######################


# with open("python/new.py", "r") as f:
#     a = f.read()

# with open("python/new.py", "a") as f:
#     a = f.write(" hello kutty")
# f = open("python/new.py", "r")
# b = f.read()
# print(b)

# f = open("highscore.txt", "w")
# f.write("highscore \n first player  33\n second player  220\n third player  9236\n fourth player  1150")
# f.close()


# def game():
#     f=open("highscore.txt","a")
#     f.write()
#     f.close()
# return 2


#############__________________problem_______________#######################

# def game():
#     return 6969


# myscore = game()

# f = open("highscore.txt", "r")
# recent = int(f.read())
# f.close()

# if (recent < myscore):
#     f = open("highscore.txt", "w")
#     f.write(str(myscore))
#     f.close()
# else:
#     print("error")


#############---------how to input 2 types in file---------###########

###### type1 #####
# with open("tables.txt", "w") as f:
#     f.write("")


###### type2 ######
# f = open("table2.txt", "w")
# f.write(" ")
# f.close()


#######___________prints tables in file_____________##############


# for i in range(2, 50):
#     f = open(f"tables{i}.txt", "w")

#     for j in range(1, 11):
#         f.write(f"{i}x{j}={i*j}\n")

#     f.close()

##############_____________replace a word______________######################


with open("dobkey.txt")as f:
    content = f.read()
if "donkey" in content:
    with open("dobkey.txt", "w") as f:
        f.write(content.replace("donkey", "3333333"))
else:
    print("there is no donkey")



