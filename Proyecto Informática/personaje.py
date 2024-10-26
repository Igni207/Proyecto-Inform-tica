import pygame

#coordenadas de donde aparece el pj
class Personaje():
    def __init__(self,x, y):
        self.forma = pygame.Rect(0,0,20,20)
        self.forma.center = (x,y)

    #donde aparece y como se lo ve
    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, (255, 255, 0), self.forma)
    
    # Método para mover al personaje
    def movimiento(self, delta_x, delta_y):
        self.forma.x += delta_x
        self.forma.y += delta_y