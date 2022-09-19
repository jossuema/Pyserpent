import pygame
import math
import random
import tkinter as tkw


class cubo(object):
    cuadros = 20
    w = 500
    def __init__(self,start,posx=1,posy=0,color=(255,0,0)):
        self.pos = start
        self.posx = 1
        self.posy = 0
        self.color = color


    def mover(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.pos = (self.pos[0] + self.posx, self.pos[1] + self.posy)

    def dibujar(self, plano, eyes=False):
        dis = self.w // self.cuadros
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(plano, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(plano, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(plano, (0,0,0), circleMiddle2, radius)