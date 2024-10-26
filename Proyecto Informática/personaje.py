import pygame
from principal import delta_x,delta_y

ANCHO_PJ=20
ALTO_PJ=20
COLOR_PJ=(160,32,240)

class Personaje():
    def __init__(self,x,y):
        self.forma=pygame.Rect(0,0,ANCHO_PJ,ALTO_PJ) #estoy creando el personaje como un rectangulo  
        self.forma.center=(x,y)
    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz,(COLOR_PJ),self.forma)
    def movimiento(self,delta_x,delta_y):
        self.forma.x=self.forma.x+delta_x
        self.forma.y=self.forma.y+delta_y