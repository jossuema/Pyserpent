from turtle import pos
import pygame
import cubo as cb
import math
import random

class serpiente(object):
    cola = [] #Se usa un vector para la representar la posicion de la cola
    direccion = {} #Se usa un diccionario para la posicion de la cabeza y movimiento
    def __init__(self, color, pos):
        self.color = color
        self.cabeza = cb.cubo(pos)
        self.cola.append(self.cabeza)
        self.posx = 0
        self.posy = 1

    def mover(self):
        for event in pygame.event.get():

            #Captura de tecla para terminar el programa

            if event.type == pygame.QUIT:
                pygame.quit()

            #Captura de teclas para el movimiento w,a,s,d

            teclas = pygame.key.get_pressed()

            for i in teclas:
                if teclas[pygame.K_a]: #activacion tecla izquierda(a)
                    self.posx = -1 
                    self.posy = 0
                    self.direccion[self.cabeza.pos[:]] = [self.posx, self.posy]

                elif teclas[pygame.K_d]:
                    self.posx = 1
                    self.posy = 0
                    self.direccion[self.cabeza.pos[:]] = [self.posx, self.posy]

                elif teclas[pygame.K_w]:
                    self.posx = 0
                    self.posy = -1
                    self.direccion[self.cabeza.pos[:]] = [self.posx, self.posy]

                elif teclas[pygame.K_s]:
                    self.posx = 0
                    self.posy = 1
                    self.direccion[self.cabeza.pos[:]] = [self.posx, self.posy]
        
        for i, c in enumerate(self.cola):
            print(i)
            print(c)
            p = c.pos[:]
            if p in self.direccion:
                turn = self.direccion[p]
                c.mover(turn[0],turn[1])
                if i == len(self.cola)-1:
                    self.direccion.pop(p)
            else:
                if c.posx == -1 and c.pos[0] <= 0: c.pos = (c.cuadros-1, c.pos[1])
                elif c.posx == 1 and c.pos[0] >= c.cuadros-1: c.pos = (0,c.pos[1])
                elif c.posy == 1 and c.pos[1] >= c.cuadros-1: c.pos = (c.pos[0], 0)
                elif c.posy == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.cuadros-1)
                else: c.mover(c.posx,c.posy)


    def limpiar(self, pos):
        self.cabeza = cb.cubo(pos)
        self.cola = []
        self.cola.append(self.cabeza)
        self.direccion = {}
        self.posx = 0
        self.posy = 1


    def agregarcubo(self):
        cola = self.cola[-1]
        dx, dy = cola.posx, cola.posy

        if dx == 1 and dy == 0:
            self.cola.append(cb.cubo((cola.pos[0]-1,cola.pos[1])))
        elif dx == -1 and dy == 0:
            self.cola.append(cb.cubo((cola.pos[0]+1,cola.pos[1])))
        elif dx == 0 and dy == 1:
            self.cola.append(cb.cubo((cola.pos[0],cola.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.cola.append(cb.cubo((cola.pos[0],cola.pos[1]+1)))

        self.cola[-1].posx = dx
        self.cola[-1].posy = dy


    def dibujar(self, plano):
        for i, c in enumerate(self.cola):
            if i ==0:
                c.dibujar(plano, True)
            else:
                c.dibujar(plano)