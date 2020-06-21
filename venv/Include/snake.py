import pygame

class Snake(object):

    def __init__(self, screen_x, screen_y, snake_x, snake_y, width_height, moveDirection):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.snake_x = snake_x
        self.snake_y = snake_y
        self.width_height = width_height
        self.moveDirection = moveDirection
        self.pointsList = []
        self.pointsList.append(Points(snake_x, snake_y))
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
            point.x = point.x - self.width_height
        if (point.x > self.screen_x - self.width_height):
            point.x = 0
        if (point.y < 0):
            point.y = point.y - self.width_height
        if (point.y > self.screen_y - self.width_height):
            point.y = 0

    def setMoveDirection(self, moveDirection):
        self.moveDirection = moveDirection

class Points(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y