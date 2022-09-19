from http.client import OK
import math
import random
import pygame
import tkinter as tk
import cubo as cb
import serpiente as sp
from tkinter import messagebox

#Funcion para dibujar 

def Dibujarventana(plano):
    global cuadros, alto, s, comida
    plano.fill((0,0,0))
    s.dibujar(plano)
    comida.dibujar(plano)
    pygame.display.update()

#Retorna dos valores randoms para la posicion de comida
#Compara la posicion de la cola de la serpiente y los valores randoms generados
def randomComida(cuadros, objeto):

    posicion = objeto.cola

    while True:
        x = random.randrange(cuadros) #genera numeros del 0 al 19
        y = random.randrange(cuadros)
        if len(list(filter(lambda z:z.pos == (x,y), posicion))) > 0:
            continue
        else:
            break

    return (x,y)


def mensaje(titulo, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(titulo, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global alto, cuadros, s, comida
    alto = 500
    cuadros = 20
    win = pygame.display.set_mode((alto, alto)) #Iniciar ventana
    s = sp.serpiente((125,0,256), (0,0)) #Crea el objeto serpiente
    comida = cb.cubo(randomComida(cuadros, s), color=(255,255,0)) #Crea el objeto cubo(comida)
    OK = True 
    contador = 0
    clock = pygame.time.Clock()
    while OK:
        pygame.time.delay(50)
        clock.tick(10)
        s.mover()
        if s.cola[0].pos == comida.pos:
            s.agregarcubo() #Se agrega un bloque de cola
            
            if contador == 0:
                comida = cb.cubo(randomComida(cuadros, s), color=(0,0,255)) #azul
                contador = contador +1
            elif contador == 1:
                comida = cb.cubo(randomComida(cuadros, s), color=(255,0,0)) #rojo
                contador = contador +1
            elif contador == 2:
                comida = cb.cubo(randomComida(cuadros, s), color=(255,255,0)) #amarillo
                contador = 0
            
            #Se genera otra comida

        for x in range(len(s.cola)):
            if s.cola[x].pos in list(map(lambda z:z.pos,s.cola[x+1:])):
                puntaje = str(len(s.cola))
                mensaje('Perdiste!!', 'Tu puntaje: '+puntaje)
                s.limpiar((10,10))
                

        Dibujarventana(win)


    pass



main()
