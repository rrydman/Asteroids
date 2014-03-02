#2012 Ross Rydman

from game import Game
from point import Point
from Ship import Ship
from Rock import Rock
from Circle import Circle
from Bullet import Bullet
from Star import Star
import config
import random
import pygame

class Asteroids(Game):
    def __init__(self, name, screen_x, screen_y, frames_per_second):
        Game.__init__(self, name, screen_x, screen_y)
        ship_position = Point(config.SCREEN_X/2, config.SCREEN_Y/2)
        self.ship = Ship(ship_position, config.SHIP_INITIAL_DIRECTION, config.SHIP_COLOR)
        self.bullet = Bullet(Point(0,0), config.BULLET_RADIUS, 0, config.BULLET_COLOR)
        self.stars = []
        for i in range(config.STAR_COUNT):
            s = Star()
            self.stars.append(s)
        self.rocks = []
        for i in range(config.ROCK_COUNT):
            (x,y) = random.randint(0, config.SCREEN_X), random.randint(0, config.SCREEN_Y)
            p = Point(x,y)
            r = Rock(p, random.uniform(0, 360.0), config.ROCK_COLOR, (random.uniform(0.0, config.ROCK_MAX_ROTATION_SPEED) * random.uniform(-1.0,1.0)), random.randint(0, config.ROCK_MAX_SPEED))
            self.rocks.append(r)

    def game_logic(self, keys, newkeys):
        for s in self.stars:
            s.game_logic(keys, newkeys)
        self.ship.game_logic(keys, newkeys)
        for rock in self.rocks:
            rock.game_logic(keys, newkeys)
            if rock.isActive() == True:
                if self.ship.intersect(rock) == True:
                    self.ship.set_inactive()
                if self.bullet.intersect(rock) == True:
                    rock.set_inactive()
                    self.bullet.set_inactive()
        if pygame.K_SPACE in newkeys:
            if self.ship.isActive() == True:
                points = self.ship.getPoints()
                self.bullet.fire(points[0], self.ship.rotation)
        self.bullet.game_logic(keys,newkeys)

    def paint(self, surface):
        self.screen.fill(config.BACKGROUND_COLOR)
        for s in self.stars:
            s.paint(surface)
        self.ship.paint(surface)
        self.bullet.paint(surface)
        for rock in self.rocks:
            rock.paint(surface)

def main():
    a = Asteroids(config.TITLE, config.SCREEN_X, config.SCREEN_Y, config.FRAMES_PER_SECOND)
    a.main_loop()
main()