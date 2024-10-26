import pygame

import constantes

from control_oleada import Gen_Ene_borde

pygame.init()

#configuracion pantallas
ventana=pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("Juego Oleadas")

#Objeto del jugador
class Jugador:
    def __init__(self, x, y):
        h = k = 50
        self.rect = pygame.Rect(x, y, h, k)
        self.sprite = pygame.image.load('Proyecto Informática\soldi.png')  # Cargar el sprite
        self.sprite = pygame.transform.scale(self.sprite, (h, k))  # Cambiar el tamaño según sea necesario

    def dibujar(self, ventana):
        ventana.blit(self.sprite, self.rect.topleft)

# Spawn del jugador
jugador = Jugador(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2)

# Variables para las oleadas
enemigos = []
oleada = 1
enemigos_por_oleada = 5
enemigos_restantes = enemigos_por_oleada
reloj = pygame.time.Clock()

# Bucle principal del juego
run = True
while run:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run = False

    # Generar enemigos para la oleada actual
    if enemigos_restantes > 0:
        enemigo = Gen_Ene_borde((jugador.rect.x, jugador.rect.y))
        enemigos.append(enemigo)
        enemigos_restantes -= 1
    elif not enemigos:  # Preparar la próxima oleada si no quedan enemigos
        oleada += 1
        enemigos_por_oleada += 3  # Aumentar dificultad
        enemigos_restantes = enemigos_por_oleada

    # Lógica de movimiento de los enemigos
    for enemigo in enemigos[:]:
        enemigo.mover_hacia_jugador(jugador.rect.center)
        if enemigo.rect.colliderect(jugador.rect):  # Colisión con el jugador
            run = False #CAMBIAR ESTO PARA LA PANTALLA GAME OVER
        if enemigo.rect.y < 0 or enemigo.rect.y > constantes.ALTO_VENTANA or enemigo.rect.x < 0 or enemigo.rect.x > constantes.ANCHO_VENTANA:
            enemigos.remove(enemigo)

    # Dibujar en pantalla
    ventana.fill((0, 0, 0))  # Fondo negro
    jugador.dibujar(ventana)
    for enemigo in enemigos:
        enemigo.dibujar(ventana)

    pygame.display.flip()
    reloj.tick(60)  # 60 FPS

pygame.quit()

