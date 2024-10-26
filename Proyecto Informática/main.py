import pygame
import constantes
from control_oleada import Gen_Ene_borde
import interfaz
from jugador import Jugador 

mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

pygame.init()

#configuracion pantallas
ventana=pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Juego Oleadas")

# Spawn del jugador
jugador = Jugador(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2)

# Variables para las oleadas
enemigos = []
oleada = 1
enemigos_por_oleada = 5
enemigos_restantes = enemigos_por_oleada
reloj = pygame.time.Clock()

#aquí creo la barra de vida, dejenme un espacio aquí para las cosas de interfaz
barra_vida = interfaz.BarraVida(vida_max=3, pos=(50, 50))

# Bucle principal del juego
run = True
while run:
    #SALUD
    pygame.display.update()

    delta_x = 0
    delta_y = 0

    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run = False
        if eventos.type == pygame.KEYDOWN:
            if eventos.key == pygame.K_a:
                mover_izquierda = True
            if eventos.key == pygame.K_d:
                mover_derecha = True
            if eventos.key == pygame.K_w:
                mover_arriba = True
            if eventos.key == pygame.K_s:
                mover_abajo = True
        if eventos.type == pygame.KEYUP:
            if eventos.key == pygame.K_a:
                mover_izquierda = False
            if eventos.key == pygame.K_d:
                mover_derecha = False
            if eventos.key == pygame.K_w:
                mover_arriba = False
            if eventos.key == pygame.K_s:
                mover_abajo = False

    # Manejar movimiento
    if mover_derecha:
        delta_x = 2
    if mover_izquierda:
        delta_x = -2
    if mover_arriba:
        delta_y = -2
    if mover_abajo:
        delta_y = 2

    # Mover al jugador
    jugador.movimiento(delta_x, delta_y)

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
    jugador.dibujar(ventana)  # Dibuja el jugador
    for enemigo in enemigos:
        enemigo.dibujar(ventana)  # Dibuja enemigos
        #mostrar la barra de vida
    barra_vida.dibujo_cor(ventana)

    pygame.display.flip()  # Actualiza la pantalla
    reloj.tick(60)  # 60 FPS
pygame.quit()