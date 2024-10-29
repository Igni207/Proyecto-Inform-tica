import pygame
import random

class Item:
    def __init__(self, x, y, item_type):
        h = k = 50
        self.rect = pygame.Rect(x, y, h, k)
        self.item_type = item_type
        if item_type == 1:
            self.sprite = pygame.image.load('imagenes/monedas.png')  #carga sprite moneda
            self.sprite = pygame.transform.scale(self.sprite, (h, k))  #tamaño
        if item_type == 2:
            self.sprite = pygame.image.load('imagenes/pocion_vida.png')
            self.sprite = pygame.transform.scale(self.sprite, (h, k))  #tamaño
        self.drop = random.choice(["True", "False"])

 
        
        

    def dibujar(self, ventana):
        ventana.blit(self.sprite, self.rect.topleft)

