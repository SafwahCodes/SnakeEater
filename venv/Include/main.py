import pygame
from Scenes import GameScene, MenuMainScene, MenuPauseScene

pygame.init()
screen_x = 420
screen_y = 300
width_height = 20
surface = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Snake Eater")
clock = pygame.time.Clock()
main_loop_running = True

scene = MenuMainScene(screen_x, screen_y)

temp_scene = None

# main loop
while main_loop_running:

    if pygame.event.get(pygame.QUIT):
        main_loop_running = False
        #return

    game_update_status = scene.update(pygame.event.get())
    if scene.get_scene_type() == 1 and game_update_status != None:
        if game_update_status == 1: # 1 - Easy gameplay
            scene = GameScene(screen_x, screen_y, width_height)
        else: # 2 - Hard gameplay (create gameplay later)
            scene = GameScene(screen_x, screen_y, width_height, hard_difficulty=True) # modify later for hard gameplay
        continue
    if scene.get_scene_type() == 2 and game_update_status != None:
        if game_update_status == 1: # 1 - pause screen
            temp_scene = scene # save game scene to resume later
            scene = MenuPauseScene(screen_x, screen_y)
        elif game_update_status == 2: # 2 - game over screen (easy)
            scene = MenuPauseScene(screen_x, screen_y, game_over=True)
        else: # 3 - game over screen (hard)
            scene = MenuPauseScene(screen_x, screen_y, game_over=True, hard_difficulty=True)
        continue
    if scene.get_scene_type() == 3 and game_update_status != None:
        if game_update_status == 1: # 1 - play again (easy)
            scene = GameScene(screen_x, screen_y, width_height)
        elif game_update_status == 2: # 2 - return to main menu
            scene = MenuMainScene(screen_x, screen_y)
        elif game_update_status == 3: # 3 - resume gameplay
            scene = temp_scene
        else: # 4 - play again (hard)
            scene = GameScene(screen_x, screen_y, width_height, hard_difficulty=True)
        continue
    scene.draw(surface)

    pygame.display.update()
    clock.tick(5)

pygame.quit()
quit()