import pygame

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
movement = "up"

def drawBackground():
    global screen_x, screen_y
    for i in range(0, screen_x, 20):
        pygame.draw.rect(gameDisplay,pygame.Color(255,255,255,255), pygame.Rect(i, 0, 1, screen_y))
    for j in range(0, screen_y, 20):
        pygame.draw.rect(gameDisplay,pygame.Color(255,255,255,255), pygame.Rect(0, j, screen_x, 1))

def drawSnake():
    global snake_x, snake_y
    if (snake_x < 0):
        snake_x = screen_x - width_height
    if (snake_x > screen_x - width_height):
        snake_x = 0
    if (snake_y < 0):
        snake_y = screen_y - width_height
    if (snake_y > screen_y - width_height):
        snake_y = 0
    pygame.draw.rect(gameDisplay, pygame.Color(255, 255, 255, 255), pygame.Rect(snake_x, snake_y, 20, 20))

def snakeMove():
    global snake_x, snake_y
    if (movement == "right"):
        snake_x += width_height
    if (movement == "down"):
        snake_y += width_height
    if (movement == "left"):
        snake_x -= width_height
    if(movement == "up"):
        snake_y -= width_height

# game loop
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                movement = "right"
            elif event.key == pygame.K_DOWN:
                movement = "down"
            elif event.key == pygame.K_LEFT:
                movement = "left"
            elif event.key == pygame.K_UP:
                movement = "up"

    gameDisplay.fill((0,0,0))
    drawBackground()
    snakeMove()
    drawSnake()
    pygame.display.update()
    clock.tick(5)

pygame.quit()
quit()