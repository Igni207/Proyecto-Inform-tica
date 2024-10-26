import pygame

import constantes

import interfaz

from personaje import Personaje

#Inicio
jugador=Personaje(x=50, y=50)
pygame.init()
ventana=pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Juego Oleadas")




#Interfaz y carga de cosas
#Música
pygame.mixer.music.load("musica/menu_musica.mp3")  #la música del menú
pygame.mixer.music.set_volume(0.5)  #para ajustar el volumen (0.0 a 1.0)
pygame.mixer.music.play(-1)  #para reproducirla en bucle




#Barra de vida
barra_vida = interfaz.BarraVida(vida_max=5, pos=(50, 50)) #se pueden cambiar la cant de vidas

#Botones

#botón de recibir daño y probar la vida
boton_rect = pygame.Rect(200, 400, 120, 50) #prueba temporal
color_boton1 = (200, 0, 0)  #prueba temporal

#botones de control de volumen
boton_volumen_up_rect = pygame.Rect(50, 300, 100, 50)
boton_volumen_down_rect = pygame.Rect(160, 300, 100, 50)
color_volumen = (255, 255, 0)




#Botón de jugar menu principal
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

    #Pantalla del menú, botones de volumen y boton de jugar
    if en_menu == True:
        #hacer que quede negro lo del menu
        ventana.fill((0, 0, 0))  #fondo negro para el menú
        font = pygame.font.Font(None, 50)
        texto_titulo = font.render("MENU PRINCIPAL", True, (255, 255, 255))
        texto_titulo_rect = texto_titulo.get_rect(center=(constantes.ANCHO_VENTANA // 2, 100))
        ventana.blit(texto_titulo, texto_titulo_rect)


        #botones de volumen
        pygame.draw.rect(ventana, color_volumen, boton_volumen_up_rect)
        texto_volumen_up = font.render("+Vol", True, (0, 0, 0))
        ventana.blit(texto_volumen_up, (boton_volumen_up_rect.x + 10, boton_volumen_up_rect.y + 10))

        pygame.draw.rect(ventana, color_volumen, boton_volumen_down_rect)
        texto_volumen_down = font.render("-Vol", True, (0, 0, 0))
        ventana.blit(texto_volumen_down, (boton_volumen_down_rect.x + 10, boton_volumen_down_rect.y + 10))





        
        #Mostrar Boton Jugar
        pygame.draw.rect(ventana, color_boton, boton_jugar_rect)
        texto_jugar = font.render("JUGAR", True, (255, 255, 255))
        texto_jugar_rect = texto_jugar.get_rect(center=boton_jugar_rect.center)
        ventana.blit(texto_jugar, texto_jugar_rect)
        

        #Cambiar del menú a la pantalla del juego y musica
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                run = False
            elif eventos.type == pygame.MOUSEBUTTONDOWN:
                #Boton Jugar
                if boton_jugar_rect.collidepoint(eventos.pos):
                    en_menu = False  #cambia del menu al juego
                    en_juego = True #arranca a jugar
                    pygame.mixer.music.load("musica/combate_musica.mp3")  # Carga la música del juego
                    pygame.mixer.music.play(-1)  # Reproduce en bucle
                # Botón de aumentar volumen
                elif boton_volumen_up_rect.collidepoint(eventos.pos):
                    if volumen < 1.0:
                        volumen += 0.1
                        pygame.mixer.music.set_volume(volumen)
                # Botón de disminuir volumen
                elif boton_volumen_down_rect.collidepoint(eventos.pos):
                    if volumen > 0.0:
                        volumen -= 0.1
                        pygame.mixer.music.set_volume(volumen)








    #Si arrancó a jugar se abre el "juego" y controlamos las vidas
    elif en_juego == True: #si arrancó a jugar:
        ventana.fill((173, 216, 230)) #fondo celeste
        jugador.dibujar(ventana)
        #mostrar la barra de vida
        barra_vida.dibujo_cor(ventana)
        #botón "Recibir Daño"
        pygame.draw.rect(ventana, color_boton1, boton_rect)
        texto_daño = font.render("Daño", True, (255, 255, 255))
        ventana.blit(texto_daño, (boton_rect.x + 15, boton_rect.y + 10))
        

        #controlar vidas para ver si se muere
        if barra_vida.vida_actual <= 0:
            game_over = True #se activa el fin
            en_juego = False #se termina el juego y nos cambia a game over



        #Recibir Daño Actualizar cuando tengamos enemigos
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                run = False
            elif eventos.type == pygame.MOUSEBUTTONDOWN:
                #botón de recibir daño que hay que borrar, el personaje recibe daño
                if boton_rect.collidepoint(eventos.pos):
                    barra_vida.recibir_daño()


    if game_over == True: #Si perdió, mostramos la pantalla de muerte
        ventana.fill((0, 0, 0))  #fondo negro de nuevo para GAME OVER
        font_game_over = pygame.font.Font(None, 70)
        texto_game_over = font_game_over.render("GAME OVER", True, (255, 0, 0))
        texto_game_over_rect = texto_game_over.get_rect(center=(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2))
        ventana.blit(texto_game_over, texto_game_over_rect)

    #comprobar que se cierre en la ultima ventana
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run=False       #lo logré














    pygame.time.delay(10)
    pygame.display.update()



pygame.quit()

