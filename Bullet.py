#2012 Ross Rydman

import pygame
from Circle import Circle
import config

class Bullet(Circle):
    def __init__(self, position, radius, rotation, color): 
        Circle.__init__(self, position, radius, rotation, color)
        self.set_inactive()

    def game_logic(self, keys, newkeys): 
        if self.isActive == False:
            return
        else:
            #test if the move will move off screen, if no, do move, if yes, make inactive
            (x,y) = self.position.pair()
            x += self.dx
            y += self.dy
            if x > config.SCREEN_X or x < 0 or y > config.SCREEN_Y or y < 0:
                self.set_inactive()
            else:
                self.move()

    def fire(self, position, rotation): 
        self.position = position
        self.rotation = rotation
        self.set_active()
        self.dx = 0
        self.dy = 0
        self.accelerate(config.BULLET_SPEED)

