# -*- coding: utf-8 -*-
"""
Idea fair simple android game
@author: Chris Minar
game object
"""
import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame
import random

class game_object():
    #
    # Class Methods
    #

    def __init__(self, screen, screenSize, position=[0,0], velocity=[0,0], color = (0,0,0), size = 20):
        #store the values that are input into the function
        self.position = position
        self.velocity = velocity
        self.screen = screen
        self.color = color
        self.screenSize = screenSize
        self.size = size
        self.size_info = pygame.display.Info()
    
    #draw the object on the screen
    def draw(self):

        ratioX = self.screenSize[0] / 486.0
        ratioY = self.screenSize[1] / 864.0

        self.lolX = self.size*ratioX
        self.lolY = self.size*ratioY

        position = ((self.position[0]*ratioX)-self.lolX/2.0, (self.position[1]*ratioY)-self.lolY/2.0, self.lolX, self.lolY)

        pygame.draw.rect(self.screen, self.color, position)
        
    #make the object jump
    def jump(self):
        self.velocity[1] -= 200

    def right(self):
        self.position[0] += 10

        if self.position[0] > 486:
            self.position[0] = 486

    def left(self):
        self.position[0] -= 10

        if self.position[0] < 0:
            self.position[0] = 0

class button():

    def __init__(self, screen, screenSize, color = (0,0,0), position=[0,0], size=[20,20]):
        self.position = position
        self.screen = screen
        self.color = color
        self.color_init = color
        self.screenSize = screenSize
        self.size = size
        self.size_info = pygame.display.Info()

    def draw(self):

        ratioX = self.screenSize[0] / 486.0
        ratioY = self.screenSize[1] / 864.0

        self.lolX = self.size[0]*ratioX
        self.lolY = self.size[1]*ratioY

        position = ((self.position[0]*ratioX)-self.lolX/2.0, (self.position[1]*ratioY)-self.lolY/2.0, self.lolX, self.lolY)

        pygame.draw.rect(self.screen, self.color, position)

    def ligar(self):
        r = self.color_init[0]+100
        g = self.color_init[1]+100
        b = self.color_init[2]+100

        if r > 255:
            r = 255

        if g > 255:
            g = 255

        if b > 255:
            b = 255

        self.color = (r,g,b)

    def desligar(self):
        self.color = self.color_init

class estrela():

    def teste():
        print "lol"

    def __init__(self, screen, screenSize, position=[0,0]):
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

class Bullet():

    def __init__(self,screen,screenSize,position=[0,0]):

        self.screen = screen
        self.color = (0,255,0)
        self.screenSize = screenSize
        self.position = position
        self.size = (1,2)

    def update(self):

        self.position[1] -= 10

    def draw(self):

        ratioX = self.screenSize[0] / 486.0
        ratioY = self.screenSize[1] / 864.0

        self.lolX = self.size[0]*ratioX
        self.lolY = self.size[1]*ratioY

        position = ((self.position[0]*ratioX)-self.lolX/2.0, (self.position[1]*ratioY)-self.lolY/2.0, self.lolX, self.lolY)

        pygame.draw.rect(self.screen, self.color, position)