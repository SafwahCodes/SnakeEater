import pygame



def drawBackground():
    for i in range(0, x, 20):
        pygame.draw.rect(gameDisplay,pygame.Color(255,255,255,255), pygame.Rect(i, 0, 1, y))
    for j in range(0, y, 20):
        pygame.draw.rect(gameDisplay,pygame.Color(255,255,255,255), pygame.Rect(0, j, x, 1))

def drawSnake():
    pygame.draw.rect(gameDisplay, pygame.Color(255, 255, 255, 255), pygame.Rect(snake_x, snake_y, 20, 20))

pygame.init()

x = 420
y = 300

snake_x = 200
snake_y = 140
width_height = 20

gameDisplay = pygame.display.set_mode((x,y))
pygame.display.set_caption("Snake Eater")

clock = pygame.time.Clock()

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x += width_height
            elif event.key == pygame.K_DOWN:
                snake_y += width_height
            elif event.key == pygame.K_LEFT:
                snake_x -= width_height
            elif event.key == pygame.K_UP:
                snake_y -= width_height

    gameDisplay.fill((0,0,0))
    drawBackground()
    drawSnake()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()