import pygame
import constantes
import interfaz 
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
duracion_invulnerable = 3  #duración en segundos


#Variables para las oleadas
enemigos = []
oleada = 1
enemigos_por_oleada = 5
enemigos_restantes = enemigos_por_oleada
reloj = pygame.time.Clock()





#Interfaz y botones (Igni)
#Música
pygame.mixer.music.load("musica/menu_musica.mp3")  #la música del menú
pygame.mixer.music.set_volume(0.3)  #para ajustar el volumen (0.0 a 1.0)
pygame.mixer.music.play(-1)  #para reproducirla en bucle



#Barra de vida
barra_vida = interfaz.BarraVida(vida_max=5, pos=(50, 50)) #se pueden cambiar la cant de vidas

#Botones

#botón de recibir daño y probar la vida, LO BORRAMOS APENAS TENGAMOS COLISIONES
boton_rect = pygame.Rect(200, 400, 120, 50) #prueba temporal
color_boton1 = (200, 0, 0)  #prueba temporal
boton_volumen_up_rect = pygame.Rect(50, 300, 100, 50)
boton_volumen_down_rect = pygame.Rect(160, 300, 100, 50)
boton_jugar_rect = pygame.Rect((constantes.ANCHO_VENTANA - 150) // 2, 300, 150, 50)
color_boton_volumen = (255, 255, 0)
color_boton_jugar = (0, 200, 0)

#botones de control de volumen
boton_volumen_up_rect = pygame.Rect(50, 300, 100, 50)
boton_volumen_down_rect = pygame.Rect(160, 300, 100, 50)
color_volumen = (255, 255, 0)




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
                    pygame.mixer.music.load("musica/combate_musica.mp3") #carga musica menu
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
        font = pygame.font.Font(None, 50)
        texto_titulo = font.render("MENU PRINCIPAL", True, (255, 255, 255))
        ventana.blit(texto_titulo, texto_titulo.get_rect(center=(constantes.ANCHO_VENTANA // 2, 100)))

        pygame.draw.rect(ventana, color_boton_jugar, boton_jugar_rect)
        ventana.blit(font.render("JUGAR", True, (255, 255, 255)), boton_jugar_rect.move(25, 10))

        pygame.draw.rect(ventana, color_boton_volumen, boton_volumen_up_rect)
        ventana.blit(font.render("+Vol", True, (0, 0, 0)), boton_volumen_up_rect.move(10, 10))

        pygame.draw.rect(ventana, color_boton_volumen, boton_volumen_down_rect)
        ventana.blit(font.render("-Vol", True, (0, 0, 0)), boton_volumen_down_rect.move(10, 10))


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
            enemigo = Gen_Ene_borde((jugador.rect.x, jugador.rect.y))
            enemigos.append(enemigo)
            enemigos_restantes -= 1
        elif not enemigos:  # Preparar la próxima oleada si no quedan enemigos
            oleada += 1
            enemigos_por_oleada += 3  # Aumentar dificultad, aumentando la cant de enemigos :D
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
        font_game_over = pygame.font.Font(None, 70)
        texto_game_over = font_game_over.render("GAME OVER", True, (255, 0, 0))
        ventana.blit(texto_game_over, texto_game_over.get_rect(center=(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2)))





    pygame.display.flip()  # Actualiza la pantalla
    reloj.tick(60)  # 60 FPS



pygame.quit()

