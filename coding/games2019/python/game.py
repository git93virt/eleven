# Making of rock paper and scissor

# rules
# 1 paper beats rock
# 2 rock beats scissor
# 3 scissor beats paper
import random


def gamewin(comp, you):
    if (you == comp):
        return None
    elif(comp == "P"):
        if(you == "R"):
            return False
        elif(you == "S"):
            return True
    elif(comp == "R"):
        if(you == "S"):
            return False
        elif(you == "P"):
            return True
    elif (comp == "S"):
        if (you == "P"):
            return False
        elif(you == "R"):
            return True


print("Rock(R),Paper(P),Scissor(S)")
comp = ("computer's turn : enter one initial form the above \n")
rand = random.randint(1, 3)
if rand == 1:
    comp = "P"
elif rand == 2:
    comp = "R"
elif rand == 3:
    comp = "S"

you = input("your's turn : enter one initial from the above \n")
a = gamewin(comp, you)
if a == None:
    print("you tied")
elif a:
    print("you win")
else:
    print("you lose")

print(f"you chose {you}")
print(f"comp chose {comp}")
