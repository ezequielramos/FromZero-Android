# -*- coding: utf-8 -*-
"""
Idea fair simple android game
@author: Chris Minar
game object
"""
import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame

class game_object():
    #
    # Class Methods
    #

    def __init__(self, screen, position=[0,0], velocity=[0,0], color = (0,0,0), size = 20):
        #store the values that are input into the function
        self.position = position
        self.velocity = velocity
        self.screen = screen
        self.color = color
        self.size = size
        self.size_info = pygame.display.Info()
    
    #draw the object on the screen
    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.position[0]-self.size/2.0, self.position[1]-self.size/2.0, self.size, self.size))
        
    #make the object jump
    def jump(self):
        self.velocity[1] -= 200

    def right(self):
        self.position[0] += self.size_info.current_w * 0.001

    def left(self):
        self.position[0] -= self.size_info.current_w * 0.001