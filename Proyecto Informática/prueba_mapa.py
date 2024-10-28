import pygame
import os

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
ANCHO_VENTANA = 1300  # Ajusta a la resolución que prefieras
ALTO_VENTANA = 700
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Juego con Fondo y Colisiones")

# Cargar la imagen del fondo
fondo = pygame.image.load("E://Proyecto-Inform-tica-PINFOAlphaV0.0.3//Proyecto Informática//imagenes//juego.png").convert()

# Escalar el fondo al tamaño de la ventana
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))    

# Definir los objetos con colisión (las columnas y antorchas) como rectángulos
colisiones = [
    pygame.Rect(310, 175, 32, 32),  # Colision puas
    pygame.Rect(830, 210, 32, 32),  # Colision puas
    pygame.Rect(785, 525, 32, 32),  # Colision puas
    pygame.Rect(225, 465, 28, 64),   # Colision columna 1
    pygame.Rect(1135, 360, 28, 64),   # Colision columna 2
    pygame.Rect(985, 150, 28, 70),   # Colision columna 3
    pygame.Rect(135, 120, 28, 64),   # Colision columna 4
    pygame.Rect(1275, 0, 24, 700),   # Colision paredes
    pygame.Rect(10, 0, 24, 700),
    pygame.Rect(0, 0, 1300, 24),
    pygame.Rect(0, 0, 1300, 24),
    pygame.Rect(0, 665, 1300, 24),
    pygame.Rect(1130, 30, 32, 50),
    pygame.Rect(350, 625, 32, 50)
]

# Ejemplo de un rectángulo para el jugador
jugador = pygame.Rect(300, 220, 32, 32)
velocidad = 1

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad
    if teclas[pygame.K_UP]:
        jugador.y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador.y += velocidad

    # Detección de colisiones
    for colision in colisiones:
        if jugador.colliderect(colision):
            print("Colisión detectada")
            # Aquí puedes definir qué sucede en caso de colisión. Por ejemplo:
            # mover al jugador hacia atrás para simular que no puede atravesar el objeto
            if teclas[pygame.K_LEFT]:
                jugador.x += velocidad
            if teclas[pygame.K_RIGHT]:
                jugador.x -= velocidad
            if teclas[pygame.K_UP]:
                jugador.y += velocidad
            if teclas[pygame.K_DOWN]:
                jugador.y -= velocidad

    # Dibujar el fondo y el jugador
    ventana.blit(fondo, (0, 0))  # Dibuja el fondo
    pygame.draw.rect(ventana, (255, 0, 0), jugador)  # Dibuja el jugador (rojo)
    
    # Opcional: dibujar las colisiones para visualizarlas (puedes quitar esto)
    for colision in colisiones:
        pygame.draw.rect(ventana, (0, 255, 0), colision, 2)  # Dibuja los objetos de colisión en verde

    pygame.display.flip()

# Cerrar Pygame
pygame.quit()
