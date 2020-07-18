import pygame
from Scenes import GameScene

pygame.init()
screen_x = 420
screen_y = 300
width_height = 20
surface = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Snake Eater")
clock = pygame.time.Clock()
main_loop_running = True

scene = GameScene(screen_x, screen_y, width_height)

# main loop
while main_loop_running:

    if pygame.event.get(pygame.QUIT):
        main_loop_running = False
        #return

    game_update_status = scene.update(pygame.event.get())
    if scene.is_game_scene() and game_update_status != None:
        if (game_update_status == 1): # 1 -
            # later change to pause screen
            pass
        else: # 2 - game over
            # later change to game over screen and reset game
            main_loop_running = False # test code
        continue # skip to next iteration of loop
    scene.draw(surface)

    pygame.display.update()
    clock.tick(5)

pygame.quit()
quit()