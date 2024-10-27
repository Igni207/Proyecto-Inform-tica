# estructure_enemy.py
import pygame
import math

class Enemigo:
    def __init__(self, x, y, velocidad, vida):
        h = k = 40
        self.rect = pygame.Rect(x, y, h, k)  #tamaño
        self.velocidad = velocidad
        self.vida = vida
        self.sprite = pygame.image.load('Imagenes/orc.png')  
        self.sprite = pygame.transform.scale(self.sprite, (h, k))  

    def mover_hacia_jugador(self, jugador_pos):
        dx, dy = jugador_pos[0] - self.rect.x, jugador_pos[1] - self.rect.y
        distancia = math.hypot(dx, dy)
        if distancia > 0:
            dx, dy = dx / distancia, dy / distancia
            self.rect.x += dx * self.velocidad
            self.rect.y += dy * self.velocidad

    def dibujar(self, ventana):
        ventana.blit(self.sprite, self.rect.topleft)

    def recibir_daño_enemigo(self, daño):
        self.vida -= daño
        if self.vida <= 0:
            return True  #para saber q se muere el enemigo
        return False
