import pygame
import math

class Proyectil:
    def __init__(self, x, y, direction):
        super().__init__()
        h = k = 20
        self.sprite = pygame.image.load('imagenes/flecha.png')  #sprite flecha
        self.sprite = pygame.transform.scale(self.sprite, (h, k)) 
        self.speed = 10  
        self.direction = direction
        self.angle = direction  #almacena la dirección
        self.rect = self.sprite.get_rect(center=(x, y))


    def update(self):
        #posicion flecha
        self.rect.x += self.speed * math.cos(self.direction)
        self.rect.y += self.speed * math.sin(self.direction)
        #borrar flecha
        if not (0 <= self.rect.x <= 800 and 0 <= self.rect.y <= 600):
            return False  #hay que eliminarlo
        return True  #sigue activo
    
    def dibujar(self, screen):
        #para rotar el sprite
        rotar_sprite = pygame.transform.rotate(self.sprite, -math.degrees(self.angle))  #rota el sprite
        new_rect = rotar_sprite.get_rect(center=self.rect.center)  #mantiene centrado si rota
        screen.blit(rotar_sprite, new_rect.topleft)