import pygame

import constantes


pygame.init()


ventana=pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))


pygame.display.set_caption("Juego Oleadas")


run=True
while run==True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            run=False
pygame.quit()

