import pygame
import random

class Snake(object):
    body = []
    turns = {}

    def __init__(self, screen_x, screen_y, snake_x, snake_y, width_height, move_direction):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.width_height = width_height
        self.move_direction = move_direction
        self.head = [snake_x, snake_y]
        self.body = []
        self.body.append(self.head)
        self.length = len(self.body)

    def draw(self, surface):
        # draw rest of body before head to that head appears on top of body during self collision
        for i, p in enumerate(self.body[1:]):
            pygame.draw.rect(surface, pygame.Color(255, 255, 255, 255), pygame.Rect(p[0], p[1], self.width_height, self.width_height))
        pygame.draw.rect(surface, pygame.Color(128, 128, 128, 255), pygame.Rect(self.head[0], self.head[1], self.width_height, self.width_height))

    def update(self):
        move_x = 0
        move_y = 0
        # update head first then iterate through the rest of the body
        if (self.move_direction == "right"):
            new_head_pos = [self.body[0][0] + self.width_height, self.body[0][1]]
        elif (self.move_direction == "down"):
            new_head_pos = [self.body[0][0], self.body[0][1] + self.width_height]
        elif (self.move_direction == "left"):
            new_head_pos = [self.body[0][0] - self.width_height, self.body[0][1]]
        elif (self.move_direction == "up"):
            new_head_pos = [self.body[0][0], self.body[0][1] - self.width_height]
        self.head = new_head_pos
        if (len(self.body) > 1):
            # this works by shifting the positions of self.body[1:] forward such that
            # self.body[1] becomes pos self.body[0] before it had been updated,
            # self.body[2] becomes pos self.body[1] before it had been updated, etc
            # this is achieved by making a copy of the self.body list before it has been
            # updated and using this as reference for the actual self.body list
            temp_head_pos = self.body[0]
            # make a copy of body list
            body_list_copy = self.body[:]
            self.body[0] = new_head_pos
            self.calculateWallClipping(self.body[0])
            for i in range(0, len(self.body)-1):
                self.body[i+1] = body_list_copy[i]
                self.calculateWallClipping(self.body[i+1])
        else:
            self.body[0] = new_head_pos
            self.calculateWallClipping(self.body[0])

    def calculateWallClipping(self, point):
        if (point[0] < 0):
            point[0] = self.screen_x - self.width_height
        if (point[0] > self.screen_x - self.width_height):
            point[0] = 0
        if (point[1] < 0):
            point[1] = self.screen_y - self.width_height
        if (point[1] > self.screen_y - self.width_height):
            point[1] = 0

    def set_move_direction(self, move_direction):
        # move_direction == "right" and not self.move_direction == "left" or move_direction == "down" and not self.move_direction == "up" or move_direction == "left" and not self.move_direction == "right" or move_direction == "up" and not self.move_direction == "down"
        if (move_direction == "right" and not self.move_direction == "left"):
            self.move_direction = move_direction
        elif (move_direction == "down" and not self.move_direction == "up"):
            self.move_direction = move_direction
        elif (move_direction == "left" and not self.move_direction == "right"):
            self.move_direction = move_direction
        elif (move_direction == "up" and not self.move_direction == "down"):
            self.move_direction = move_direction

    def getBody(self):
        return self.body

    def getHeadCoords(self):
        return self.body[0]

    def grow(self):
        if (self.length == 1):
            if (self.move_direction == "right"):
                self.body.append([self.body[-1][0] - self.width_height, self.body[-1][1]])
            elif (self.move_direction == "down"):
                self.body.append([self.body[-1][0], self.body[-1][1] - self.width_height])
            elif (self.move_direction == "left"):
                self.body.append([self.body[-1][0] + self.width_height, self.body[-1][1]])
            elif (self.move_direction == "up"):
                self.body.append([self.body[-1][0], self.body[-1][1] + self.width_height])
        else:
            last_coords = self.body[-1]
            second_last_coords = self.body[-2]
            delta_x = last_coords[0] - second_last_coords[0]
            delta_y = last_coords[1] - second_last_coords[1]
            self.body.append([last_coords[0] + delta_x, last_coords[1] + delta_y])
        self.length = len(self.body)

    def has_self_collision(self):
        if (self.length > 1):
            return self.head in self.body[1:]

class Food(object):

    def __init__(self, screen_x, screen_y, width_height, usedCoordsList):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.width_height = width_height
        self.screen_coords = self.produceCoordsList()
        self.radius = int(width_height/2)
        self.getNewCoords(usedCoordsList)

    def produceCoordsList(self):
        coordsList = []
        for i in range(0, self.screen_y, self.width_height):
            for j in range(0, self.screen_x, self.width_height):
                coordsList.append([j, i])
        return coordsList

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color(150, 150, 150, 255), (self.coords[0] + self.radius, self.coords[1] + self.radius), self.radius)

    def update(self):
        pass

    def getCoords(self):
        return self.coords

    def getNewCoords(self, usedCoordsList):
        while True:
            tempCoords = random.choice(self.screen_coords) # generate new food coords
            if (not self.inUsedCoordsList(tempCoords, usedCoordsList)): # check if coords clash with usedCoordsList
                break
        self.coords = tempCoords
        #print(self.coords)

    def inUsedCoordsList(self, tempCoords, usedCoordsList):
        for p in usedCoordsList:
            if (tempCoords[0] == p[0]):
                if (tempCoords[1] == p[1]):
                    return True
        return False