import random
import cv2


# rand=random.randint(1,100)

# print (rand)

# user=str(input("guess the no bw 1 to 100: "))



# print(user)

################converts a color image into grey######################


path ="C:\\Users\\win10\\Desktop\\games2019\\img\\tekken.jpg"

img=cv2.imread(path)
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inverted=255-grey
blurred=cv2.GaussianBlur(inverted,(21,21),0)
invertedblur=255-blurred
sketch=cv2.divide(grey,invertedblur,scale=256)

cv2.imwrite("C:\\Users\\win10\\Desktop\\games2019\\img\\new.png",sketch)
