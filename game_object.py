# -*- coding: utf-8 -*-
"""
Idea fair simple android game
@author: Chris Minar
game object
"""
import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame

class button(pygame.sprite.Group):

    def __init__(self, screen, screenSize, image_on, image_off, position):

        super(button,self).__init__()

        self.position = position
        self.screen = screen
        self.screenSize = screenSize
        self.size_info = pygame.display.Info()

        self.ligado = pygame.image.load(image_on)
        self.desligado = pygame.image.load(image_off)

        ratioX = self.screenSize[0] / 486.0
        ratioY = self.screenSize[1] / 864.0

        self.ligado = pygame.transform.scale(self.ligado, (160*ratioX,84*ratioY))
        self.desligado = pygame.transform.scale(self.desligado, (160*ratioX,84*ratioY))

        self.imagem = pygame.sprite.Sprite()
        self.imagem.image = self.desligado

        self.imagem.image = self.desligado
        self.imagem.rect = self.imagem.image.get_rect()

        self.imagem.rect.x = position[0]*ratioX
        self.imagem.rect.y = position[1]*ratioY

        self.add(self.imagem)

    def update(self):

        ratioX = self.screenSize[0] / 486.0
        ratioY = self.screenSize[1] / 864.0

        self.imagem.rect.x = self.position[0]*ratioX
        self.imagem.rect.y = self.position[1]*ratioY

    def ligar(self):
        self.imagem.image = self.ligado

    def desligar(self):
        self.imagem.image = self.desligado

class qualquercoisa(pygame.sprite.Group):

    def __init__(self, screen, screenSize, position, velocity, color = (0,0,0), size = 20):

        super(qualquercoisa,self).__init__()

        #store the values that are input into the function
        self.position = position
        self.velocity = velocity
        self.screen = screen
        self.color = color
        self.screenSize = screenSize
        self.size = size
        self.size_info = pygame.display.Info()

        self.imagem = pygame.sprite.Sprite()
        self.imagem.image = pygame.image.load('images/mainship_t.png')

        ratioX = self.screenSize[0] / 486.0
        ratioY = self.screenSize[1] / 864.0

        self.imagem.image = pygame.transform.scale(self.imagem.image, (32*ratioX,32*ratioY))
        self.imagem.rect = self.imagem.image.get_rect()

        self.imagem.rect.x = position[0]*ratioX
        self.imagem.rect.y = position[1]*ratioY

        self.add(self.imagem)

    def update(self):

        ratioX = self.screenSize[0] / 486.0
        ratioY = self.screenSize[1] / 864.0

        self.imagem.rect.x = self.position[0]*ratioX
        self.imagem.rect.y = self.position[1]*ratioY

    def right(self):
        self.position[0] += 10

        if self.position[0] > 486:
            self.position[0] = 486

    def left(self):
        self.position[0] -= 10

        if self.position[0] < 0:
            self.position[0] = 0

    #make the object jump
    def jump(self):
        self.velocity[1] -= 200

class enemy(pygame.sprite.Group):

    def __init__(self, screen, screenSize, position, size = 20):

        super(enemy,self).__init__()

        #store the values that are input into the function
        self.position = position
        self.screen = screen
        self.initialDegree = 0
        self.screenSize = screenSize
        self.size = size
        self.size_info = pygame.display.Info()

        self.imagemCrua = pygame.image.load('images/mainship_t_o.png')

        self.imagem = pygame.sprite.Sprite()
        self.imagem.image = self.imagemCrua
        self.imagem.image = pygame.transform.rotate(self.imagem.image, 0)

        ratioX = self.screenSize[0] / 486.0
        ratioY = self.screenSize[1] / 864.0

        self.imagem.image = pygame.transform.scale(self.imagem.image, (32*ratioX,32*ratioY))
        self.imagem.rect = self.imagem.image.get_rect()

        self.imagem.rect.x = position[0]*ratioX
        self.imagem.rect.y = position[1]*ratioY

        self.add(self.imagem)

    def update(self):

        self.position[1] += 1

        ratioX = self.screenSize[0] / 486.0
        ratioY = self.screenSize[1] / 864.0

        self.initialDegree += 10
        self.imagem.image = self.imagemCrua
        self.imagem.image = pygame.transform.scale(self.imagem.image, (32*ratioX,32*ratioY))
        self.imagem.image = pygame.transform.rotate(self.imagem.image, self.initialDegree)

        #self.imagem.image = pygame.transform.scale(self.imagem.image, (32*ratioX,32*ratioY))

        self.imagem.rect = self.imagem.image.get_rect()

        self.imagem.rect.center = (0,0)

        self.imagem.rect.x += self.position[0]*ratioX
        self.imagem.rect.y += self.position[1]*ratioY

        #self.imagem.rect = self.imagem.image.get_rect()

class Bullet():

    def __init__(self,screen,screenSize,position):

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
