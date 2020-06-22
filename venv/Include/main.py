import pygame
from items import Snake
from items import Food
from utils import Point
# testing switch user for commits

pygame.init()
screen_x = 420
screen_y = 300
gameDisplay = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Snake Eater")
clock = pygame.time.Clock()
gameOver = False

snake_x = 200
snake_y = 140
width_height = 20
moveDirection = "up"

snek = Snake(screen_x, screen_y, snake_x, snake_y, width_height, moveDirection)

def produceCoordsList():
    coordsList = []
    for i in range(0,screen_y+ width_height,width_height):
        for j in range(0, screen_x+width_height, width_height):
            coordsList.append(Point(j, i))
            #print("({0}, {1})".format(j, i))
    return coordsList

screenCoords = produceCoordsList()
rat = Food(screen_x, screen_y, width_height, screenCoords, snek.getPointsList())

def drawBackground():
    global screen_x, screen_y
    for i in range(0, screen_x, 20):
        pygame.draw.rect(gameDisplay,pygame.Color(255,255,255,255), pygame.Rect(i, 0, 1, screen_y))
    for j in range(0, screen_y, 20):
        pygame.draw.rect(gameDisplay,pygame.Color(255,255,255,255), pygame.Rect(0, j, screen_x, 1))

# game loop
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snek.setMoveDirection("right")
            elif event.key == pygame.K_DOWN:
                snek.setMoveDirection("down")
            elif event.key == pygame.K_LEFT:
                snek.setMoveDirection("left")
            elif event.key == pygame.K_UP:
                snek.setMoveDirection("up")

    gameDisplay.fill((0,0,0))
    drawBackground()
    snek.update()
    snek.draw(gameDisplay)
    rat.draw(gameDisplay)
    pygame.display.update()
    clock.tick(5)

pygame.quit()
quit()