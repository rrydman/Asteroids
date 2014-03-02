#2012 Ross Rydman

import pygame
import math

class Shape:
    def __init__(self, position, rotation, color): 
        self.position = position
        self.color = color
        self.rotation = rotation
        self.active = True
        self.dx = 0
        self.dy = 0

    def paint(self, surface):
       raise NotImplementedError()

    def game_logic(self, keys, newkeys):
       raise NotImplementedError()

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

    def accelerate(self, acceleration):
        self.dx = self.dx + acceleration * math.cos(math.radians(self.rotation))
        self.dy = self.dy + acceleration * math.sin(math.radians(self.rotation))

    def get_rotation(self):
       return self.rotation

    def set_active(self):
        self.active = True

    def intersect(self, other_polygon):
        #if intersect, return True --- if no intersections, return False
        self_poly_points = []
        self_poly_points = self.getPoints()
        other_poly_points = []
        other_poly_points = other_polygon.getPoints()
        for point in self_poly_points:
            if other_polygon.contains(point) == True:
                return True
        for point in other_poly_points:
            if self.contains(point) == True:
                return True
        return False

    def contains(self):
        raise NotImplementedError()

    def getPoints(self):
        raise NotImplementedError()