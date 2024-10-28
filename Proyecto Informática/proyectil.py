import pygame
import math

class Proyectil:
    def __init__(self, x, y, direction):
        super().__init__()
        h = k = 20
        self.sprite = pygame.image.load('E://Proyecto-Inform-tica-PINFOAlphaV0.0.3//Proyecto Informática//imagenes//flecha.png')  # Cargar el sprite
        self.sprite = pygame.transform.scale(self.sprite, (h, k))  # Cambiar el tamaño según sea necesario
        self.speed = 10  
        self.direction = direction
        self.angle = direction  # Almacena la dirección
        self.rect = self.sprite.get_rect(center=(x, y))


    def update(self):
        # Actualiza la posición del proyectil
        self.rect.x += self.speed * math.cos(self.direction)
        self.rect.y += self.speed * math.sin(self.direction)
        # Elimina el proyectil si sale de la pantalla
        if not (0 <= self.rect.x <= 800 and 0 <= self.rect.y <= 600):
            return False  # Retorna False si el proyectil debe ser eliminado
        return True  # Retorna True si el proyectil sigue activo
    
    def dibujar(self, screen):
        # Rota el sprite y dibuja
        rotated_sprite = pygame.transform.rotate(self.sprite, -math.degrees(self.angle))  # Rota el sprite
        new_rect = rotated_sprite.get_rect(center=self.rect.center)  # Mantiene el centro al rotar
        screen.blit(rotated_sprite, new_rect.topleft)