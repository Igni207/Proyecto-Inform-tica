import pygame

class Moneda:
    def __init__(self, x, y):
        super().__init__()
        h = k = 20
        self.rect = pygame.Rect(x, y, h, k)
        self.sprite = pygame.image.load('Proyecto Informática/imagenes/monedas.png')  # Cargar el sprite
        self.sprite = pygame.transform.scale(self.sprite, (h, k))  # Cambiar el tamaño según sea necesario
    
    def dibujar(self, screen):
        screen.blit(self.sprite, self.rect)  # Dibuja el sprite en la pantalla
