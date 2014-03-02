#2012 Ross Rydman

import pygame
import math
from Shape import Shape
import config
from point import Point

class Circle(Shape):
    def __init__(self, position, radius, rotation, color):
        Shape.__init__(self, position, rotation, color)
        self.radius = radius

    def paint(self, surface):
        if self.active == False:
            return
        (x,y) = self.position.pair()
        pygame.draw.circle(surface, self.color, (x,y), int(self.radius))

    def move(self):
        (x,y) = self.position.pair()
        x += self.dx
        y += self.dy
        if x > config.SCREEN_X:
            x = 0
        elif x < 0:
            x = config.SCREEN_X
        if y > config.SCREEN_Y:
            y = 0
        elif y < 0:
            y = config.SCREEN_Y
        newposition = Point(x,y)
        self.position = newposition

    def rotate(self, degrees):
        self.rotation += degrees

    def accelerate(self, acceleration):
        self.dx = self.dx + acceleration * math.cos(math.radians(self.rotation))
        self.dy = self.dy + acceleration * math.sin(math.radians(self.rotation))

    def isActive(self):
        return self.active

    def set_inactive(self):
        self.active = False

    def getPoints(self):
        points = []
        for angle in range(0, 360, 360/config.BULLET_POINT_COUNT):
            angle_rad = math.radians(angle)
            (x,y) = math.cos(angle_rad) * self.radius, math.sin(angle_rad) * self.radius
            (xpos, ypos) = self.position.pair()
            x += xpos
            y += ypos
            p = Point(x,y)
            points.append(p)
        return points

    def contains(self, point):
        dist_x = self.position.x - point.x
        dist_y = self.position.y - point.y
        return dist_x*dist_x + dist_y*dist_y <= self.radius*self.radius