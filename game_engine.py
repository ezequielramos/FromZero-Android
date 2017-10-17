# -*- coding: utf-8 -*-
"""
Idea fair simple android game
@author: Chris Minar
game engine class
"""

import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame
from game_object import game_object as go
import time

class game_engine():
    #
    # Class Members
    #
    # Pygame variables
    SCREEN_SIZE = (500,500)
    BACKGROUND_COLOR = (50,50,50)
    CAPTION = "Sample Android Game"
    done = False
    fps = 30.0
    # Game variables
    GROUND_COLOR = (255,255,255)
    OBJECT_COLOR = (255,0,0)
    gravity = 9.81*10.0
    object_size = 20
    objects = []
    gametime = time.time()

    #
    # Class Methods
    #
    """called when this class is initialised"""
    def __init__(self):
        # Initialise Pygame window
        pygame.init()

        #Set screen size to be the screen resolution
        size_info = pygame.display.Info()
        self.SCREEN_SIZE=(size_info.current_w,size_info.current_h)
        self.object_size = 20
        #self.SCREEN_SIZE=(1024,720)
        self.right = False
        self.left = False

        #os.environ["SDL_VIDO_CENTERED"] = "TRUE"
        #Finish initialising pygame
        pygame.display.set_caption(self.CAPTION)
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.screen_rect = self.screen.get_rect()
        self.keys = pygame.key.get_pressed()
        #Add square to object list
        self.objects.append(go(self.screen, [self.SCREEN_SIZE[0]/2.0, self.SCREEN_SIZE[1]/2.0], [0,0], self.OBJECT_COLOR, self.object_size))
        #Reset floor height based on new screen size
        self.floor_height = self.SCREEN_SIZE[1]/2.0

    """handle key presses"""
    def event_loop(self):
        #For each event that has happened(each keystroke):
        for event in pygame.event.get():
            #Add keys pressed to self.keys so we can access it outside of this function (this is currently not used)
            self.keys = pygame.key.get_pressed()
            #If the key is a left mouse click or android touch make the square jump
            if (event.type == pygame.MOUSEBUTTONDOWN) and event.button == 1:
                x, y = event.pos

                if y < self.SCREEN_SIZE[1]/2.0:
                    self.objects[0].jump()

                if y > self.SCREEN_SIZE[1]/2.0:
                    if x > self.SCREEN_SIZE[0]/2.0:
                        self.right = True
                    if x < self.SCREEN_SIZE[0]/2.0:
                        self.left = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                x, y = event.pos
                if y > self.SCREEN_SIZE[1]/2.0:
                    if x > self.SCREEN_SIZE[0]/2.0:
                        self.right = False
                    if x < self.SCREEN_SIZE[0]/2.0:
                        self.left = False

            #If the key pressed is the android back button, kill the program
            elif event.type == pygame.K_AC_BACK:
                self.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True

            print self.right

        if self.right:
            self.objects[0].right()

        if self.left:
            self.objects[0].left()
    
    """update velocity and position of all game objects"""
    def update_physics(self):
        newtime = time.time()
        dt = newtime-self.gametime
        self.gametime = newtime
        #take one timestep for each object in the objects list
        for gameobject in self.objects:
            # x = x_0 + v_0*dt + 0.5*g*dt^2 
            gameobject.position[1] = gameobject.position[1] + gameobject.velocity[1]*dt + 0.5*self.gravity*dt**2
            # v = v_0 + g*dt 
            gameobject.velocity[1] = gameobject.velocity[1] + self.gravity*dt
            #make sure it doesn't go through the floor
            if gameobject.position[1] > self.floor_height:
                gameobject.position[1] = self.floor_height
                gameobject.velocity[1] = 0.0

            if gameobject.position[1] < 0:
                gameobject.position[1] = 0
                gameobject.velocity[1] = 0.0
            
    """main game loop"""
    def game_loop(self):
        while not self.done:
            #set background color
            self.screen.fill(self.BACKGROUND_COLOR)
            #draw floor
            pygame.draw.line(self.screen, self.GROUND_COLOR, (0,self.SCREEN_SIZE[1]/2.0+self.object_size/2.0), (self.SCREEN_SIZE[0],self.SCREEN_SIZE[1]/2.0+self.object_size/2.0))
            #check for and handle button presses
            self.event_loop()
            #advance the time for all objects
            self.update_physics()
            #Draw all objects
            for gameobject in self.objects:
                gameobject.draw()
            pygame.display.update()
            
    def quit_game(self):
        pygame.display.quit()
        pygame.quit()