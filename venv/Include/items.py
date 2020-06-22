import pygame
import random
from utils import Point

class Snake(object):

    def __init__(self, screen_x, screen_y, snake_x, snake_y, width_height, moveDirection):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.snake_x = snake_x
        self.snake_y = snake_y
        self.width_height = width_height
        self.moveDirection = moveDirection
        self.pointsList = []
        self.pointsList.append(Point(snake_x, snake_y))
        self.length = len(self.pointsList)

    def draw(self, surface):
        for p in self.pointsList:
            pygame.draw.rect(surface, pygame.Color(255, 255, 255, 255), pygame.Rect(p.x, p.y, 20, 20))

    def update(self):
        tempHeadPosition = self.pointsList[0]
        if (self.moveDirection == "right"):
            self.pointsList[0].x += self.width_height
        if (self.moveDirection == "down"):
            self.pointsList[0].y += self.width_height
        if (self.moveDirection == "left"):
            self.pointsList[0].x -= self.width_height
        if (self.moveDirection == "up"):
            self.pointsList[0].y -= self.width_height
        if self.length > 1:
            for i in range(1,self.length+1):
                temp = self.pointsList[i]
                self.pointsList = tempHeadPosition
                tempHeadPosition = temp
                self.calculateWallClipping((self.pointsList[i]))
        else:
            self.calculateWallClipping(self.pointsList[0])

    def calculateWallClipping(self, point):
        if (point.x < 0):
            point.x = self.screen_x - self.width_height
        if (point.x > self.screen_x - self.width_height):
            point.x = 0
        if (point.y < 0):
            point.y = self.screen_y - self.width_height
        if (point.y > self.screen_y - self.width_height):
            point.y = 0

    def setMoveDirection(self, moveDirection):
        self.moveDirection = moveDirection

    def getPointsList(self):
        return self.pointsList

class Food(object):

    def __init__(self, screen_x, screen_y, width_height, screenCoords, usedCoordsList):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.width_height = width_height
        self.screen_coords = screenCoords
        self.radius = int(width_height/2)
        self.coords = self.getNewCoords(usedCoordsList)

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color(150, 150, 150, 255), (self.coords.x + self.radius, self.coords.y + self.radius), self.radius)

    def update(self):
        pass

    def getNewCoords(self, usedCoordsList):
        while True:
            tempCoords = random.choice(self.screen_coords) # generate new food coords
            if (not self.inUsedCoordsList(tempCoords, usedCoordsList)): # check if coords clash with usedCoordsList
                break
        return tempCoords

    def inUsedCoordsList(self, tempCoords, usedCoordsList):
        for p in usedCoordsList:
            if (tempCoords.x == p.x):
                if (tempCoords.y == p.y):
                    return True
        return False