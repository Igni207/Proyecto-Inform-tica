import pygame
import math
from interfaz import ANCHO, ALTO
from personaje import (Personaje)

Jugador=Personaje (50, 50)

pygame.init()

pantalla=pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("NOMBRE DEL JUEGO")

mover_arriba=False
mover_abajo=False
mover_izquierda=False
mover_derecha=False

run=True
while run:

    delta_x=0
    delta_y=0

    if mover_derecha==True:
        delta_x=5
    if mover_izquierda==True:
        delta_x=-5
    if mover_arriba==True:
        delta_y=-5
    if mover_abajo==True:
        delta_y=-5

    Jugador.movimiento(delta_x,delta_y)

    Jugador.dibujar(pantalla)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                mover_izquierda=True
            if event.key==pygame.K_d:
                mover_derecha=True
            if event.key==pygame.K_w:
                mover_arriba=True
            if event.key==pygame.K_s:
                mover_abajo=True
            
            print(f"{delta_x},{delta_y}")
    pygame.display.update()

pygame.quit()