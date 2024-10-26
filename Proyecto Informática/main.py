import pygame

import constantes

import interfaz

from personaje import Personaje

jugador=Personaje(x=50, y=50)
pygame.init()
ventana=pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Juego Oleadas")

#aquí creo la barra de vida, dejenme un espacio aquí para las cosas de interfaz
barra_vida = interfaz.BarraVida(vida_max=3, pos=(50, 50))


#botón de recibir daño y probar la vida
boton_rect = pygame.Rect(200, 400, 120, 50)  # posición y tamaño del botón
color_boton = (200, 0, 0)  # color para el botón


run=True
while run==True:

    ventana.fill((173, 216, 230))  #fondo con un color azul claro

    
    jugador.dibujar(ventana)

    #lo q pone en el boton
    font = pygame.font.Font(None, 30)
    texto = font.render("Recibir Daño", True, (255, 255, 255))
    ventana.blit(texto, (boton_rect.x + 10, boton_rect.y + 10))





    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run=False
        elif eventos.type == pygame.MOUSEBUTTONDOWN:
            # Si el jugador hace clic en el botón, el personaje recibe daño
            if boton_rect.collidepoint(eventos.pos):
                barra_vida.recibir_daño()

    #mostrar la barra de vida
    barra_vida.dibujo_cor(ventana)
    







    pygame.time.delay(10)
    pygame.display.update()



pygame.quit()

