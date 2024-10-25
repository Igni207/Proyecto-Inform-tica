import pygame

import constantes

from personaje import Personaje

jugador=Personaje(x=50, y=50)


pygame.init()


ventana=pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))


pygame.display.set_caption("Juego Oleadas")


run=True
while run==True:

    jugador.dibujar(ventana)




    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run=False


    pygame.display.update()



pygame.quit()

