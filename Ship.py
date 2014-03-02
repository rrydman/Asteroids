#2012 Ross Rydman

from polygon import Polygon
from point import Point
import pygame
import config
import math

class Ship(Polygon):
    def __init__(self, position, rotation, color):
        p1 = Point(0,-4)
        p2 = Point(0,4)
        p3 = Point(20,0)
        self.outline = [p3, p1, p2] 
        self.position = position
        self.rotation = rotation
        self.color = color
        Polygon.__init__(self, self.outline, self.position, self.rotation, self.color)

    def game_logic(self, keys, newkeys):
        if self.active == False:
            return
        if pygame.K_LEFT in keys:
            self.rotate(-1 * config.SHIP_ROTATION_RATE)
        if pygame.K_RIGHT in keys:
            self.rotate(config.SHIP_ROTATION_RATE)
        if pygame.K_UP in keys:
            self.accelerate(config.SHIP_ACCELERATION_RATE)
        if pygame.K_DOWN in keys:
            self.accelerate(-1 * config.SHIP_ACCELERATION_RATE)
        self.move()


