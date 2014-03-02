#2012 Ross Rydman

from polygon import Polygon
from point import Point
import config
import pygame
import math
import random

class Rock(Polygon):
    def __init__(self, position, rotation, color, rotation_speed, motion):
        self.outline = []
        for angle in range(0, 360, 360/config.ROCK_POLYGON_SIZE):
            radius = random.uniform(config.ROCK_MIN_RADIUS, config.ROCK_MAX_RADIUS)
            angle_rad = math.radians(angle)
            (x,y) = math.cos(angle_rad) * radius, math.sin(angle_rad) * radius
            p = Point(x,y)
            self.outline.append(p)
        self.position = position
        self.rotation = rotation
        self.color = color
        self.rotation_speed = rotation_speed
        self.motion = motion
        Polygon.__init__(self, self.outline, self.position, self.rotation, self.color)
        self.accelerate(self.motion)

    def game_logic(self, keys, newkeys):
        if self.active == False:
            return
        self.rotate(self.rotation_speed)
        self.move()
