def read(filename):
    try:
        f = open(filename, "r")
        data = f.read()
        print(data)
        f.close()
        # with open(filename, "r") as f:
        #     print(f.read())

    except FileNotFoundError:
        print(f"your {filename} is not present")


read("file1.txt")
read("file2.txt")
read("file3.txt")


lists = [1, 2, 3, 4, 56, 78, 9, 8, 9, 4, ]

# lists1=[i for item in lists if item[3]]

for index, item in enumerate(lists):
    if index==2 or index==4 or index==6:
        print(index,item)



num=int(input("enter a table number: "))

li=[num*i for i in range(1,11)  ]
five = li

print(five)
print (f"this is with {li}")