

# a=input("what iss your name : ")
# print (f"Welcome, {a}")
# print ("add a number")
# try:
#     b=int(input("first number :"))
#     c=int(input("second number :"))
#     d=b/c
#     print(f"the sum of first and second number is {d}")
# except :
#     raise ZeroDivisionError(f"cant work with zero ")
# finally:
#     print(__name__)


# use for __name__=="__main__"
def greet(name):
    print(f"welcome,{name}")


print(__name__)
if __name__ == "__main__":
    a = input("enter your name")
    greet(a)
