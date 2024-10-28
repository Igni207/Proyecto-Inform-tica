# estructure_enemy.py
import pygame
import math

class Enemigo:
    def __init__(self, x, y, velocidad, vida):
        h = k = 40
        self.rect = pygame.Rect(x, y, h, k)  # Tamaño del enemigo
        velocidad = 3
        vida = 3
        self.velocidad = velocidad
        self.vida = vida
        self.sprite = pygame.image.load('E://Proyecto-Inform-tica-PINFOAlphaV0.0.3//Proyecto Informática//imagenes//orc.png')  # Cargar el sprite
        self.sprite = pygame.transform.scale(self.sprite, (h, k))  # Cambiar el tamaño según sea necesario

    def mover_hacia_jugador(self, jugador_pos):
        dx, dy = jugador_pos[0] - self.rect.x, jugador_pos[1] - self.rect.y
        distancia = math.hypot(dx, dy)
        if distancia > 0:
            dx, dy = dx / distancia, dy / distancia
            self.rect.x += dx * self.velocidad
            self.rect.y += dy * self.velocidad

    def dibujar(self, ventana):
        ventana.blit(self.sprite, self.rect.topleft)

    def recibir_dano(self, dano):
        dano = 1
        self.vida -= dano
        return self.vida <= 0  # Devuelve True si el enemigo ha muerto
