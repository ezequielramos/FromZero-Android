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
        self.color = (self.color_init[0]+100,self.color_init[1]+100,self.color_init[2]+100)

    def desligar(self):
        self.color = self.color_init

class estrela():

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

class Player(pygame.sprite.Group):

    width = 32
    height = 28

    def __init__(self, x, y):

        super(Player,self).__init__()

        self.group = pygame.sprite.Group()
        
        base = pygame.sprite.Sprite()

        base.image = pygame.Surface([self.width, 8])

        base.rect = base.image.get_rect()

        base.rect.x = x
        base.rect.y = y + 24

        self.base = base

        self.group.add(self.base)

        base = pygame.sprite.Sprite()

        base.image = pygame.Surface([6, 22])

        base.rect = base.image.get_rect()

        base.rect.x = x + 14
        base.rect.y = y + 2

        self.tronco = base

        self.group.add(self.tronco)

        self.imagem = pygame.sprite.Sprite()

        self.imagem.image = pygame.image.load('images/mainship_t.png')

        self.imagem.rect = self.imagem.image.get_rect()

        self.imagem.rect.x = x
        self.imagem.rect.y = y

        self.pos = [False,False,False,False]

        self.add(self.imagem)

    def right(self):

        self.position[0] += 10

        if self.position[0] > 454:
            self.position[0] -= 10
        else:
            for sprite in self.group_grey:
                sprite[0] += 10
            for sprite in self.group_darkblue:
                sprite[0] += 10
            for sprite in self.group_darkgrey:
                sprite[0] += 10
            for sprite in self.group_purple:
                sprite[0] += 10

    def left(self):

        self.position[0] -= 10

        if 0 > self.position[0]:
            self.position[0] += 10
        else:
            for sprite in self.group_grey:
                sprite[0] -= 10
            for sprite in self.group_darkblue:
                sprite[0] -= 10
            for sprite in self.group_darkgrey:
                sprite[0] -= 10
            for sprite in self.group_purple:
                sprite[0] -= 10