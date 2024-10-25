import pygame

#coordenadas de donde aparece el pj
class Personaje():
    def __init__(self,x, y):
        self.forma = pygame.Rect(0,0,20,20)
        self.forma.center = (x,y)

    #donde aparece y como se lo ve
    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, (255, 255, 0), self.forma)
