import pygame

#de la ventana
ANCHO_VENTANA=1024
ALTO_VENTANA=768

#posicion
pos=(50,50)


#Colisiones
colisiones = [
    pygame.Rect(int(385 * 0.64), int(220 * 0.8533), 40, 40),  # puas LISTO
    pygame.Rect(int(1020 * 0.64), int(265 * 0.8533), 40, 40), # puas arriba derecha LISTO
    pygame.Rect(int(965 * 0.64), int(670 * 0.8533), 40, 40), # puas abajo derecha LISTO
    pygame.Rect(int(280 * 0.64), int(620 * 0.8533), 28, 64),   # columna 1 abajo izquierda LISTO
    pygame.Rect(int(1400 * 0.64), int(470 * 0.8533), 28, 64),  # columna 2 abajo derecha LISTO
    pygame.Rect(int(1210 * 0.64), int(200 * 0.8533), 28, 70),    # columna 3 la pared semi central derecha LISTO
    pygame.Rect(int(170 * 0.64), int(155 * 0.8533), 28, 64),    # columna 4 arriba izquierda LISTO
    pygame.Rect(int(1570 * 0.64), 0, 24, 900),    # pared derecha
    pygame.Rect(10, 0, 24, 900),    #pared izquierda
    pygame.Rect(0, 0, 1600, 24),    #pared arriba
    pygame.Rect(0, 870, 1600, 24),   #pared abajo
    pygame.Rect(int(1400 * 0.64), int(40 * 0.8533), 32, 50),  #lava arriba derecha LISTO
    pygame.Rect(int(430 * 0.64), int(800 * 0.8533), 32, 50)   #lava abajo izquierda LISTO
]


#todo listo en 1600x900

#tiempo entre cada flecha
TIEMPO_DISPARO = 365