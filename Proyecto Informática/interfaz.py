import pygame

#Intento de Corazones

class BarraVida:
    def __init__(self, vida_max, pos):
        self.vida_max = vida_max
        self.vida_actual = vida_max
        self.pos = pos
        #cargo las imagenes, las podemos cambiar sin drama
        self.vida_full = pygame.image.load("imagenes/corazon_vivo.png")
        self.vida_vacia = pygame.image.load("imagenes/corazon_muerto.png")
        #para cambiarle el tamaño a los corazones
        self.vida_full = pygame.transform.scale(self.vida_full, (40, 40))
        self.vida_vacia= pygame.transform.scale(self.vida_vacia, (40, 40))
    def dibujo_cor(self, screen):
        for i in range (self.vida_max):
            if i < self.vida_actual:
                #para dibujar en la pantalla principal
                screen.blit(self.vida_full, (self.pos[0] + i * 50, self.pos[1]))
            else:
                screen.blit(self.vida_vacia, (self.pos[0] + i * 50, self.pos[1]))
    #recibir daño
    def recibir_daño(self):
        if self.vida_actual > 0:
            self.vida_actual -=1
            