import pygame
import constantes
import interfaz 
import proyectil
import math
from jugador import Jugador
from control_oleada import Gen_Ene_borde
from estructure_enemy import Enemigo
from proyectil import Proyectil
from items import Item


pygame.init()



#para el movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#para el proyectil
proyectiles = []
enemigos = []
daño = 1
ultimo_disparo = pygame.time.get_ticks() #tiempo entre disparos
puede_disparar = True

#config pantallas
ventana=pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Juego Oleadas")

#fondo
fondo = pygame.image.load("imagenes/juego.png").convert()
fondo = pygame.transform.scale(fondo, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)) 


#spawn del jugador
jugador = Jugador(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2)


#tiempo de inmortalidad despues de un golpe
invulnerable = False
tiempo_invulnerable = 0  #temporizador para invulnerabilidad
duracion_invulnerable = 1.5  #duración en segundos


#Variables para las oleadas
enemigos = []
oleada = 1
enemigos_por_oleada = 5
enemigos_restantes = enemigos_por_oleada
reloj = pygame.time.Clock()


#items
#moneda = Item(constantes.ANCHO_VENTANA//3, constantes.ALTO_VENTANA//3, 1)
#pocion_vida = Item(constantes.ANCHO_VENTANA//5, constantes.ALTO_VENTANA//5, 2)
pociones=[]
monedas=[]
cant_nec_pocion=0
cant_nec_moneda=0





#Interfaz y botones (Igni)

#fuente así estilo medieval
fuente = pygame.font.Font("Fuente/AncientModernTales-a7Po.ttf", 80)


#Música
pygame.mixer.music.load("musica/menu_musica.mp3")  #la música del menú
pygame.mixer.music.set_volume(0.3)  #para ajustar el volumen, hagan q no se pase de 1.0
pygame.mixer.music.play(-1)  #bucle
musica_game_over = pygame.mixer.Sound("musica/game_over.mp3")
musica_win = pygame.mixer.Sound("musica/victoria.mp3") 



#Barra de vida
barra_vida = interfaz.BarraVida(vida_max=5, pos=(50, 50)) #se pueden cambiar la cant de vidas
#Cont de oleadas
contador_oleadas = interfaz.ContadorOleadas(pos=(constantes.ANCHO_VENTANA - 200, 50))
#Cont de monedas
contador_monedas = interfaz.ContadorMonedas((50, 100))


#Botones


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
victoria = False
volumen = 0.5  #volumen inicial para la música












run=True
while run==True:

    #para actualizar la pantalla
    pygame.display.update()
    
    delta_x = 0
    delta_y = 0
    #invulnerabilidad tras golpe
    if invulnerable == True:
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
                #botonesn de volumen
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

        #boton de jugar :D
        texto_jugar = fuente.render("JUGAR", True, (255, 255, 255))
        ancho_texto_jugar = texto_jugar.get_width()
        alto_texto_jugar = texto_jugar.get_height()
        boton_jugar_rect = pygame.Rect((constantes.ANCHO_VENTANA - ancho_texto_jugar) // 2, 200, ancho_texto_jugar, alto_texto_jugar)
        ventana.blit(texto_jugar, boton_jugar_rect)


        #botón volumen + 
        texto_volumen_up = fuente.render("+Vol", True, (255, 255, 255))
        boton_volumen_up_rect = texto_volumen_up.get_rect(topleft=(10, constantes.ALTO_VENTANA - 360))  #10 y 360 son los pixeles para el borde 
        ventana.blit(texto_volumen_up, boton_volumen_up_rect)

        #botón volumen -
        texto_volumen_down = fuente.render("-Vol", True, (255, 255, 255))
        boton_volumen_down_rect = texto_volumen_down.get_rect(topleft=(10, constantes.ALTO_VENTANA - 270)) #lo dejo en 270 pq sino se solapan y se rompe si le damos a los 2
        ventana.blit(texto_volumen_down, boton_volumen_down_rect)


    #logica juego activo
    elif en_juego == True: 


        ventana.blit(fondo, (0, 0)) 
        jugador.dibujar(ventana)
        barra_vida.dibujo_cor(ventana)
        contador_oleadas.dibujar(ventana)
        contador_monedas.dibujar(ventana)
        
        

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




        #movimiento cuando choca con el mapa
        for colision in constantes.colisiones:
            if jugador.rect.colliderect(colision):
                if mover_izquierda == True:
                    jugador.rect.x += 2
                elif mover_derecha == True:
                    jugador.rect.x -= 2
                elif mover_arriba == True:
                    jugador.rect.y += 2
                elif mover_abajo == True:
                    jugador.rect.y -= 2
        
        #guardemos esto por si hay q mover las hitbox otra vez
        #for colision in constantes.colisiones:
        #    pygame.draw.rect(ventana, (255, 0, 0), colision, 2)

        #control flecha
        tiempo_actual = pygame.time.get_ticks()

        
        if eventos.type == pygame.MOUSEBUTTONDOWN:
            if eventos.button == 1: 
                if tiempo_actual - ultimo_disparo >= constantes.TIEMPO_DISPARO:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    dx = mouse_x - jugador.rect.centerx
                    dy = mouse_y - jugador.rect.centery
                    direction = math.atan2(dy, dx)
                    proyectil = Proyectil(jugador.rect.centerx, jugador.rect.centery, direction)
                    proyectiles.append(proyectil)
                    ultimo_disparo = tiempo_actual


        for proyectil in proyectiles[:]:
            proyectil.update()
            #comprobar colision de la flecha con el enemigo
            enemigos_golpeados = [enemigo for enemigo in enemigos if proyectil.rect.colliderect(enemigo.rect)]
            if enemigos_golpeados:
                for enemigo in enemigos_golpeados:
                    if enemigo.recibir_daño_enemigo(daño):  #si recibe daño
                        enemigos.remove(enemigo)  #lo eliminamos
                        enemigo_eliminado = "SI"
                        if enemigo_eliminado == "SI":
                            cant_nec_pocion+=1
                            if cant_nec_pocion==3:
                                pocion_vida = Item(enemigo.rect.x, enemigo.rect.y, 2)
                                pocion = pocion_vida
                                pociones.append(pocion)
                                cant_nec_pocion=0
                            cant_nec_moneda +=1
                            if cant_nec_moneda==5:
                                moneda = Item(enemigo.rect.x, enemigo.rect.y, 1)
                                moneda_list = moneda
                                monedas.append(moneda_list)
                                cant_nec_moneda=0


                proyectiles.remove(proyectil)

        for pocion in pociones[:]:
            if pocion_vida.drop == ("True"):
                pocion_vida.dibujar(ventana)

            if jugador.rect.colliderect(pocion_vida.rect):
                if barra_vida.vida_actual < 5:
                    barra_vida.vida_actual+=1
                pociones.remove(pocion)

        for moneda_list in monedas[:]:
            if moneda.drop == ("True"):
                moneda.dibujar(ventana)

            if jugador.rect.colliderect(moneda.rect):
                contador_monedas.recoger_moneda()
                
                monedas.remove(moneda_list)



        for proyectil in proyectiles:
            proyectil.dibujar(ventana)






        #generar enemigos para la oleada actual
        if enemigos_restantes > 0:
            enemigo = Gen_Ene_borde((jugador.rect.x, jugador.rect.y))
            enemigos.append(enemigo)
            enemigos_restantes -= 1
        elif not enemigos:  #prox oleada si no hay enemigos
            oleada += 1
            enemigos_por_oleada += 3  #aumentando la cant de enemigos :D
            enemigos_restantes = enemigos_por_oleada
            contador_oleadas.siguiente_oleada() #de interfaz
        #movimiento enemigos
        for enemigo in enemigos[:]:
            enemigo.mover_hacia_jugador(jugador.rect.center)
            #daño a la barra de vida
            if enemigo.rect.colliderect(jugador.rect):
                if not invulnerable:
                    barra_vida.recibir_daño()
                    invulnerable = True  #se hace invencible
                    tiempo_invulnerable = duracion_invulnerable  #para reiniciar el tiempo
                if barra_vida.vida_actual <= 0:
                    en_juego = False
                    game_over = True        
            if enemigo.rect.y < 0 or enemigo.rect.y > constantes.ALTO_VENTANA or enemigo.rect.x < 0 or enemigo.rect.x > constantes.ANCHO_VENTANA:
                enemigos.remove(enemigo) #eso borra al enemigo que sale de la pantalla verdad?
        for enemigo in enemigos:
            enemigo.dibujar(ventana)  #dibuja los enemigos



        #suponiendo que esto está dentro de algo estilo if jugador.rect.colliderect(moneda.rect):
        #Digamos que aquí esta lo de las monedas, dentro del ciclo, cuando agarren las monedas
        #vamos a usar esta función de aquí: contador_monedas.recoger_moneda()
        #de esa forma aumenta el contador :D
        #para ganar
        #if self.monedas >= 10:
        #   victoria == True





    #Pantalla Game Over :c
    elif game_over==True:
        ventana.fill((0, 0, 0))
        texto_game_over = fuente.render("GAME OVER", True, (255, 0, 0))
        ventana.blit(texto_game_over, texto_game_over.get_rect(center=(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2)))


        #musica game over
        pygame.mixer.music.stop()  #para la musica de combate
        musica_game_over.set_volume(0.3) #bajar volumen dios mio
        musica_game_over.play()  #reproduce game over

    #Pantalla de la Massive Victory de este equipo que terminó el juego :D
    elif victoria == True:
        ventana.fill((0,0,0))
        texto_victoria = fuente.render("COMPLETASTE EL JUEGO")
        ventana.blit(texto_victoria, (100, 300))
        #gracias por jugar
        fuente_pequeña = pygame.font.Font("Fuente/AncientModernTales-a7Po.ttf", 40)  #letra mas chica
        texto_gracias = fuente_pequeña.render("Gracias por jugar", True, (255, 255, 255))
        ventana.blit(texto_gracias, texto_gracias.get_rect(center=(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2 - 50)))
    
        #Nosotros B)
        nombres = ["Desarrolladores:", "Alzogaray", "Quinteros", "Lopez", "Chocobar", "Sandoval", "Luna"]
        posicion_verti = (constantes.ALTO_VENTANA // 2 + 50)  #donde salen

        for nombre in nombres:
            texto_nombre = fuente_pequeña.render(nombre, True, (255, 255, 255))
            ventana.blit(texto_nombre, texto_nombre.get_rect(center=(constantes.ANCHO_VENTANA // 2, posicion_verti)))
            posicion_verti += 50  #espacio entre nombres
        
        #Musica de victoria
        pygame.mixer.music.stop()  #para la musica de combate
        musica_win.set_volume(0.3) #bajar volumen dios mio
        musica_win.play()  #reproduce Massive Victory

    pygame.display.flip()  #actualizar pantalla
    reloj.tick(60)  # 60 FPS



pygame.quit()

