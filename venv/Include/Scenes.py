import pygame
from items import Snake, Food

class Scene(object):

    def __init__():
        pass

    def draw(self, surface):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError

    def is_game_scene(self):
        raise NotImplementedError

    def is_menu_main_scene(self):
        raise NotImplementedError

    def is_menu_pause_scene(self):
        raise NotImplementedError

class GameScene(Scene):

    def __init__(self, screen_x, screen_y, width_height):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.width_height = width_height

        # init snake
        self.reset_snek()

        # init food
        self.rat = Food(self.screen_x, self.screen_y, self.width_height, self.snek.getBody())

        # init walls (maybe) for harder difficulties

    def is_game_scene(self):
        return True

    def is_menu_main_scene(self):
        return False

    def is_menu_pause_scene(self):
        return False

    def reset_snek(self):
        self.snake_x = (self.screen_x / 2) - (self.width_height / 2)
        self.snake_y = (self.screen_y / 2) - (self.width_height / 2)
        self.moveDirection = "up"
        self.snek = Snake(self.screen_x, self.screen_y, self.snake_x, self.snake_y, self.width_height, self.moveDirection)

    def check_snake_food_collision(self):
        snek_head_coords = self.snek.getHeadCoords()
        rat_coords = self.rat.getCoords()
        if snek_head_coords == rat_coords:
            self.snek.grow()
            self.rat.getNewCoords(self.snek.getBody())
            return # None

    def has_snake_snake_collision(self):
        return self.snek.has_self_collision()

    def drawBackground():
        global screen_x, screen_y
        for i in range(0, screen_x, 20):
            pygame.draw.rect(gameDisplay, pygame.Color(255, 255, 255, 255), pygame.Rect(i, 0, 1, screen_y))
        for j in range(0, screen_y, 20):
            pygame.draw.rect(gameDisplay, pygame.Color(255, 255, 255, 255), pygame.Rect(0, j, screen_x, 1))

    def draw(self, surface):
        # background draw
        surface.fill((0, 0, 0))
        for i in range(0, self.screen_x, 20):
            pygame.draw.rect(surface, pygame.Color(255, 255, 255, 255), pygame.Rect(i, 0, 1, self.screen_y))
        for j in range(0, self.screen_y, 20):
            pygame.draw.rect(surface, pygame.Color(255, 255, 255, 255), pygame.Rect(0, j, self.screen_x, 1))

        # food draw
        self.rat.draw(surface)

        # snake draw
        self.snek.draw(surface)

    def update(self, events):
        # scene handler should check whether exit/escape button has been pressed
        # snake handle events
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snek.set_move_direction("right")
                elif event.key == pygame.K_DOWN:
                    self.snek.set_move_direction("down")
                elif event.key == pygame.K_LEFT:
                    self.snek.set_move_direction("left")
                elif event.key == pygame.K_UP:
                    self.snek.set_move_direction("up")
                elif event.key == pygame.K_ESCAPE:
                    return 1 # opens pause menu

        # food update
        self.rat.update()

        # snake update
        self.snek.update()

        # collision update
        self.check_snake_food_collision()
        if self.has_snake_snake_collision():
            return 2 # game over

    def handle_events(self, events):
        pass


class MenuMainScene(Scene):

    def __init__(self):
        pass

    def draw(self, surface):
        pass

    def update(self):
        pass

    def handle_events(self, events):
        pass