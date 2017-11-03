# -*- coding: utf-8 -*-
"""
Idea fair simple android game
@author: Chris Minar
game engine class
"""

import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame
from game_object import button, Bullet, qualquercoisa, enemy
from objects import estrela
import time
import random

class game_engine():
    #
    # Class Members
    #
    # Pygame variables
    SCREEN_SIZE = (500,500)
    BACKGROUND_COLOR = (1,1,1)
    CAPTION = "Sample Android Game"
    done = False
    fps = 30.0
    # Game variables
    GROUND_COLOR = (255,255,255)
    OBJECT_COLOR = (255,255,0)
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

        self.clock = pygame.time.Clock()
        #self.lastEvent = ""

        self.touching = []

        #Set screen size to be the screen resolution
        size_info = pygame.display.Info()
        self.SCREEN_SIZE=(size_info.current_w,size_info.current_h)
        self.object_size = 20
        #self.SCREEN_SIZE=(486,864)
        #self.SCREEN_SIZE=(243,432)
        self.right = False
        self.left = False

        self.ratioX = self.SCREEN_SIZE[0] / 486.0
        self.ratioY = self.SCREEN_SIZE[1] / 864.0

        #os.environ["SDL_VIDO_CENTERED"] = "TRUE"
        #Finish initialising pygame
        pygame.display.set_caption(self.CAPTION)
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.screen_rect = self.screen.get_rect()
        self.keys = pygame.key.get_pressed()

        #Reset floor height based on new screen size
        self.floor_height = 864 - 864/10.0

        self.botaoEsquerda = button(self.screen, self.SCREEN_SIZE, 'images/direction_button_pressed.png', 'images/direction_button.png', [2, 2+self.floor_height])

        self.botaoEsquerda.ligado = pygame.transform.flip(self.botaoEsquerda.ligado, True, False)
        self.botaoEsquerda.desligado = pygame.transform.flip(self.botaoEsquerda.desligado, True, False)
        self.botaoEsquerda.imagem.image = pygame.transform.flip(self.botaoEsquerda.imagem.image, True, False)

        self.objects.append(self.botaoEsquerda)

        self.botaoCentro = button(self.screen, self.SCREEN_SIZE, 'images/shoot_pressed.png', 'images/shoot.png', [163, 2+self.floor_height])
        self.objects.append(self.botaoCentro)

        self.botaoDireita = button(self.screen, self.SCREEN_SIZE, 'images/direction_button_pressed.png', 'images/direction_button.png', [324, 2+self.floor_height])
        self.objects.append(self.botaoDireita)

        self.naveali = qualquercoisa(self.screen, self.SCREEN_SIZE, [470/2.0, 848/2.0], [0, 0], (255,255,255))

        self.enemy = enemy(self.screen, self.SCREEN_SIZE, [470/2.0, 20])

        self.estrelas = []
        self.bullets = []
        for _ in range(0,100):
            self.estrelas.append(estrela.estrela(self.screen,self.SCREEN_SIZE,[random.randint(1,486),random.randint(1,864)]))

    def event_loop(self):
        #For each event that has happened(each keystroke):
        for event in pygame.event.get():

            #if(event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEWHEEL):
            #self.botaoTeste.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            #print event.which

            #self.lastEvent = str(event.type)

            #Add keys pressed to self.keys so we can access it outside of this function (this is currently not used)
            self.keys = pygame.key.get_pressed()

            #If the key is a left mouse click or android touch make the square jump
            if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN):
                #x, y = event.pos
                if event.type == pygame.FINGERDOWN:
                    x = event.x * self.SCREEN_SIZE[0]
                    y = event.y * self.SCREEN_SIZE[1]
                    clickId = event.fingerId
                else:
                    x, y = event.pos
                    clickId = event.which

                if y > self.floor_height * self.ratioY:
                    if x > (self.SCREEN_SIZE[0]/3.0)*2:
                        self.botaoDireita.ligar()
                        self.right = True
                        self.touching.append([clickId,"right"])
                    elif x < self.SCREEN_SIZE[0]/3.0:
                        self.botaoEsquerda.ligar()
                        self.left = True
                        self.touching.append([clickId,"left"])
                    else:
                        self.botaoCentro.ligar()
                        self.bullets.append(Bullet(self.screen,self.SCREEN_SIZE,[self.naveali.position[0]+16,self.naveali.position[1]]))
                        self.touching.append([clickId,"shot"])

            if (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.FINGERUP):

                if event.type == pygame.FINGERUP:
                    clickId = event.fingerId
                else:
                    clickId = event.which

                for touch in self.touching:
                    if touch[0] == clickId:
                        if touch[1] == "right":
                            self.botaoDireita.desligar()
                            self.right = False
                        elif touch[1] == "left":
                            self.botaoEsquerda.desligar()
                            self.left = False
                        elif touch[1] == "shot":
                            self.botaoCentro.desligar()
                        self.touching.remove(touch)

            #If the key pressed is the android back button, kill the program
            elif event.type == pygame.K_AC_BACK:
                self.done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True

        if self.right:
            self.naveali.right()

        if self.left:
            self.naveali.left()

    def update_physics(self):
        newtime = time.time()
        dt = newtime-self.gametime
        self.gametime = newtime

        ratioPosition = self.naveali.velocity[1]*dt + 0.5*self.gravity*dt**2
        ratioVelocity = self.gravity*dt

        # x = x_0 + v_0*dt + 0.5*g*dt^2
        self.naveali.position[1] += ratioPosition
        # v = v_0 + g*dt
        self.naveali.velocity[1] += ratioVelocity
        #make sure it doesn't go through the floor
        if self.naveali.position[1] > self.floor_height-70:
            self.naveali.position[1] = self.floor_height-70
            self.naveali.velocity[1] = 0.0

        if 0 > self.naveali.position[1]:
            self.naveali.position[1] = 0
            self.naveali.velocity[1] = 0.0

    def game_loop(self):
        while not self.done:
            #set background color
            self.screen.fill(self.BACKGROUND_COLOR)
            #check for and handle button presses
            self.event_loop()
            #advance the time for all objects
            self.update_physics()

            #draw stars
            for eachestrela in self.estrelas:

                eachestrela.descer()

                if eachestrela.position[1] > self.floor_height:
                    self.estrelas.remove(eachestrela)
                    eachestrela = None
                else:
                    eachestrela.draw()

            #Draw all objects
            for gameobject in self.objects:
                gameobject.update()
                gameobject.draw(self.screen)

            for bullet in self.bullets:
                bullet.update()
                if 0 > bullet.position[1]:
                    self.bullets.remove(bullet)
                    bullet = None
                else:
                    bullet.draw()

            self.naveali.update()
            self.naveali.draw(self.screen)

            self.enemy.update()
            self.enemy.draw(self.screen)

            pygame.display.update()

            if 100 > len(self.estrelas):
                self.estrelas.append(estrela.estrela(self.screen,self.SCREEN_SIZE,[random.randint(1,486),0]))

            self.clock.tick(self.fps)

    @classmethod
    def quit_game(self):
        pygame.display.quit()
        pygame.quit()