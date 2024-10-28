import pygame
#mi personaje
class Jugador:
    def __init__(self, x, y):
        h = k = 50
        self.rect = pygame.Rect(x, y, h, k)
        self.sprite = pygame.image.load('E://Proyecto-Inform-tica-PINFOAlphaV0.0.3//Proyecto Informática//imagenes//soldi.png')  # Cargar el sprite
        self.sprite = pygame.transform.scale(self.sprite, (h, k))  # Cambiar el tamaño según sea necesario
        self.vida = 5

    def dibujar(self, ventana):
        ventana.blit(self.sprite, self.rect.topleft)

    def movimiento(self,delta_x,delta_y):
        self.rect.x = self.rect.x + delta_x
        self.rect.y = self.rect.y + delta_y

    def perder_vida(self):
        self.vida -= 1
        if self.vida <= 0:
            print("¡El jugador ha perdido todas sus vidas!")
            pygame.quit()
            exit()