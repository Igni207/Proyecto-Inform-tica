import pygame

#de la ventana
ANCHO_VENTANA=1600
ALTO_VENTANA=900

#posicion para botones
pos=(50,50)


#Colisiones
colisiones = [
    pygame.Rect(385, 220, 40, 40),  # puas LISTO
    pygame.Rect(1020, 265, 40, 40), # puas arriba derecha LISTO
    pygame.Rect(965, 670, 40, 40), # puas abajo derecha  LISTO
    pygame.Rect(280, 620, 28, 64),   # columna 1 abajo izquierda LISTO
    pygame.Rect(1400, 470, 28, 64),  # columna 2 abajo derecha LISTO
    pygame.Rect(1210, 200, 28, 70),    # columna 3 la pared semi central derecha LISTO
    pygame.Rect(170, 155, 28, 64),    # columna 4 arriba izquierda LISTO
    pygame.Rect(1570, 0, 24, 900),    # pared derecha
    pygame.Rect(10, 0, 24, 900),    #pared izquierda
    pygame.Rect(0, 0, 1600, 24),    #pared arriba
    pygame.Rect(0, 870, 1600, 24),   #pared abajo
    pygame.Rect(1400, 40, 32, 50),  #lava arriba derecha LISTO
    pygame.Rect(430, 800, 32, 50)   #lava abajo izquierda LISTO
]

#todo listo en 1600x900

#tiempo entre cada flecha
TIEMPO_DISPARO = 400