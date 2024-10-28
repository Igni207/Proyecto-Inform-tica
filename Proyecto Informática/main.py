import pygame
import constantes
import interfaz 
import time
from jugador import Jugador
from control_oleada import Gen_Ene_borde

#para el movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

pygame.init()

#config pantallas
ventana=pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Juego Oleadas")

#spawn del jugador
jugador = Jugador(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2)

#tiempo de inmortalidad despues de un golpe
invulnerable = False
tiempo_invulnerable = 0  #temporizador para invulnerabilidad
duracion_invulnerable = 1.5  #duración en segundos

#Variables para las oleadasaaa
enemigos = []
oleada = 1
enemigos_por_oleada = 5
enemigos_restantes = enemigos_por_oleada
reloj = pygame.time.Clock()
tiempo_descanso = 5
tiempo_descanso = 4

#Interfaz y botones (Igni)
#fuente así estilo medieval
fuente = pygame.font.Font("Proyecto Informática\Fuente\AncientModernTales-a7Po.ttf", 80)

#Música
pygame.mixer.music.load("Proyecto Informática\musica\menu_musica.mp3")  #la música del menú
pygame.mixer.music.set_volume(0.3)  #para ajustar el volumen (0.0 a 1.0)
pygame.mixer.music.play(-1)  #para reproducirla en bucle
musica_game_over = pygame.mixer.Sound("Proyecto Informática\musica\game_over.mp3")

#Barra de vida
barra_vida = interfaz.BarraVida(vida_max=5, pos=(50, 50)) #se pueden cambiar la cant de vidas

#Botones

#botón de recibir daño y probar la vida
boton_volumen_up_rect = pygame.Rect(50, 300, 100, 50)
boton_volumen_down_rect = pygame.Rect(160, 300, 100, 50)
boton_jugar_rect = pygame.Rect((constantes.ANCHO_VENTANA - 150) // 2, 300, 150, 50)
color_boton_volumen = (255, 255, 0)
color_boton_jugar = (0, 200, 0)

#botón de jugar menu principal
boton_jugar_width, boton_jugar_height = 150, 50
boton_jugar_rect = pygame.Rect((constantes.ANCHO_VENTANA - boton_jugar_width) // 2,
                                300, boton_jugar_width, boton_jugar_height)
color_boton = (0, 200, 0)  

#estado del juego, True si estamos en el menú, False si estamos en el juego
en_menu = True
en_juego = False
game_over = False
volumen = 0.5  #volumen inicial para la música


run=True
while run==True:

    #para actualizar la pantalla
    pygame.display.update()
    
    delta_x = 0
    delta_y = 0
    #invulnerabilidad tras golpe
    if invulnerable:
        tiempo_invulnerable -= reloj.get_time() / 1000  #Resta el tiempo
        if tiempo_invulnerable <= 0:  
            invulnerable = False  #ya no es invulnerable



    #Gestionemos los eventos para tener más orden
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run = False


        #eventos del menú:
        if en_menu == True:
            if eventos.type ==pygame.MOUSEBUTTONDOWN:
                if boton_jugar_rect.collidepoint(eventos.pos):
                    en_menu = False
                    en_juego = True #para cambiar del menú al juego
                    pygame.mixer.music.load("Proyecto Informática\musica\combate_musica.mp3") #carga musica menu
                    pygame.mixer.music.play(-1) #bucle
                #botones
                elif boton_volumen_up_rect.collidepoint(eventos.pos):
                    if volumen < 1.0:
                        volumen += 0.1
                        pygame.mixer.music.set_volume(volumen)
                elif boton_volumen_down_rect.collidepoint(eventos.pos):
                    if volumen > 0.0:
                        volumen -= 0.1
                        pygame.mixer.music.set_volume(volumen)

        elif en_juego == True:
            #movimiento
            if eventos.type == pygame.KEYDOWN:
                if eventos.key == pygame.K_a:
                    mover_izquierda = True
                elif eventos.key == pygame.K_d:
                    mover_derecha = True
                elif eventos.key == pygame.K_w:
                    mover_arriba = True
                elif eventos.key == pygame.K_s:
                    mover_abajo = True
            elif eventos.type == pygame.KEYUP:
                if eventos.key == pygame.K_a:
                    mover_izquierda = False
                elif eventos.key == pygame.K_d:
                    mover_derecha = False
                elif eventos.key == pygame.K_w:
                    mover_arriba = False
                elif eventos.key == pygame.K_s:
                    mover_abajo = False



    #logica del menu
    if en_menu == True:
        #hacer que quede negro lo del menu
        ventana.fill((0, 0, 0))  #fondo negro para el menú

        texto_titulo = fuente.render("MENU PRINCIPAL", True, (255, 255, 255))
        ventana.blit(texto_titulo, texto_titulo.get_rect(center=(constantes.ANCHO_VENTANA // 2, 100)))

        #boton de jugar nuevo :D
        texto_jugar = fuente.render("JUGAR", True, (255, 255, 255))
        ancho_texto_jugar = texto_jugar.get_width()
        alto_texto_jugar = texto_jugar.get_height()
        boton_jugar_rect = pygame.Rect((constantes.ANCHO_VENTANA - ancho_texto_jugar) // 2, 200, ancho_texto_jugar, alto_texto_jugar)
        ventana.blit(texto_jugar, boton_jugar_rect)


        # Botón de volumen + 
        texto_volumen_up = fuente.render("+Vol", True, (255, 255, 255))
        boton_volumen_up_rect = texto_volumen_up.get_rect(topleft=(10, constantes.ALTO_VENTANA - 360))  #10 y 360 son los pixeles para el borde 
        ventana.blit(texto_volumen_up, boton_volumen_up_rect)

        # Botón de volumen -
        texto_volumen_down = fuente.render("-Vol", True, (255, 255, 255))
        boton_volumen_down_rect = texto_volumen_down.get_rect(topleft=(10, constantes.ALTO_VENTANA - 270)) 
        ventana.blit(texto_volumen_down, boton_volumen_down_rect)


    #logica juego activo
    elif en_juego == True: 

        ventana.fill((173, 216, 230))
        jugador.dibujar(ventana)
        barra_vida.dibujo_cor(ventana)
        #movimiento del jugador
        if mover_derecha:
            delta_x = 2
        if mover_izquierda:
            delta_x = -2
        if mover_arriba:
            delta_y = -2
        if mover_abajo:
            delta_y = 2
        jugador.movimiento(delta_x, delta_y)

        #generar enemigos para la oleada actual
        if enemigos_restantes > 0:
            enemigo = Gen_Ene_borde((jugador.rect.x, jugador.rect.y),oleada)
            enemigos.append(enemigo)
            enemigos_restantes -= 1
        elif not enemigos:  # Preparar la próxima oleada si no quedan enemigos
            print(f"tiempo de {tiempo_descanso} antes de la proxima ronda")
            time.sleep(tiempo_descanso)
            oleada += 1
            enemigos_por_oleada += 2  # Aumentar dificultad, aumentando la cant de enemigos :D
            enemigos_restantes = enemigos_por_oleada
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
    #Game Over :c
    elif game_over==True:
        ventana.fill((0, 0, 0))
        texto_game_over = fuente.render("GAME OVER", True, (255, 0, 0))
        ventana.blit(texto_game_over, texto_game_over.get_rect(center=(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2 - 150)))
    
        #gracias por jugar
        fuente_pequeña = pygame.font.Font("Proyecto Informática\Fuente\AncientModernTales-a7Po.ttf", 40)  #letra mas chica
        texto_gracias = fuente_pequeña.render("Gracias por jugar", True, (255, 255, 255))
        ventana.blit(texto_gracias, texto_gracias.get_rect(center=(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2 - 50)))
    
        #Nosotros B)
        nombres = ["Desarrolladores:", "Alzogaray", "Quinteros", "Lopez", "Chocobar", "Sandoval", "Luna"]
        y_posicion = constantes.ALTO_VENTANA // 2 + 50  #donde salen

        for nombre in nombres:
            texto_nombre = fuente_pequeña.render(nombre, True, (255, 255, 255))
            ventana.blit(texto_nombre, texto_nombre.get_rect(center=(constantes.ANCHO_VENTANA // 2, y_posicion)))
            y_posicion += 50  #espacio entre nombres

        #musica game over
        pygame.mixer.music.stop()  #para la musica de combate
        musica_game_over.set_volume(0.3) #bajar volumen dios mio
        musica_game_over.play()  #reproduce game over

    pygame.display.flip()  #actualizar pantalla
    reloj.tick(60)  # 60 FPS

pygame.quit()