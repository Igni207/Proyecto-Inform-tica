import pygame
import math
from jugador import Jugador
from proyectil import Proyectil
from estructure_enemy import Enemigo
from control_oleada import Gen_Ene_borde
import constantes
import interfaz
import time

pygame.init()
ventana=pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

#spawn jugador
jugador = Jugador(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2)

#Barra de vida
barra_vida = interfaz.BarraVida(vida_max=5, pos=(50, 50)) #se pueden cambiar la cant de vidas


# Crear una instancia del jugador
proyectiles = []
enemigos = []
oleada = 1
enemigos_por_oleada = 2
enemigos_restantes = enemigos_por_oleada
monedas_recogidas = 0 
dano=1
reloj = pygame.time.Clock()
tiempo_descanso = 3.5
tiempo_descanso = 4

#tiempo de inmortalidad despues de un golpe
invulnerable = False
tiempo_invulnerable = 0  #temporizador para invulnerabilidad
duracion_invulnerable = 1.5  #duración en segundos

# Puedes ajustar la lógica de generación
contador_enemigos = 0  # Contador para controlar la generación de enemigos
tiempo_generacion = 60  # Por ejemplo, genera un enemigo cada 60 frames

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - jugador.rect.centerx
                dy = mouse_y - jugador.rect.centery
                direction = math.atan2(dy, dx)
                proyectil = Proyectil(jugador.rect.centerx, jugador.rect.centery, direction)
                proyectiles.append(proyectil)

    #generar enemigos para la oleada actual
    if enemigos_restantes > 0:
        enemigo = Gen_Ene_borde((jugador.rect.x, jugador.rect.y),oleada)
        enemigos.append(enemigo)
        enemigos_restantes -= 1
    elif not enemigos:  # Preparar la próxima oleada si no quedan 
        print(f"tiempo de {tiempo_descanso} antes de la proxima ronda")
        time.sleep(tiempo_descanso)
        oleada += 1
        enemigos_por_oleada += 2  # Aumentar dificultad, aumentando la cant de enemigos :D
        enemigos_restantes = enemigos_por_oleada
    
    enemigos_a_eliminar = []  # Lista para almacenar enemigos que deben ser eliminados
    #movimiento enemigos
    for enemigo in enemigos[:]:
        enemigo.mover_hacia_jugador(jugador.rect.center)

        #la barra de vida
        if enemigo.rect.colliderect(jugador.rect):
            if not invulnerable:
                barra_vida.recibir_daño()
                invulnerable = True  # Activar invulnerabilidad
                tiempo_invulnerable = duracion_invulnerable  # Reiniciar el temporizador de invulnerabilidad
            if barra_vida.vida_actual <= 0:
                en_juego = False
                game_over = True        
        if enemigo.rect.y < 0 or enemigo.rect.y > constantes.ALTO_VENTANA or enemigo.rect.x < 0 or enemigo.rect.x > constantes.ANCHO_VENTANA:
            enemigos.remove(enemigo) #eso borra al enemigo que sale de la pantalla verdad?
    for enemigo in enemigos:
        enemigo.dibujar(ventana)  # Dibuja enemigos

    # Actualizar proyectiles
    for proyectil in proyectiles[:]:
        proyectil.update()
        # Comprobar colisiones con enemigos
        enemigos_golpeados = [enemigo for enemigo in enemigos if proyectil.rect.colliderect(enemigo.rect)]
        for enemigo in enemigos_golpeados:
            if enemigo.recibir_dano(dano):  # Si el enemigo recibe daño
                enemigos.remove(enemigo)  # Eliminar enemigo después de la colisión
            if proyectil in proyectiles:  # Verifica si el proyectil está en la lista
                proyectiles.remove(proyectil)  # Eliminar proyectil después de la colisión

    # Comprobar colisiones entre jugador y enemigos
    colisiones_jugador = [enemigo for enemigo in enemigos if jugador.rect.colliderect(enemigo.rect)]
    if colisiones_jugador:
        jugador.perder_vida()

    if monedas_recogidas >= 7:  # condición de victoria
        print("¡Has recogido 7 monedas! ¡Ganaste!")
        running = False 

    # Limpiar la pantalla
    ventana.fill((0, 0, 0))
    
    # Dibujar el jugador
    jugador.dibujar(ventana)
    
    # Dibujar proyectiles
    for proyectil in proyectiles:
        proyectil.dibujar(ventana)  # Usar el método dibujar del proyectil

    # Dibujar enemigos
    for enemigo in enemigos:
        enemigo.dibujar(ventana)

    # Mostrar información en pantalla
    vidas_texto = font.render(f"Vidas: {jugador.vida}", True, (255, 255, 255))
    monedas_texto = font.render(f"Monedas: {monedas_recogidas}", True, (255, 255, 255))
    ventana.blit(vidas_texto, (10, 10))
    ventana.blit(monedas_texto, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
