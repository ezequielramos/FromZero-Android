import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame
import random

class estrela(object):

    def __init__(self, screen, screenSize, position):
        self.position = position
        self.screen = screen
        self.color = (255,255,255)
        self.screenSize = screenSize
        self.size = (1,1)
        self.size_info = pygame.display.Info()
        self.velocity = random.randint(1,10)

    def draw(self):

        ratioX = self.screenSize[0] / 486.0
        ratioY = self.screenSize[1] / 864.0

        self.lolX = self.size[0]*ratioX
        self.lolY = self.size[1]*ratioY

        position = ((self.position[0]*ratioX)-self.lolX/2.0, (self.position[1]*ratioY)-self.lolY/2.0, self.lolX, self.lolY)

        pygame.draw.rect(self.screen, self.color, position)

    def descer(self):

        self.position[1] += self.velocity