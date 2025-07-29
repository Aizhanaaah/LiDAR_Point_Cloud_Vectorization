import math
import pygame
class buildEnvironments:
    def __init__(self, mapdimensions):
        pygame.init()
        self.pointCloud = []
        self.externalMap = pygame.image.load("map1.png")
        self.mapH, self.mapW = mapdimensions
        self.MapWindowName = 'RRT Path Planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapW, self.mapH))
        self.map.blit(self.externalMap, (0, 0))
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
