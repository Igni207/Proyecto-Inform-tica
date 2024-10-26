import pygame
import math
from interfaz_fexx import ANCHO, ALTO
from personaje import Personaje

# Crear el objeto Personaje
Jugador = Personaje(50, 50)

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("NOMBRE DEL JUEGO")

mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

run = True
while run:
    delta_x = 0
    delta_y = 0

    # Manejar movimiento
    if mover_derecha:
        delta_x = 1
    if mover_izquierda:
        delta_x = -1
    if mover_arriba:
        delta_y = -1
    if mover_abajo:
        delta_y = 1

    # Mover al jugador
    Jugador.movimiento(delta_x, delta_y)

    # Limpiar la pantalla
    pantalla.fill((0, 0, 0))  # Rellenar la pantalla de negro

    # Dibujar al jugador
    Jugador.dibujar(pantalla)

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
        if event.type == pygame.KEYUP:  # Para detener el movimiento al soltar la tecla
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
            
            print(f"{delta_x},{delta_y}")
    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()
