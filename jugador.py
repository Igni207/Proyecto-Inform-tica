import pygame
#el personaje
class Jugador:
    def __init__(self, x, y):
        h = k = 50
        self.rect = pygame.Rect(x, y, h, k)
        self.sprite = pygame.image.load('Imagenes/soldi.png') 
        self.sprite = pygame.transform.scale(self.sprite, (h, k)) 

    def dibujar(self, ventana):
        ventana.blit(self.sprite, self.rect.topleft)

    def movimiento(self,delta_x,delta_y):
        self.rect.x = self.rect.x + delta_x
        self.rect.y = self.rect.y + delta_y 

