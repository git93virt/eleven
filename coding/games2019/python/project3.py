import random as rd


print("This is a guessing game so lets start!!!\n******RULE******\nGuess the number between 1-100")
rand = rd.randrange(1, 100)
print(rand)
guess = 0
player = None


while (player != rand):
    player = int(input("enter your number: "))
    guess += 1
    if player == rand:
        print("you gussed right")
    else:
        if player > rand:
            print("wrong number...please enter smaller number")
        else:
            print("you are wrong!!!!!please enter larger number")

    print(f"your guessed {guess}time")


# # player=input("enter your number: ")
# for rand in player:
#     player = int(input("enter your number: "))
#     if player is rand:
#         print ("your guessed right")
#     else:
#         print ("your guessed wrong")

# for i in rand:
#     if player>i:
#         print("you guessed lower number")
#     else:
#         print("you guessed higher number")


while(True):
    print("press q to exit")
    user = input("enter a number: ")
    if user=="q":
        break
    try:
        user = int(user)
        if user > 5:
            print("you enter a greater number")
        else:
            print("your number is smaller than 5")
    except Exception as e:
        print(e)

print ("thaks for playing")
