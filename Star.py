#2012 Ross Rydman

from Circle import Circle
from point import Point

import random
import config

class Star(Circle):
    def __init__(self):
        (x,y) = random.randint(0, config.SCREEN_X), random.randint(0, config.SCREEN_Y)
        position = Point(x,y)
        rand = random.randint(0,255)
        color = (rand,rand,rand)
        radius = config.STAR_RADIUS
        rotation = 0.0
        Circle.__init__(self, position, radius, rotation, color)

    def game_logic(self, keys, newkeys):
        amount = random.randint(0,config.STAR_TWINKLE_SPEED)
        (r,g,b) = self.color
        r += amount
        if r > 255:
            r = 0
        g += amount
        if g > 255:
            g = 0
        b += amount
        if b > 255:
            b = 0
        self.color = (r,g,b)
