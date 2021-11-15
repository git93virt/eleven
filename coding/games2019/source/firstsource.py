from os import write
import pygame as pg
import random
# import color

pg.init()
# print(pygame.init())

# for opening game window
gwindow = pg.display.set_mode((600, 400))


# for giving game title on window
pg.display.set_caption("snakes")

# for update game
pg.display.update()

# creating game exit variable


time = pg.time.Clock()
font = pg.font.SysFont(None, 25)


red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
maroon = (125, 0, 0)
color = (210, 35, 62)

def screentxt(text, color, x, y):
    screen = font.render(text, True, color)
    gwindow.blit(screen, [x, y])


def snakebody(gwindow, color, snakelist, snakesize):
    for x, y in snakelist:
        pg.draw.rect(gwindow, color, [x, y, snakesize, snakesize])


def welcome():
    exitgame = False
    while not exitgame:
        gwindow.fill(green)
        screentxt("snake ka baap", color, 250, 200)
        screentxt("press enter to start game", color, 200, 170)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exitgame = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    gloop()

            # if event.type == pg.MOUSEBUTTONDOWN:
            #     print("you clicked mouse button")

        pg.display.update()
        time.tick(25)


def gloop():
    exitgame = False
    gameover = False
    radius = 8
    snkx = 20
    snky = 62
    snakesize = 20
    fps = 25
    vel_x = 0
    vel_y = 0
    foodx = random.randint(0, 600)
    foody = random.randint(0, 400)
    score = 0
    snakelength = 1
    snakelist = []
    with open("txt file/highscore.txt", "r") as f:
        highscore = f.read()

    while not exitgame:
        if gameover:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gwindow.fill(green)
            screentxt("GAMEOVER \n YOUR SCORE : " +
                      str(score), blue, 600/2, 400/2)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exitgame = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        welcome()
        else:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exitgame = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        vel_x = 3
                        vel_y = 0

                    # print("you have presssed right arrow key")
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        vel_x = -3
                        vel_y = 0

                    # print("you have presssed left arrow key")
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        vel_y = -3
                        vel_x = 0

                    # print("you have presssed up arrow key")
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        vel_y = 3
                        vel_x = 0

                    # print("you have presssed down arrow key")

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        score += 10

                if event.type == pg.MOUSEBUTTONDOWN:
                    print("you clicked mouse button")
                    

            snkx = snkx+vel_x
            snky = snky+vel_y

            if abs((snkx-foodx) < 3 and abs(snky-foody) < 3):
                score += 1*10
                print(f"your score is : {score}")
                foodx = random.randint(60, 600)
                foody = random.randint(60, 400)
                snakelength += 10
                # print(highscore)
                if score > int(highscore):
                    highscore = score

            gwindow.fill(green)
            screentxt("score:" + str(score) +
                      " Highscore: "+str(highscore), blue, 5, 5)
            pg.draw.circle(gwindow, red, (foodx, foody), radius)
            # pg.draw.rect(gwindow, red, [foodx, foody, snakesize, snakesize])

            head = []
            head.append(snkx)
            head.append(snky)
            snakelist.append(head)

            if len(snakelist) > snakelength:
                del snakelist[0]

            if head in snakelist[:-1]:
                gameover = 1

            if snkx < 0 or snkx > 600 or snky < 0 or snky > 400:
                gameover = True

            snakebody(gwindow, blue, snakelist, snakesize)
        time.tick(fps)
        pg.display.update()

    pg.quit()
    quit()


welcome()


gloop()

# pygame.sprite.draw(, bgd=None)
# pygame.draw.circle(Surface, color, pos, radius, width=0)
