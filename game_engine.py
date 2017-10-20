# -*- coding: utf-8 -*-
"""
Idea fair simple android game
@author: Chris Minar
game engine class
"""

import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame
from game_object import game_object, button, estrela, Bullet, qualquercoisa
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
        #Add square to object list

        self.player = game_object(self.screen, self.SCREEN_SIZE, [486/2.0, 864/2.0], [0,0], self.OBJECT_COLOR, self.object_size)
        #self.player = Player(486/2.0, 864/2.0, self.screen, self.SCREEN_SIZE)

        #self.objects.append(self.player)
        
        #Reset floor height based on new screen size
        self.floor_height = 864 - 864/10.0

        sizeX = (486/3.0)-2
        sizeY = 864/10.0-4

        self.botaoEsquerda = button(self.screen, self.SCREEN_SIZE, (100,100,100), [2+sizeX/2, 2+self.floor_height+sizeY/2], [sizeX, sizeY])
        self.objects.append(self.botaoEsquerda)

        self.botaoDireita = button(self.screen, self.SCREEN_SIZE, (100,100,100), [(sizeX+2)+(sizeX+2)+sizeX/2, 2+self.floor_height+sizeY/2], [sizeX, sizeY])
        self.objects.append(self.botaoDireita)

        self.botaoCentro = button(self.screen, self.SCREEN_SIZE, (255,0,0), [(sizeX+3)+sizeX/2, 2+self.floor_height+sizeY/2], [sizeX, sizeY])
        self.objects.append(self.botaoCentro)

        self.botaoTeste = button(self.screen, self.SCREEN_SIZE, (255,255,255), [0, 0], [50, 50])
        self.objects.append(self.botaoTeste)

        self.naveali = qualquercoisa(self.screen, self.SCREEN_SIZE, [470/2.0, 848/2.0], [0, 0], (255,255,255))

        self.estrelas = []
        self.bullets = []
        for i in range(0,100):
            self.estrelas.append(estrela(self.screen,self.SCREEN_SIZE,[random.randint(1,486),random.randint(1,864)]))

    """handle key presses"""
    def event_loop(self):
        #For each event that has happened(each keystroke):
        for event in pygame.event.get():

            #if(event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEWHEEL):
            self.botaoTeste.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            #print event.which

            #self.lastEvent = str(event.type)

            #Add keys pressed to self.keys so we can access it outside of this function (this is currently not used)
            self.keys = pygame.key.get_pressed()

            '''self.lastEvent = []

            if (event.type == 1792 or event.type == 1793):
                #print str(event)
                #self.lastEvent = str(event)

                textobemgrande = str(event)

                while len(textobemgrande) > 50:
                    self.lastEvent.append(textobemgrande[0:50])
                    textobemgrande = textobemgrande[50:]

                self.lastEvent.append(textobemgrande)'''



            #If the key is a left mouse click or android touch make the square jump
            if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN):
                #x, y = event.pos
                try:
                    x = event.x * self.SCREEN_SIZE[0]
                    y = event.y * self.SCREEN_SIZE[1]
                except:
                    x, y = event.pos

                try:
                    clickId = event.fingerId
                except:
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

                try:
                    clickId = event.fingerId
                except:
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
            self.player.right()
            self.naveali.right()

        if self.left:
            self.player.left()
            self.naveali.left()
    
    """update velocity and position of all game objects"""
    def update_physics(self):
        newtime = time.time()
        dt = newtime-self.gametime
        self.gametime = newtime

        ratioPosition = self.player.velocity[1]*dt + 0.5*self.gravity*dt**2
        ratioPosition = self.naveali.velocity[1]*dt + 0.5*self.gravity*dt**2
        ratioVelocity = self.gravity*dt

        # x = x_0 + v_0*dt + 0.5*g*dt^2 
        self.player.position[1] += ratioPosition
        self.naveali.position[1] += ratioPosition
        # v = v_0 + g*dt 
        self.player.velocity[1] += ratioVelocity
        self.naveali.velocity[1] += ratioVelocity
        #make sure it doesn't go through the floor
        if self.naveali.position[1] > self.floor_height-70:

            self.player.position[1] = self.floor_height-70
            self.naveali.position[1] = self.floor_height-70

            self.player.velocity[1] = 0.0
            self.naveali.velocity[1] = 0.0

        if 0 > self.naveali.position[1]:
            self.player.position[1] = 0
            self.naveali.position[1] = 0
            self.player.velocity[1] = 0.0
            self.naveali.velocity[1] = 0.0
            
    """main game loop"""
    def game_loop(self):
        while not self.done:
            #set background color
            self.screen.fill(self.BACKGROUND_COLOR)
            #check for and handle button presses
            self.event_loop()
            #advance the time for all objects
            self.update_physics()

            '''textoY = 50

            group = pygame.sprite.Group()

            for texto in self.lastEvent:

                font = pygame.font.Font("DejaVuSans.ttf", 24)
                text = font.render(texto, True, (255, 255, 255, 255))

                base = pygame.sprite.Sprite()

                base.image = text

                base.rect = base.image.get_rect()

                base.rect.x = 50
                base.rect.y = textoY                

                group.add(base)

                textoY += 70

            group.draw(self.screen)'''

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
                gameobject.draw()

            for bullet in self.bullets:
                bullet.update()
                if 0 > bullet.position[1]:
                    self.bullets.remove(bullet)
                    bullet = None
                else:
                    bullet.draw()

            self.naveali.update()
            self.naveali.draw(self.screen)

            pygame.display.update()

            if 100 > len(self.estrelas):
                self.estrelas.append(estrela(self.screen,self.SCREEN_SIZE,[random.randint(1,486),0]))

            self.clock.tick(self.fps)

            
    def quit_game(self):
        pygame.display.quit()
        pygame.quit()