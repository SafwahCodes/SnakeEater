import pygame
import pygame_menu
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

    def get_scene_type(self):
        raise NotImplementedError

class MenuPauseScene(Scene):

    def __init__(self, screen_x, screen_y, game_over=False, hard_difficulty=False):
        self.menu = pygame_menu.Menu(screen_y, screen_x, 'Game Over', theme=pygame_menu.themes.THEME_DARK)
        if game_over:
            if hard_difficulty:
                self.menu.add_button('Play again? (Hard)', self.play_hard_restart_button_action)
            else:
                self.menu.add_button('Play again? (Easy)', self.play_easy_restart_button_action)
        else:
            self.menu.add_button('Resume game', self.play_resume_button_action)
        self.menu.add_button('Exit to main menu', self.return_button_action) # exit whole program
        self.menu.add_button('Exit to desktop', pygame_menu.events.EXIT) # exit whole program
        self.return_value = None

    def return_button_action(self):
        self.return_value = 2

    def get_scene_type(self):
        return 3

    def play_easy_restart_button_action(self):
        self.return_value = 1

    def play_hard_restart_button_action(self):
        self.return_value = 4

    def play_resume_button_action(self):
        self.return_value = 3

    def draw(self, surface):
        self.menu.draw(surface)

    def update(self, events):
        self.menu.update(events)
        return self.return_value

class MenuMainScene(Scene):

    def __init__(self, screen_x, screen_y):
        self.menu = pygame_menu.Menu(screen_y, screen_x, 'Snake Eater', theme=pygame_menu.themes.THEME_DARK)
        self.menu.add_button('Play', self.play_button_action)
        self.menu.add_selector('Difficulty: ', [('Easy', 1),('Hard', 2)], onchange=self.set_difficulty)
        self.menu.add_button('Exit', pygame_menu.events.EXIT) # exit whole program
        self.return_value = None
        self.hold_difficulty_value = 1

    def set_difficulty(self, difficulty, value):
        self.hold_difficulty_value = value

    def get_scene_type(self):
        return 1

    def play_button_action(self):
        self.return_value = self.hold_difficulty_value

    def draw(self, surface):
        self.menu.draw(surface)

    def update(self, events):
        self.menu.update(events)
        return self.return_value

class GameScene(Scene):

    def __init__(self, screen_x, screen_y, width_height, hard_difficulty=False): # add difficulty flag later
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.width_height = width_height

        # init snake
        self.reset_snek(hard_difficulty)

        # init food
        self.rat = Food(self.screen_x, self.screen_y, self.width_height, self.snek.getBody())

        # init walls (maybe) for harder difficulties

    def get_scene_type(self):
        return 2

    def reset_snek(self, hard_difficulty):
        self.snake_x = (self.screen_x / 2) - (self.width_height / 2)
        self.snake_y = (self.screen_y / 2) - (self.width_height / 2)
        self.moveDirection = "up"
        self.snek = Snake(self.screen_x, self.screen_y, self.snake_x, self.snake_y, self.width_height, self.moveDirection, hard_difficulty)

    def check_snake_food_collision(self):
        snek_head_coords = self.snek.getHeadCoords()
        rat_coords = self.rat.getCoords()
        if snek_head_coords == rat_coords:
            self.snek.grow()
            self.rat.getNewCoords(self.snek.getBody())
            return # None

    def has_snake_snake_collision(self):
        return self.snek.has_self_collision()

    def has_snake_wall_collision(self):
        snek_head_coords = self.snek.getHeadCoords()
        return snek_head_coords[0] < 0 or snek_head_coords[0] > self.screen_x or snek_head_coords[1] < 0 or snek_head_coords[1] > self.screen_y

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
            return 2 # game over (easy)
        if self.has_snake_wall_collision():
            return 3 # game over (hard)

    def handle_events(self, events):
        pass

